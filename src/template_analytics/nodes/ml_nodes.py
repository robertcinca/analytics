import logging
from typing import Any, Dict

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV


class MlNodes:
    def random_forest_classifier(
        X_train: pd.DataFrame, y_train: pd.Series, parameters: Dict[str, Any]
    ) -> RandomForestClassifier:
        rf = RandomForestClassifier()

        random_grid = {
            "n_estimators": parameters["n_estimators"],
            "max_features": parameters["max_features"],
            "max_depth": parameters["max_depth"],
            "min_samples_split": parameters["min_samples_split"],
            "min_samples_leaf": parameters["min_samples_leaf"],
        }

        rf_random = RandomizedSearchCV(
            estimator=rf,
            param_distributions=random_grid,
            n_iter=10,
            cv=4,
            verbose=5,
            random_state=parameters["random_state"],
            n_jobs=-1,
        )

        rf_random.fit(X_train, y_train)

        return rf_random.best_estimator_

    def make_predictions(model: RandomForestClassifier, X_test: pd.DataFrame) -> pd.Series:

        return model.predict(X_test)

    def report_accuracy(y_pred: pd.Series, y_test: pd.Series):
        accuracy = (y_pred == y_test).sum() / len(y_test)

        logger = logging.getLogger(__name__)
        logger.info("Model has accuracy of %.3f on test data.", accuracy)

        return {"accuracy": accuracy}
