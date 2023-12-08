from abc import ABC
from typing import Union, List, Dict

from knext import rest
from knext.component.builder.base import SourceReader


class CsvSourceReader(SourceReader):
    """A source component that reading data from CSV file.

    Args:
        local_path: The local path of CSV file.
        columns: The column names that need to be read from the CSV file.
        start_row: The starting number of rows read from the CSV file.
                    If the CSV file includes a header, it needs to be greater than or equal to 2.
    Examples:
        source = SourceCsvComponent(
                    local_path="./builder/job/data/App.csv",
                    columns=["id", 'riskMark', 'useCert'],
                    start_row=2
                )
    """

    """The local path of CSV file."""
    local_path: str
    """The column names that need to be read from the CSV file."""
    columns: List[str]
    """The starting number of rows read from the CSV file.
    If the CSV file includes a header, it needs to be greater than or equal to 2."""
    start_row: int

    def invoke(self, input):
        pass

    def submit(self):
        pass

    def to_rest(self):
        """Transforms `SourceCsvComponent` to REST model `CsvSourceNodeConfig`."""

        config = rest.CsvSourceNodeConfig(
            start_row=self.start_row, url=self.local_path, columns=self.columns
        )
        return rest.Node(**super().to_dict(), node_config=config)

    @classmethod
    def from_rest(cls, node: rest.Node):
        return cls()