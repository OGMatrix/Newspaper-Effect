from moviepy.editor import VideoClip, ImageSequenceClip
import os

def createVideo(duration: float, output: str):
    # Directory containing your image files
    image_directory = "./cache/cropped"

    # Get a list of image file names in the directory
    image_files = sorted([os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('.jpg', '.png', '.jpeg'))])

    # Define the duration (in seconds) for each image
    image_duration = duration

    # Load the images as a list of clips
    image_clips = [ImageSequenceClip([image_file], durations=[image_duration]) for image_file in image_files]

    # Concatenate the image clips into a single video clip
    video_clip = VideoClip(lambda t: image_clips[min(int(t / image_duration), len(image_clips) - 1)].get_frame(t), duration=len(image_clips) * image_duration)

    # Set the output filename
    output_filename = f"./output/{output}.mp4"

    # Write the video clip to an MP4 file
    video_clip.write_videofile(output_filename, codec="libx264", fps=24)  # You can adjust codec and fps as needed