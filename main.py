from create_cursor import frames_to_cursor
from parse_video import parse_video

import click
import logging

logger = logging.getLogger()

@click.command()
@click.argument("input_video_path")
def create_cursor(input_video_path: str):
    logger.info("Loading video")
    video_frames_path = parse_video(input_video_path, 7)
    logger.info("Generating Cursor")
    cursor_path = frames_to_cursor(video_frames_path)
    


if __name__ == "__main__":
    create_cursor()