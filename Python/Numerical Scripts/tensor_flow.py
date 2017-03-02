__author__ = 'J Tas'

import tensorflow as tf
import numpy as np
import pandas as pd
import tempfile


FEATURE_COLUMNS = ["leeftijd", "L1", "L2", "L3", "avgVehicleSpeed", "VIJ", "VOJ", "ratio"]
LABEL_COLUMN = 'damaged'


def read(file):
    df = pd.read_csv(file)
    assert isinstance(df.head, object)
    print(df.head(n=5))
    return df


def input_fn(df):
    feature_cols = {k: tf.constant(df[k].values) for k in FEATURE_COLUMNS}
    label = tf.constant(df[LABEL_COLUMN].values)
    return feature_cols, label


def main():
    file = "data_rws.csv"
    data = read(file)
    model_dir = tempfile.mkdtemp()
    m = tf.contrib.learn.DNNLinearCombinedClassifier(
        model_dir=model_dir,
        linear_feature_columns=wide_columns,
        dnn_feature_columns=deep_columns,
        dnn_hidden_units=[100, 50])


if __name__ == "__main__":
    main()
