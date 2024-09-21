from pydantic import AfterValidator
from typing_extensions import Annotated


def between_0_n_1(value: float) -> float:
    assert 0 <= value <= 1, "Value must be between 0 and 1"
    return value


CloudCoverageRatio = Annotated[float, AfterValidator(between_0_n_1)]
