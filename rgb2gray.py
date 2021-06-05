from PIL import Image
import os

im_dir = 'C:/Users/hkzhang/Desktop/02_TGRS/figures_jpg_eps/Bai.png'
save_dir = 'C:/Users/hkzhang/Desktop/02_TGRS/figures_jpg_eps/Bai.jpg'

im = Image.open(im_dir).convert('L')
im.save(save_dir)