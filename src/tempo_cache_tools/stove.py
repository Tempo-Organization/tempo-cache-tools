from dataclasses import dataclass

from tempo_cache import cache


# fix the exe part of the cache with this
@dataclass
class StoveToolInfo(cache.ToolInfo):
    tool_name: str = "stove"
    repo_name: str = "stove"
    repo_owner: str = "bananaturtlesandwich"


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return f'{self.tool_name}.exe'
        elif cache.is_linux():
            return f'{self.tool_name}-linux'
        else:
            raise ValueError('Unsupported OS')


    def get_executable_name(self) -> str:
        if cache.is_windows():
            return f'{self.tool_name}.exe'
        elif cache.is_linux():
            return f'{self.tool_name}-linux'
        else:
            raise ValueError('Unsupported OS')
