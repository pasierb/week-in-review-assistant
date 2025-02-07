from data_source.base import BaseDataSource
import subprocess
from typing import List, Optional


class JrnlDataSource(BaseDataSource):
    def __init__(self, description: str, args: Optional[List[str]] = None):
        super().__init__(description=description)
        self.args = args or ['-n', '10']  # Default to showing last 10 entries if no args provided

    def get_data(self):
        result = subprocess.run(['jrnl'] + self.args, capture_output=True, text=True)
        return result.stdout
