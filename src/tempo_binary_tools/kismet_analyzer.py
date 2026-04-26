from dataclasses import dataclass

from tempo_binary_tools import git

from tempo_binary_tool_manager import manager


@dataclass
class KismetAnalyzerToolInfo(manager.ToolInfo):
    tool_name: str = 'kismet_analyzer'
    repo_name: str = 'kismet-analyzer'
    repo_owner: str = 'trumank'


    def get_file_to_download(self) -> str:
        commit_short_hash = git.get_commit_short_hash_from_tag("trumank/kismet-analyzer", True)
        if manager.is_windows():
            return f'{self.repo_name}-{commit_short_hash}-win-x64.zip'
        elif manager.is_linux():
            return f'{self.repo_name}-{commit_short_hash}-linux-x64.zip'
        else:
            raise ValueError('Unsupported OS')

    def get_executable_name(self) -> str:
        if manager.is_windows():
            return f'{self.repo_name}.exe'
        elif manager.is_linux():
            return f'{self.repo_name}'
        else:
            raise ValueError('Unsupported OS')
