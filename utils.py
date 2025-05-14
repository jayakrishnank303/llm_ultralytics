import os

def validate_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError("Image file not found.")
    if not path.lower().endswith(('.jpg', '.jpeg', '.png')):
        raise ValueError("Only .jpg, .jpeg, and .png files are supported.")
    return path
