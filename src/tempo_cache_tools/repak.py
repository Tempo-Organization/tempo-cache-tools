from dataclasses import dataclass

from tempo_cache import cache


@dataclass
class RepakToolInfo(cache.ToolInfo):
    tool_name: str = 'repak'
    repo_name: str = 'repak'
    repo_owner: str = 'trumank'


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return 'repak_cli-x86_64-pc-windows-msvc.zip'
        elif cache.is_linux():
            return 'repak_cli-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('unsupported os')
