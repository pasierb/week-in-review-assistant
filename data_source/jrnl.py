from data_source.base import BaseDataSource
import subprocess


class JrnlDataSource(BaseDataSource):
    def __init__(self, description: str):
        super().__init__(description=description)

    def get_data(self):
        result = subprocess.run(['jrnl', '-n', '10'], capture_output=True, text=True)
        return result.stdout
