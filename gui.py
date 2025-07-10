import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QFileDialog, QHBoxLayout
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
import cv2
import numpy as np

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(r"C:\Users\dhruv\OneDrive\Desktop\PROJECTS\Project 3.0\Real-ESR\BasicSR-master"))
from basicsr.archs.rrdbnet_arch import RRDBNet
sys.path.append(os.path.abspath(r"C:\Users\dhruv\OneDrive\Desktop\PROJECTS\Project 3.0\Real-ESRGAN"))
from realesrgan import RealESRGANer


class UpscaleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-ESRGAN Image Upscaler")
        self.setGeometry(100, 100, 800, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        btn_layout = QHBoxLayout()
        self.open_btn = QPushButton("Select Image")
        self.upscale_btn = QPushButton("Upscale Image")
        self.upscale_btn.setEnabled(False)
        btn_layout.addWidget(self.open_btn)
        btn_layout.addWidget(self.upscale_btn)

        self.layout.addLayout(btn_layout)

        img_layout = QHBoxLayout()
        self.input_label = QLabel("Original Image")
        self.output_label = QLabel("Upscaled Image")
        self.input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_layout.addWidget(self.input_label)
        img_layout.addWidget(self.output_label)

        self.layout.addLayout(img_layout)

        self.open_btn.clicked.connect(self.load_image)
        self.upscale_btn.clicked.connect(self.upscale_image)

        self.img = None

        
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(base_path, 'RealESRGAN_x4plus.pth')

        self.model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
        self.upsampler = RealESRGANer(scale=4, model_path=model_path, model=self.model)

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path:
            self.img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            pix = self.cv_to_pixmap(self.img)
            self.input_label.setPixmap(pix.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
            self.upscale_btn.setEnabled(True)

    def upscale_image(self):
        if self.img is not None:
            try:
                output, _ = self.upsampler.enhance(self.img, outscale=4)
                pix = self.cv_to_pixmap(output)
                self.output_label.setPixmap(pix.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

                output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Output')
                os.makedirs(output_folder, exist_ok=True)
                cv2.imwrite(os.path.join(output_folder, 'upscaled_output.jpg'), output)
            except Exception as e:
                print(f"Upscaling error: {e}")

    def cv_to_pixmap(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = img.shape
        bytes_per_line = ch * w
        qimg = QImage(img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qimg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UpscaleApp()
    window.show()
    sys.exit(app.exec())
