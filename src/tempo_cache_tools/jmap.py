from dataclasses import dataclass

from tempo_cache import cache


@dataclass
class JmapToolInfo(cache.ToolInfo):
    tool_name: str = "jmap"
    repo_name: str = "jmap"
    repo_owner: str = "trumank"


    def get_executable_name(self) -> str:
        if cache.is_windows():
            return 'jmap_dumper.exe'
        elif cache.is_linux():
            return 'jmap_dumper'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if cache.is_windows():
            return 'jmap_dumper-x86_64-pc-windows-msvc.zip'
        elif cache.is_linux():
            return 'jmap_dumper-x86_64-unknown-linux-gnu.tar.xz'
        else:
            raise ValueError('unsupported os')
