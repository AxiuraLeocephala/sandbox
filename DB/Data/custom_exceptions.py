from typing import Optional

class FallingAsleepError(Exception):
    def __init__(self, msg: Optional[str] = None) -> None:
        super().__init__()
        self.msg = msg