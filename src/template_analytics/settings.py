"""
Creates and stores ML experiments
"""

from pathlib import Path

from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore

SESSION_STORE_CLASS = SQLiteStore
SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / "data")}
