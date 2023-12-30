from dataclasses import dataclass, field
from typing import Optional


@dataclass
class State:
    tiles: list[int] = field(default_factory=lambda: [0 for _ in range(50)])
    hand: Optional[int] = None
    output: list[int] = field(default_factory=list) 
