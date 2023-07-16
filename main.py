from create_cursor import frames_to_cursor
from parse_video import parse_video

import click
import logging

logger = logging.getLogger()

@click.command()
@click.argument("output_path")
@click.argument("input_video_path")
# @click.option("-mx", "--max_height", default=255)
# @click.option("-b", "--backplate", is_flag=True, default=False)
def create_cursor(output_path: str, input_video_path: str):
    print("a")
    logger.info("Loading video")
    video_frames_path = parse_video(input_video_path)
    logger.info("Generating Cursor")
    print("b")
    frames_to_cursor(video_frames_path)


if __name__ == "__main__":
    create_cursor()