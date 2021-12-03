"""Node to query API and download dataset.
"""
import logging
import requests
from typing import ByteString

logger = logging.getLogger(__file__)


def query_api(api_reponse: requests.Response) -> ByteString:
    """Query the API and log the response.

    Args:
        api_reponse: APIDataSet, configured to desired package.

    Returns:
        ByteString, the content of the response.
    """
    logger.info(f"Kaggle API response status: {api_reponse.status_code}")

    return api_reponse.content
