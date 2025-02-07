from data_source.base import BaseDataSource
from typing import List
from io import StringIO


class BaseProcessor:
    def __init__(self, system_prompt: str, data_sources: List[BaseDataSource]):
        self.system_prompt = system_prompt
        self.data_sources = data_sources

    def process(self) -> str:
        data_source_results = [str(data_source) for data_source in self.data_sources]

        buffer = StringIO()
        buffer.write(self.system_prompt)
        buffer.write("\n\n---\n\n")
        buffer.write('\n\n'.join(data_source_results))

        return buffer.getvalue()

