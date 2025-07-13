from dataclasses import dataclass
from datetime import time

@dataclass
class SystemParameters:
    state_creation_orders: bool
    shutdown_time: time

    @classmethod
    def avaible_attributes(cls):
        return vars(cls).get("__dataclass_field__")