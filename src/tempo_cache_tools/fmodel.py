from dataclasses import dataclass

from tempo_cache import cache


@dataclass
class PatternsleuthToolInfo(cache.ToolInfo):
    tool_name: str = "FModel"
    repo_name: str = "FModel"
    repo_owner: str = "4sval"


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return f'{self.tool_name}-x86_64-pc-windows-msvc.zip'
        elif cache.is_linux():
            return f'{self.tool_name}-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('Unsupported OS')


    def get_executable_name(self) -> str:
        if cache.is_windows():
            return f'{self.tool_name}.exe'
        elif cache.is_linux():
            return f'{self.tool_name}'
        else:
            raise ValueError('Unsupported OS')
