from dataclasses import dataclass

from tempo_cache import cache


# test this later (because tool name is not the same as the repo name)
@dataclass
class UassetGuiToolInfo(cache.ToolInfo):
    tool_name: str = "uasset_gui"
    repo_name: str = "UAssetGUI"
    repo_owner: str = "atenfyr"
    file_paths: list[str] = ['UAssetGUI.exe']


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
