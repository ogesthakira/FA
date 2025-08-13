import os
from PyQt6.QtWidgets import QTreeWidgetItem
from utils import human_readable_size

def process_folder(folder_path: str, parent_item: QTreeWidgetItem) -> int:
    """Recursively process folder and calculate sizes."""
    total_size = 0
    
    try:
        with os.scandir(folder_path) as it:
            for entry in it:
                if entry.is_dir(follow_symlinks=False):
                    try:
                        child_item = QTreeWidgetItem(parent_item)
                        child_item.setText(0, entry.name)
                        
                        dir_size = process_folder(entry.path, child_item)
                        child_item.setText(1, human_readable_size(dir_size))
                        total_size += dir_size
                    except PermissionError:
                        continue
                elif entry.is_file(follow_symlinks=False):
                    try:
                        total_size += entry.stat().st_size
                    except PermissionError:
                        continue
    except PermissionError:
        pass
    
    return total_size
