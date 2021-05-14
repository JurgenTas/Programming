"""
:author: juergen.tas@triodos.com

Implements (file) writer functionality
"""
from abc import ABC

import pandas as pd


class FileWriter(ABC):

    def __init__(self, fpath, frame):
        """
        Base writer class.
        :param fpath: file path
        """
        self._fpath = fpath
        self._data = frame

    def __repr__(self):  # pragma: no cover
        return f"Filename path({self._fpath})"

    @property
    def data(self) -> pd.DataFrame:  # pragma: no cover
        return self._data

    def write(self):
        pass


class CsvFileWriter(FileWriter):
    """Implements simple pandas csv file writer class."""

    def __init__(self, *args, sep: str = ";"):
        super(CsvFileWriter, self).__init__(*args)
        self._sep = sep

    def write(self):  # pragma: no cover
        self._data.to_csv(self._fpath, sep=self._sep)
