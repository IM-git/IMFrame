import requests

from src.enums.global_enums import GlobalErrorMessages
from src.enums.list_of_status_codes import StatusCodes

from tools import Logger


class BaseCases:
    """These are the standard parts of the test
    that most tests are used in."""

    @staticmethod
    def check_status_code(url: str,
                          status: int = StatusCodes.OK.value) -> None:
        """Checking status code a webpage.
        Get two values:
            url webpage in str format,
            expected status code in int format.
        By default, we wait status code 200 - OK."""
        page_response = requests.get(url=url)
        status_code_webpage = page_response.status_code
        Logger().info(f"Checking the page status code: {status_code_webpage}.")
        assert status_code_webpage == status,\
            GlobalErrorMessages.WRONG_STATUS_CODE.value
