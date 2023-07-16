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
            if img.size[1] < 128:
                new_img = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
                new_img.paste(img, ((128 - size[0]) // 2, (128 - size[1]) // 2))
                img = new_img

            output_path = input_folder.joinpath(filename)
            # img.convert('BGRA')
            img.save(output_path, format="png") # Save output image

        except Exception as e:
            print(f"Error resizing and converting image {filename}: {str(e)}")

def write_video_to_images(video_path: Path, output_path: Path, frame_skip: int):
    """ Take in video and output folder of jpg images. Optionally only export 1/frame_skip images """
    video = cv2.VideoCapture(video_path)
            
    success, image = video.read()
    count = 0
    while success and count < 100:
        if not count % frame_skip: # Only export every frame_skip frames
            cv2.imwrite(os.path.join(output_path, f"frame{count}.png"), image)
            success,image = video.read()
            
        count += 1
        
parse_video("MORBIUS.mp4")