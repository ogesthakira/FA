import os
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QPushButton, QTreeWidget, QTreeWidgetItem, QFileDialog, QLabel
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon, QGuiApplication
from core import process_folder
from utils import human_readable_size

class FolderSizeAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folder Size Analyzer")
        self.setMinimumSize(QSize(750, 500))
        
        # Dark theme styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2D2D2D;
            }
            QWidget {
                color: #E0E0E0;
                background-color: #2D2D2D;
                selection-background-color: #3D3D3D;
                selection-color: #FFFFFF;
            }
            QPushButton {
                background-color: #3D3D3D;
                border: 1px solid #4D4D4D;
                border-radius: 4px;
                padding: 5px 10px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #4D4D4D;
            }
            QPushButton:pressed {
                background-color: #2D2D2D;
            }
            QTreeWidget {
                background-color: #252525;
                border: 1px solid #3D3D3D;
                alternate-background-color: #2D2D2D;
                font-family: "Arial";
                font-size: 10pt;
            }
            QHeaderView::section {
                background-color: #3D3D3D;
                padding: 5px;
                border: 1px solid #4D4D4D;
            }
        """)
        
        # Set application icon (optional)
        try:
            # Note: This will not work without a 'folder_icon.png' file
            self.setWindowIcon(QIcon("folder_icon.png"))
        except:
            pass

        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        
        # Top panel with folder selection
        top_panel = QHBoxLayout()
        
        self.folder_label = QLabel("No folder selected")
        self.folder_label.setFont(QFont("Arial", 10))
        
        select_button = QPushButton("Select Folder")
        select_button.setFixedWidth(120)
        select_button.clicked.connect(self.select_folder)
        
        top_panel.addWidget(self.folder_label)
        top_panel.addStretch()
        top_panel.addWidget(select_button)
        
        # Tree widget for displaying folder sizes
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Folder", "Size"])
        self.tree_widget.setColumnWidth(0, 400)
        self.tree_widget.setSortingEnabled(True)
        self.tree_widget.sortByColumn(1, Qt.SortOrder.DescendingOrder)
        
        # Status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Ready")
        
        # Add widgets to main layout
        main_layout.addLayout(top_panel)
        main_layout.addWidget(self.tree_widget)
        
    def select_folder(self):
        """Open folder dialog and analyze selected folder."""
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder to Analyze",
            str(Path.home()),
            QFileDialog.Option.ShowDirsOnly
        )
        
        if folder_path:
            self.folder_label.setText(f"Selected: {folder_path}")
            self.analyze_folder(folder_path)
    
    def analyze_folder(self, folder_path: str):
        """Analyze folder and populate tree widget with results."""
        self.tree_widget.clear()
        self.status_bar.showMessage("Analyzing folder...")
        QGuiApplication.processEvents()
        
        try:
            root_item = QTreeWidgetItem(self.tree_widget)
            root_item.setText(0, os.path.basename(folder_path))
            
            total_size = process_folder(folder_path, root_item)
            root_item.setText(1, human_readable_size(total_size))
            
            self.tree_widget.expandItem(root_item)
            self.status_bar.showMessage(f"Analysis complete. Total size: {human_readable_size(total_size)}")
        except Exception as e:
            self.status_bar.showMessage(f"Error: {str(e)}")
