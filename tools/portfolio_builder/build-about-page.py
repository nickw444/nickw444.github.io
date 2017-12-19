import argparse
from dtos import Project, Contribution, ConfigFile
import json
from jinja2 import Template

from logging import getLogger
logger = getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description='Update Website About Page.')
    parser.add_argument('data', help='Path to portfolio data')
    parser.add_argument('output', help='Path to about page to output')
    args = parser.parse_args()
    data_file = open(args.data)

    data = ConfigFile.deserialize(json.load(data_file))

    projects = data.projects
    for project in projects:
        print(project)

    about_template = Template(open('templates/about.html').read())
    output_file = open(args.output, 'w')
    output_file.write(about_template.render(
        projects=projects,
        contributions=data.contributions
    ))

if __name__ == '__main__':
    main()
