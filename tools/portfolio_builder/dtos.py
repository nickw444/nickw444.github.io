from typing import Dict, List

class Project():
    def __init__(self, repo: str, title: str, languages: List[str],
                 featured: bool, description: str, url: str) -> None:
        self.repo = repo
        self.title = title
        self.languages = languages
        self.featured = featured
        self.description = description
        self.url = url

    @staticmethod
    def deserialize(data: Dict) -> 'Project':
        return Project(
            repo=data.get('repo'),
            title=data.get('title'),
            languages=data.get('languages'),
            featured=data.get('featured', False),
            description=data.get('description'),
            url=data.get('url'),
        )

    def serialize(self) -> Dict:
        return {
            'repo': self.repo,
            'title': self.title,
            'languages': self.languages,
            'featured': self.featured,
            'description': self.description,
            'url': self.url,
        }

    def __repr__(self) -> str:
        return '<Project repo={} title={}>'.format(self.repo, self.title)

class Contribution():
    def __init__(self, pull: str, issue: str, description: str) -> None:
        self.pull = pull
        self.issue = issue
        self.description = description

    @staticmethod
    def deserialize(data: Dict) -> 'Contribution':
        return Contribution(
            pull=data.get('pull'),
            issue=data.get('issue'),
            description=data.get('description')
        )

    def serialize(self) -> Dict:
        return {
            'pull': self.pull,
            'issue': self.issue,
            'description': self.description,
        }

    def __repr__(self) -> str:
        return '<Contribution description={}>'.format(self.description)

class ConfigFile():
    def __init__(self, projects: List[Project], contributions: List[Contribution]) -> None:
        self.projects = projects
        self.contributions = contributions

    @staticmethod
    def deserialize(data: Dict) -> 'ConfigFile':
        projects = [Project.deserialize(o) for o in data['projects']]
        contributions = [Contribution.deserialize(o) for o in data['contributions']]
        return ConfigFile(contributions=contributions, projects=projects)

    def serialize(self) -> Dict:
        return {
            'projects': [p.serialize() for p in self.projects],
            'contributions': [c.serialize() for c in self.contributions],
        }

    def __repr__(self) -> str:
        return '<ConfigFile: {} projects, {} contributions>'.format(
            len(self.projects), len(self.contributions))
