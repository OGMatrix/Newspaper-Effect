from moviepy.editor import VideoClip, ImageSequenceClip
import os

def createVideo(duration: float, output: str):
    image_directory = "./cache/cropped"

    image_files = sorted([os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('.jpg', '.png', '.jpeg'))])

    image_duration = duration

    image_clips = [ImageSequenceClip([image_file], durations=[image_duration]) for image_file in image_files]

    video_clip = VideoClip(lambda t: image_clips[min(int(t / image_duration), len(image_clips) - 1)].get_frame(t), duration=len(image_clips) * image_duration)

    output_filename = f"./output/{output}.mp4"

    video_clip.write_videofile(output_filename, codec="libx264", fps=24)  # You can adjust codec and fps as needed