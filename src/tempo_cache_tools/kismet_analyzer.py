from dataclasses import dataclass

from tempo_cache_tools import git

from tempo_cache import cache


@dataclass
# test the tool name and repo name not being the same is okay
class KismetAnalyzerToolInfo(cache.ToolInfo):
    tool_name: str = 'kismet_analyzer'
    repo_name: str = 'kismet-analyzer'
    repo_owner: str = 'trumank'


    def get_file_to_download(self) -> str:
        commit_short_hash = git.get_commit_short_hash_from_tag("trumank/kismet-analyzer", cache.is_online)
        if cache.is_windows():
            return f'{self.repo_name}-{commit_short_hash}-win-x64.zip'
        elif cache.is_linux():
            return f'{self.repo_name}-{commit_short_hash}-linux-x64.zip'
        else:
            raise ValueError('Unsupported OS')

    def get_executable_name(self) -> str:
        if cache.is_windows():
            return f'{self.repo_name}.exe'
        elif cache.is_linux():
            return f'{self.repo_name}'
        else:
            raise ValueError('Unsupported OS')
