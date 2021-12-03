"""API Query pipeline.
"""

from kedro.pipeline import Pipeline, node

from .nodes import query_api


def create_pipeline(**kwargs) -> Pipeline:
    """Create the API query pipeline.

    Args:
        **kwargs: keywords.

    Returns:
        Pipeline.
    """
    return Pipeline([node(query_api, "kaggle_api", "kaggle_content", name="query_api")])
