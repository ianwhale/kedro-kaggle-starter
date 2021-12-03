"""SafeAPIDataSet class definiiton.
"""
from typing import Any, Dict, Iterable, List, Union
from requests.auth import AuthBase

from kedro.extras.datasets.api import APIDataSet


class AuthorizableAPIDataSet(APIDataSet):
    """APIDataSet that allows the ``auth`` keyword argument to be a list."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        url: str,
        method: str = "GET",
        data: Any = None,
        params: Dict[str, Any] = None,
        headers: Dict[str, Any] = None,
        auth: Union[Iterable[str], AuthBase] = None,
        json: Union[List, Dict[str, Any]] = None,
        timeout: int = 60,
        credentials: Union[Iterable[str], AuthBase] = None,
    ) -> None:
        """Creates a new instance of ``APIDataSet`` to fetch data from an API endpoint.

        Args:
            url: The API URL endpoint.
            method: The Method of the request, GET, POST, PUT, DELETE, HEAD, etc...
            data: The request payload, used for POST, PUT, etc requests
                https://requests.readthedocs.io/en/master/user/quickstart/#more-complicated-post-requests
            params: The url parameters of the API.
                https://requests.readthedocs.io/en/master/user/quickstart/#passing-parameters-in-urls
            headers: The HTTP headers.
                https://requests.readthedocs.io/en/master/user/quickstart/#custom-headers
            auth: Anything ``requests`` accepts. Normally it's either ``('login', 'password')``,
                or ``AuthBase``, ``HTTPBasicAuth`` instance for more complex cases.
                Casts any iterable to a tuple.
            json: The request payload, used for POST, PUT, etc requests, passed in
                to the json kwarg in the requests object.
                https://requests.readthedocs.io/en/master/user/quickstart/#more-complicated-post-requests
            timeout: The wait time in seconds for a response, defaults to 1 minute.
                https://requests.readthedocs.io/en/master/user/quickstart/#timeouts
            credentials: Anything ``requests`` accepts. Normally it's either ``('login', 'password')``,
                or ``AuthBase``, ``HTTPBasicAuth`` instance for more complex cases.
                Casts any iterable to a tuple.

        Raises:
            ValueError: if both ``credentials`` and ``auth`` are specified.
        """
        if credentials is not None and auth is not None:
            raise ValueError("Cannot specify both auth and credentials.")

        auth = credentials or auth

        if isinstance(auth, Iterable):
            auth = tuple(auth)

        super().__init__(
            url=url,
            method=method,
            data=data,
            params=params,
            headers=headers,
            auth=auth,
            json=json,
            timeout=timeout,
        )
