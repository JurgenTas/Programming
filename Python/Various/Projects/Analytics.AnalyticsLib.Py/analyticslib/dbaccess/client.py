"""
:author: juergen.tas@triodos.com

Connects to a SQL database
"""

import pandas as pd
import sqlalchemy as db
from pandas import DataFrame


class SQLEngine:
    _engine: db.engine
    _con: str

    def __init__(self, conn):
        """
        Returns engine object
        :param conn: connection string
        """
        self._engine = None
        self._conn = conn

    def __enter__(self):
        self._engine = db.create_engine(self._conn)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._engine.dispose()

    def read_to_frame(self, query):
        """
        Read SQL query or database table into a DataFrame
        :param query: SQL query
        :return: DataFrame
        """
        with self._engine.connect() as conn:
            df: DataFrame = pd.read_sql(query, con=conn)
        return df

    def write_frame_to_table(self, df, table, **kwargs):
        """
        Write records stored in a DataFrame to a SQL database
        :param df: DataFrame
        :param table: table name
        """
        with self._engine.connect() as conn:
            df.to_sql(table, con=conn, **kwargs)
