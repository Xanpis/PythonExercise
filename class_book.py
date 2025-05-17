from dataclasses import dataclass, field

@dataclass
class Book:
    name: str
    genre: str
    status: bool = field(default=True)