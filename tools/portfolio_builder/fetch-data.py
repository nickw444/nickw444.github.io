import argparse
from github import Github
from typing import Dict, List
import json
import yaml
import re
import os
from dtos import Project, Contribution, ConfigFile

import logging
logger = logging.getLogger(__name__)

PULL_URL_RE = re.compile(r'github.com/(.+)/pull/([0-9]+)$')
ISSUES_URL_RE = re.compile(r'github.com/(.+)/issues/([0-9]+)$')

def main():
    logging.basicConfig(level=logging.INFO)
    access_token = os.environ['ACCESS_TOKEN']
    parser = argparse.ArgumentParser(description='Update Website Portfolio.')
    parser.add_argument('config_file', help='Path to portfolio configuration')
    parser.add_argument('output', help='Path to portfolio file to output')
    args = parser.parse_args()
    config_file = open(args.config_file)

    g = Github(access_token)

    config = ConfigFile.deserialize(yaml.load(config_file))

    for project in config.projects:
        if project.repo is not None:
            logger.info('Fetching additional info for {}'.format(project.repo))
            try:
                gh_repo = g.get_repo(project.repo)
                project.url = gh_repo.html_url
                # Fill out any extra info we can fetch
                if project.languages is None:
                    if gh_repo.language:
                        project.languages = [gh_repo.language]

                if project.title is None:
                    project.title = gh_repo.name

                if project.description is None:
                    project.description = gh_repo.description

            except Exception as e:
                logger.error('Error whilst fetching {}: {}'.format(project.repo, e))
                continue

    for contribution in config.contributions:
        if contribution.description is None:
            logger.info('Fetching additional info for {}'.format(contribution))
            if contribution.pull is not None:
                match = PULL_URL_RE.search(contribution.pull)
                if match is None:
                    logger.error('Was unable to match pull URL: {}'.format(contribution.pull))
                else:
                    repo, pull_number = match.group(1), int(match.group(2))
                    pull = g.get_repo(repo).get_pull(pull_number)
                    contribution.description = pull.title

            elif contribution.issue is not None:
                match = ISSUES_URL_RE.search(contribution.issue)
                if match is None:
                    logger.error('Was unable to match issue URL: {}'.format(contribution.issue))
                else:
                    repo, issue_number = match.group(1), int(match.group(2))
                    issue = g.get_repo(repo).get_issue(issue_number)
                    contribution.description = issue.title

    output_file = open(args.output, 'w')
    json.dump(config.serialize(), output_file)

if __name__ == '__main__':
    main()

