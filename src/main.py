# PyQt5 GUI controller
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QSlider, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys


class EdenMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eden Voice Recorder")
        self.setFixedSize(600, 500)
        self.setStyleSheet("background-color: #eaeff4;")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Title / Mic Icon Placeholder
        title = QLabel("Voice Recorder")
        title.setFont(QFont("Arial", 20))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Timer display
        self.timer_label = QLabel("00:00")
        self.timer_label.setFont(QFont("Courier", 24))
        self.timer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_label)

        # Waveform Placeholder
        waveform = QFrame()
        waveform.setFixedHeight(100)
        waveform.setStyleSheet("background-color: #cdd7e1; border-radius: 10px;")
        layout.addWidget(waveform)

        # Buttons Row
        button_row = QHBoxLayout()
        for label in ["Start", "Pause", "Resume", "Stop"]:
            btn = QPushButton(label)
            btn.setFixedSize(80, 40)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #dce4ec;
                    border: none;
                    border-radius: 10px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #c0cbd7;
                }
            """)
            button_row.addWidget(btn)
        layout.addLayout(button_row)

        # Slider + Options Row
        slider_row = QHBoxLayout()
        slider = QSlider(Qt.Horizontal)
        slider.setStyleSheet("QSlider::groove:horizontal { background: #d0dae5; height: 8px; }")
        slider_row.addWidget(slider)
        layout.addLayout(slider_row)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EdenMainWindow()
    window.show()
    sys.exit(app.exec_())
