from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Sample:
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float