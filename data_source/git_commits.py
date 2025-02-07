from data_source.base import BaseDataSource
import subprocess


class GitCommitsDataSource(BaseDataSource):
    def __init__(self, description: str, repo_dirs: list[str]):
        super().__init__(description=description)
        self.repo_dirs = repo_dirs

    def get_data(self) -> str:
        results = []

        for repo_dir in self.repo_dirs:
            # Get the current directory
            result = subprocess.run([
                'git',
                'log',
                '--pretty=format:%nCommit Date: %ad%nTitle: %s%nDescription: %b%n%n---',
                '--date=short',
                '--since=1 week ago'
            ], capture_output=True, text=True, cwd=repo_dir)
            results.append(result.stdout)

        return "\n".join(results)
