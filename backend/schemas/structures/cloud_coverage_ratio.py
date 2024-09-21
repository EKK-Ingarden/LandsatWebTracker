from pydantic import AfterValidator
from typing_extensions import Annotated


def is_between_0_and_1(value: float) -> float:
    assert 0 <= value <= 1, "Value must be between 0 and 1"
    return value


CloudCoverageRatio = Annotated[float, AfterValidator(is_between_0_and_1)]
