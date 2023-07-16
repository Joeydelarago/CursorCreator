from email.mime import image
from typing import List
from pathlib import Path
from PIL import Image
from click import Tuple

import cv2
import os


def parse_video(video_path: Path, frame_skip: int = 1, output_folder = "temp") -> Path:
    video_frames_path = Path(f"./{output_folder}")
    os.makedirs(video_frames_path, exist_ok=True)
    
    write_video_to_images(video_path, video_frames_path, frame_skip)
    
    process_images(video_frames_path)

    return video_frames_path

def process_images(input_folder: Path, size: Tuple = (128, 128)):
    """ Resize images to cursors size and convert them to ico files """
    for filename in os.listdir(input_folder):
        file_path = input_folder.joinpath(filename)

        if not filename.lower().endswith('.png'):
            continue 
        
        try:
            img = Image.open(file_path)
            img.thumbnail(size)
            
            # Add padding to fit the height
            if img.width > img.height:
                crop_size = (img.width - img.height) // 2
                img = img.crop((crop_size, 0, img.width - crop_size, img.height))
            elif img.height > img.width:
                crop_size = (img.height - img.width) // 2
                img = img.crop((0, crop_size, img.width, img.height - crop_size))

            output_path = input_folder.joinpath(filename)
            img = img.convert('RGBA')
            img.save(output_path, format="png") # Save output image

        except Exception as e:
            print(f"Error resizing and converting image {filename}: {str(e)}")

def write_video_to_images(video_path: Path, output_path: Path, frame_skip: int, reverse: bool = False):
    """ Take in video and output folder of jpg images. Optionally only export 1/frame_skip images """
    video = cv2.VideoCapture(video_path)
            
    success, image = video.read()
    count = 0
    while success:
        if not count % frame_skip: # Only export every frame_skip frames
            if reverse:
                cv2.imwrite(os.path.join(output_path, f"frame{1000000 - count:07d}.png"), image)
            else:
                cv2.imwrite(os.path.join(output_path, f"frame{count:07d}.png"), image)

        success,image = video.read()
        count += 1