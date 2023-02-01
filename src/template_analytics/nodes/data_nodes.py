from typing import Any, Dict, Tuple

import pandas as pd

from ..helpers import Helper


class DataNodes:
    def merge_data(parameters: Dict[str, Any], data: pd.DataFrame, *args) -> pd.DataFrame:

        data_converted = Helper.convert_types(data)

        if args:
            for additional_data in args:
                data_converted = data_converted.merge(
                    Helper.convert_types(additional_data), on=parameters["id_column"]
                )

        return data_converted

    def split_data(
        data: pd.DataFrame, parameters: Dict[str, Any]
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        data_train = data.sample(
            frac=parameters["train_fraction"], random_state=parameters["random_state"]
        )
        data_test = data.drop(data_train.index)

        X_train = data_train.drop(columns=parameters["target_column"])
        X_test = data_test.drop(columns=parameters["target_column"])
        y_train = data_train[parameters["target_column"]]
        y_test = data_test[parameters["target_column"]]

        return X_train, X_test, y_train, y_test
