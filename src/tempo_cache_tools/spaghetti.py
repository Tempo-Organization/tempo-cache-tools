from dataclasses import dataclass

from tempo_cache import cache


# fix the exe part of the cache with this
@dataclass
class SpaghettiToolInfo(cache.ToolInfo):
    tool_name: str = "spaghetti"
    repo_name: str = "spaghetti"
    repo_owner: str = "bananaturtlesandwich"


    def get_executable_name(self) -> str:
        if cache.is_windows():
            return 'spaghetti.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return 'spaghetti.exe'
        else:
            raise ValueError('unsupported os')
