from dataclasses import dataclass

from tempo_binary_tool_manager import manager


# test this later (because tool name is not the same as the repo name)
@dataclass
class UmodelToolInfo(manager.ToolInfo):
    tool_name: str = "umodel"
    repo_name: str = "UEViewer"
    repo_owner: str = "Mythical-Github"


    def get_executable_name(self) -> str:
        if manager.is_windows():
            return 'umodel_64.exe'
        else:
            raise ValueError('unsupported os')


    def get_file_to_download(self) -> str:
        if manager.is_windows():
            return 'umodel_win32.zip'
        else:
            raise ValueError('unsupported os')
