from pathlib import Path

class DirectoryUtils:
    
    @staticmethod
    def scan_directory(path, search_pattern = "*"):
        result = list(Path(path).rglob(search_pattern))
        return result
    