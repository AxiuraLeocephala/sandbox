import hashlib
from typing import Any, Callable, Iterable, TypeVar, Union, List, Literal

md5_obj = hashlib.new("md5")
sha256_obj = hashlib.new("sha256")

class HashTable(dict):
    generate_hash: Callable
    # __instance: None
    # __is_exist = False

    def __init__(self, list_values: Iterable[Union[int, str, tuple, bytes]], algoritm: Literal["md5", "sha256"]):
        # if self.__is_exist: return 

        match algoritm:
            case "md5":
                self.generate_hash = self.generate_md5_hash
            case "sha256":
                self.generate_hash = self.generate_sha256_hash

        super().__init__()
        list_keys: List[str] = list()

        for value in list_values:
            while True:
                hash_value = self.generate_hash(value)
                try:
                    list_keys.index(hash_value)
                except ValueError:
                    break
                else:
                    continue

            list_keys.append(hash_value)

        for k, v in zip(list_keys, list_values):
            self[k] = v

    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #         cls.__is_exist = True
    #     return cls.__instance

    def generate_md5_hash(self, value: Any) -> str:
        md5_obj.update(str(value).encode())
        return md5_obj.hexdigest()
    
    def generate_sha256_hash(self, value: Any) -> str:
        sha256_obj.update(str(value).encode())
        return sha256_obj.hexdigest()

if __name__ == "__main__":
    list_values: List[str] = []
    length_list_value = 10

    for i in range(1, length_list_value + 1):
        list_values.append(f"элемент_{i}")

    hash_table = HashTable(list_values, algoritm="md5")
    for k, v in hash_table.items():
        print(f"{k}: {v}")
    
