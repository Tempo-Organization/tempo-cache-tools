from dataclasses import dataclass

from tempo_cache import cache


@dataclass
class PatternsleuthToolInfo(cache.ToolInfo):
    tool_name: str = "FModel"
    repo_name: str = "FModel"
    repo_owner: str = "4sval"


    def get_executable_name(self) -> str:
        if cache.is_windows():
            return 'FModel.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return 'Fmodel.zip'
        else:
            raise ValueError('unsupported os')
