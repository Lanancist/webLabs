
class User:
    def __init__(self, name:str, info: str):
        self.name = name
        self.info = info

    def get_name(self) -> str:
        return self.name

    def get_info(self) -> str:
        return self.info

    def srt_name(self, name :str) -> None:
        if name.strip(): self.name = name
        else: self.name = "Михаил"

    def srt_name(self, info :str) -> None:
        if info.strip():self.info = info
        else: self.info = "Очень, очень хороший мальчик!"