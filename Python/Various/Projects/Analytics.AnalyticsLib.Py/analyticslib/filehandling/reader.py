"""
:author: juergen.tas@triodos.com

Implements (file) reader functionality
"""
from abc import ABC

from pandas import read_csv, DataFrame


class FileReader(ABC):

    def __init__(self, fpath):
        """
        Base reader class.
        :param fpath: file path
        """
        self._fpath = fpath
        self._data = DataFrame()

    def __repr__(self):  # pragma: no cover
        return f"Filename path({self._fpath})"

    @property
    def data(self) -> DataFrame:  # pragma: no cover
        return self._data

    def read(self):
        pass


class CsvFileReader(FileReader):
    """Implements simple pandas csv file reader class."""

    def __init__(self, *args, sep: str = ";"):
        super(CsvFileReader, self).__init__(*args)
        self._sep = sep
        self._data = self.read()

    def read(self):  # pragma: no cover
        return read_csv(self._fpath, sep=self._sep)
