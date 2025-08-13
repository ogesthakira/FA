import sys
from PyQt6.QtWidgets import QApplication
from ui import FolderSizeAnalyzer

def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    analyzer = FolderSizeAnalyzer()
    analyzer.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
