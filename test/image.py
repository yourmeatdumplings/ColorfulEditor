from PIL import Image

def fix_image_srgb_profile(file_path):
    img = Image.open(file_path)
    img.save(file_path, icc_profile=None)

fix_image_srgb_profile('../Assets/Texture2D/icon.png')