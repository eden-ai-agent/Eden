# Main application entry point
import sys
import logging
from PyQt5.QtWidgets import QApplication
from main import EdenMainWindow


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("eden.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    logging.info("Logging initialized.")


def main():
    setup_logging()
    logging.info("Launching Eden Voice Recorder...")

    app = QApplication(sys.argv)
    window = EdenMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
