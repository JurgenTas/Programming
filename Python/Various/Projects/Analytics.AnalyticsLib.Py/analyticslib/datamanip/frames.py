"""
:author: juergen.tas@triodos.com

Utility functions for Pandas DataFrames
"""
import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class FrameContainer:
    """Simple container class for Pandas DataFrame"""

    def __init__(self, df: pd.DataFrame, **id_params):
        """
        Class to store Pandas DataFrame with id parameters.
        :param df: Pandas DataFrame
        :param id_params: id parameters
        """
        self._data = df
        self._id_params = id_params

    def __len__(self):  # pragma: no cover
        return len(self._data.index)

    @property
    def data(self) -> pd.DataFrame:  # pragma: no cover
        return self._data

    @property
    def id_params(self) -> dict:  # pragma: no cover
        return self._id_params


def sort_frame(df: pd.DataFrame, by: list, asc: bool = True,
               drop: bool = True) -> pd.DataFrame:
    """
    Sort DataFrame column-wise and update index.
    :param df: Original DataFrame
    :param by: name or list of names to sort by
    :param asc: sort ascending vs. descending
    :param drop:
    :return: DataFrame with sorted values
    """
    return df.sort_values(by, ascending=asc).reset_index(drop=drop)


def trim_white_spaces_frame(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pre-process DataFrame; i.e. trim data of unnecessary whitespaces.
    :param df: original DataFrame
    :return: updated frame
    """
    if len(df.index) != 0:
        df.columns = df.columns.str.strip()
        return _trim_frame(df)  # Strip whitespaces
    return df


def _trim_frame(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trim whitespace/tabs/newline from ends of each value across all
    fields in DataFrame.
    :param df: original DataFrame
    :return: updated DataFrame
    """
    return df.applymap(lambda x: ' '.join(x.split()) if type(x) is str else x)


def merge_frames(frames, ignore_index=True) -> pd.DataFrame:
    """
    Merges list of DataFrames to one total DataFrame.
    :param frames: list of DataFrame
    :param ignore_index: ignore index indicator
    :return: merged DataFrame
    """
    try:
        if not all(isinstance(frame, pd.DataFrame) for frame in frames):
            raise TypeError("invalid type encountered!")
    except TypeError as err:
        msg = "Error merging frames: %s" % err
        logger.error(msg)
        raise
    else:
        return pd.concat(frames, ignore_index=ignore_index)


def join_frames(df_left: pd.DataFrame, df_right: pd.DataFrame, cols,
                how="left") -> pd.DataFrame:
    """
    Join left DataFrame on right DataFrame using cols and how.
    :param df_left: left DataFrame
    :param df_right: right DataFrame
    :param cols: columns (names) to join on
    :param how: one of 'left', 'right', 'outer', 'inner'
    :return: resulting DataFrame of join operation
    """
    try:
        for col in cols:
            if col not in df_left.columns or col not in df_right.columns:
                raise ValueError("Invalid column name: ", col)
    except ValueError as err:
        msg = "Error joining frames: %s" % err
        logger.error(msg)
        raise
    else:
        return pd.merge(df_left, df_right, how, on=cols)


def dates_as_index_frame(df, col="Date", date_format="%Y-%m-%d"):
    """Private helper function to add date column of DataFrame as index"""
    df.index = pd.to_datetime(df[col], format=date_format)
    df = df.drop(col, 1)  # drop original date column
    df = df.dropna()
    return df


def select_rows_in_frame(df, **conditions):
    """
    Select rows in a Pandas DataFrame by conditions on (multiple)
    equality columns.
    :param df: original Pandas DataFrame
    :param conditions: set of equality conditions
    :return: DataFrame with selected rows
    """
    rows_filter = pd.Series(np.ones(df.shape[0], dtype=bool))
    for k, v in conditions.items():
        rows_filter = ((df[k] == v) & rows_filter)
    return df[rows_filter]  # filter rows


def replace_values_in_frame(df, to_replace_in_column, value, **conditions):
    """
    Replace value(s) in a column of a Pandas Dataframe based on (multiple)
    column value equality conditions.
    :param df: original Pandas DataFrame
    :param to_replace_in_column: values in column to_replace
    :param value: value to replace any values matching conditions with
    :param conditions: set of equality conditions
    :return: updated Pandas DataFrame
    """
    rows_filter = pd.Series(np.ones(df.shape[0], dtype=bool))
    for k, v in conditions.items():
        rows_filter = ((df[k] == v) & rows_filter)
    df.loc[rows_filter, to_replace_in_column] = value  # replace value(s)
    return df
