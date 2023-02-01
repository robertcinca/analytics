# standard library

from typing import Any, Dict

import pandas as pd
import pytest
from template_analytics.nodes import MlNodes


class TestPipeline:
    def prediction(value):
        return False if 0 < value > 1 else True

    @pytest.mark.parametrize(
        "data_row",
        [
            {
                "ID": {0: 0},
                "CODE_GENDER": {0: 1},
                "FLAG_OWN_CAR": {0: 1},
                "FLAG_OWN_REALTY": {0: 1},
                "CNT_CHILDREN": {0: 0},
                "AMT_INCOME_TOTAL": {0: 577},
                "NAME_INCOME_TYPE": {0: 4},
                "NAME_EDUCATION_TYPE": {0: 1},
                "NAME_FAMILY_STATUS": {0: 0},
                "NAME_HOUSING_TYPE": {0: 4},
                "DAYS_BIRTH": {0: 2002},
                "DAYS_EMPLOYED": {0: 4963},
                "FLAG_MOBIL": {0: 0},
                "FLAG_WORK_PHONE": {0: 1},
                "FLAG_PHONE": {0: 0},
                "FLAG_EMAIL": {0: 0},
                "OCCUPATION_TYPE": {0: 0},
                "CNT_FAM_MEMBERS": {0: 4},
                "MONTHS_BALANCE": {0: 60},
                "STATUS": {0: 7},
            }
        ],
    )
    def test_pipeline_one(self, data_row: Dict[str, Any]) -> None:
        sample_row = pd.DataFrame.from_dict(data_row)

        X_test = sample_row.drop(columns="CODE_GENDER")
        y_test = sample_row["CODE_GENDER"]

        model = pd.read_pickle("data/06_models/model.pkl")

        assert TestPipeline.prediction(MlNodes.make_predictions(model, X_test)) is True

        # Expecting the prediction to be correct for this particular sample
        assert TestPipeline.prediction(MlNodes.make_predictions(model, X_test)) == y_test[0]
