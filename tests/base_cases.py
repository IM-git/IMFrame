import requests

from src.enums.global_enums import GlobalErrorMessages
from src.enums.list_of_status_codes import StatusCodes


# Note! M.b. necessary create __init__ and initialize a self.page_response = requests.get(url=url)
class BaseCases:
    """These are the standard parts of the test
    that most tests are used in."""

    @staticmethod
    def check_status_code(url: str,
                          status: int = StatusCodes.OK.value):
        """Checking status code a webpage.
        Get two values:
            url webpage in str format,
            expected status code in int format.
        By default, we wait status code 200 - OK."""
        page_response = requests.get(url=url)
        status_code_webpage = page_response.status_code
        assert status_code_webpage == status,\
            GlobalErrorMessages.WRONG_STATUS_CODE.value





# def check_status_code(url: str,
#                       status: int = StatusCodes.OK.value):
#     def actual_decorator(func):
#         def wrapper():
#             page_response = requests.get(url=url)
#             status_code_webpage = page_response.status_code
#             assert status_code_webpage == status,\
#                 GlobalErrorMessages.WRONG_STATUS_CODE.value
#             func()
#         return wrapper
#     return actual_decorator

