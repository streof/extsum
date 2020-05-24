"""Load Picsum photo as byte stream."""

import requests as req
from requests.exceptions import ConnectionError, Timeout
from typing import Iterator


class Load:
    def __init__(self, from_url: str) -> None:
        """Represent photo as URL.

        :param from_url: Photo URL.
        """
        self.url = from_url

    def __iter__(self) -> Iterator:
        """Return photo as byte stream.

        In case of failure the error is shown.
        """
        byte_stream = iter(())
        try:
            response = req.get(self.url, stream=True)
            response.raise_for_status()
        except ConnectionError as conn_err:
            print(f"Connection error: {conn_err}")
        except Timeout as time_err:
            print(f"Timeout error: {time_err}")
        except Exception as err:
            print(f"Error: {err}")
        else:
            byte_stream = response.iter_content()
        finally:
            return byte_stream
