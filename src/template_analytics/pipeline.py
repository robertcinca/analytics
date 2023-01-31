"""
This is a boilerplate pipeline
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

# from .nodes import make_predictions, merge_data, report_accuracy, split_data,
from .nodes import DataNodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=DataNodes.merge_data,
                inputs=["application_record_csv", "credit_record_csv"],
                outputs="merged_record",
                name="merged",
            ),
            node(
                func=DataNodes.convert_types,
                inputs="merged_record",
                outputs="converted_record",
                name="converted",
            ),
            node(
                func=DataNodes.split_data,
                inputs=["example_iris_data", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split",
            ),
            node(
                func=DataNodes.make_predictions,
                inputs=["X_train", "X_test", "y_train"],
                outputs="y_pred",
                name="make_predictions",
            ),
            node(
                func=DataNodes.report_accuracy,
                inputs=["y_pred", "y_test"],
                outputs=None,
                name="report_accuracy",
            ),
        ]
    )
