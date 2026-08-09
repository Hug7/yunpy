from typing import Dict, Any


class Table:

    def to_dict(self) -> Dict[str, Any]:
        pass

    @staticmethod
    def empty_dict() -> Dict[str, Any]:
        pass

    @staticmethod
    def table_name() -> str:
        pass
