from data_source.base import BaseDataSource
import subprocess
from typing import List, Optional

class GitCommitsDataSource(BaseDataSource):
    def __init__(self, description: str, repo_dirs: list[str], args: Optional[List[str]] = None):
        super().__init__(description=description)
        self.repo_dirs = repo_dirs
        self.args = args or []
    def get_data(self) -> str:
        results = []

        for repo_dir in self.repo_dirs:
            # Get the current directory
            result = subprocess.run([
                'git',
                'log',
                '--pretty=format:%nCommit Date: %ad%nTitle: %s%nDescription: %b%n%n---',
                '--date=short',
                *self.args,
            ], capture_output=True, text=True, cwd=repo_dir)
            results.append(result.stdout)

        return "\n".join(results)
