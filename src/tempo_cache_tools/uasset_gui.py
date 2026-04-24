from dataclasses import dataclass, field
from pathlib import Path

from tempo_cache import cache


@dataclass
class UassetGuiToolInfo(cache.ToolInfo):
    tool_name: str = "uasset_gui"
    repo_name: str = "UAssetGUI"
    repo_owner: str = "atenfyr"
    file_paths: list[Path] = field(default_factory=lambda: [Path('UAssetGUI.exe')])


    def get_executable_name(self) -> str:
        if cache.is_windows():
            return 'UAssetGUI.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return 'UAssetGUI.exe'
        else:
            raise ValueError('unsupported os')
