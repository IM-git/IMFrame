from tools.exceptions.base_exception import BaseExceptions


class InvalidCondition(BaseExceptions):
    """We use this class for indicate invalid condition exception.
    This type answer is not used in the condition."""
    pass


class InvalidConditionInTest(BaseExceptions):
    """We use this class for indicate invalid condition exception
    in the tests. This type answer is not used in the condition.
    Appears when 'browser' value in tests entered not correctly
    or missing in the test/s."""
    pass
