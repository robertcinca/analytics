import numpy as np
import pandas as pd


class Helper:
    @staticmethod
    def convert_types(data: pd.DataFrame):
        """
        Convert data types to numeric and categorical columns
        """
        # Replace bool with numeric
        data.replace({False: 0.0, True: 1.0}, inplace=True)

        # Get a list of columns that are numeric and objects
        numeric_list = data.select_dtypes(include=[np.number]).columns
        object_list = data.select_dtypes(object).columns

        # convert numeric types
        data[numeric_list] = data[numeric_list].astype(np.float32)

        # convert objects
        for column in object_list:
            data[column] = pd.Categorical(data[column])
            data[column] = data[column].cat.codes

        return data
