import sys
sys.path.append(r"C:\Users\dhruv\OneDrive\Desktop\PROJECTS\Project 3.0\BasicSR-master")
sys.path.append(r"C:\Users\dhruv\OneDrive\Desktop\PROJECTS\Project 3.0\Real-ESRGAN\upscaler")
sys.path.append(r"C:\Users\dhruv\OneDrive\Desktop\PROJECTS\Project 3.0\Real-ESRGAN")
import cv2
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, 
                num_grow_ch=32, scale=4)
upsampler = RealESRGANer(scale=4, model_path='RealESRGAN_x4plus.pth', model=model)

img = cv2.imread('C:\\Users\\dhruv\\Downloads\\test_case.jpg', cv2.IMREAD_UNCHANGED)

output, _ = upsampler.enhance(img, outscale=4)

cv2.imwrite(r'C:\Users\dhruv\OneDrive\Desktop\PROJECTS\Project 3.0\Real-ESRGAN\upscaler\Output\output.jpg', output)
