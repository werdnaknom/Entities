from pathlib import Path, WindowsPath, PosixPath
from dataclasses import dataclass
import platform
import os


@dataclass
class PathTranslator:
    path_name: str
    path_str: str
    system: str = platform.system()

    def to_windows(self):
        return self.path_str

    @property
    def path(self) -> Path:
        if (self.system == "Linux") & (self.path_str.find("//") == 0):
            # //npo needs to be changed to /npo
            linux_str = self.path_str[1:]
            path = Path(linux_str)
        else:
            path = Path(self.path_str)

        assert path.exists()
        return path

    def to_dict(self):
        return {self.path_name: self.to_windows()}