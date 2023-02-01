from kedro.pipeline import Pipeline, node, pipeline

from .nodes import DataNodes, MlNodes


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=DataNodes.merge_data,
                inputs=["parameters", "application_record", "credit_record"],
                outputs="merged_record",
                name="merged",
            ),
            node(
                func=DataNodes.split_data,
                inputs=["merged_record", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split",
            ),
            node(
                func=MlNodes.random_forest_classifier,
                inputs=["X_train", "y_train", "parameters"],
                outputs="model",
                name="ml_model",
            ),
            node(
                func=MlNodes.make_predictions,
                inputs=["model", "X_test"],
                outputs="y_pred",
                name="make_predictions",
            ),
            node(
                func=MlNodes.report_accuracy,
                inputs=["y_pred", "y_test"],
                outputs="metrics",
                name="report_accuracy",
            ),
        ]
    )
