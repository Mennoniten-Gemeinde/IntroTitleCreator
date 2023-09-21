import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk
from PIL import ImageFont

# Initialize Tkinter root
root = Tk()
root.withdraw()  # We don't need a full GUI, so keep the root window from appearing

# Show an "Open" dialog box and return the path to the selected file
video_path = filedialog.askopenfilename(title="Select video", filetypes=[("Video files", "*.mp4 *.avi *.mkv"), ("All files", "*.*")])

# If a file was selected, proceed with the rest of the script
if video_path:
    title_text = input("Enter the video title: ")

    title_image_name = f"{title_text}_title_image.jpg"
    output_video_name = f"{title_text}_output_video.mp4"

    # Load the static background image
    background_image_path = "background.jpg"  # Replace with the path to your background image
    img = Image.open(background_image_path)

    # Initialize ImageDraw
    draw = ImageDraw.Draw(img)

    # Choose a font and size (large size like 200)
    font_path = "arial.ttf"  # Replace with the path to your .ttf file
    font_size = 200  # You can adjust the size here
    font = ImageFont.truetype(font_path, font_size)

    # Define text size and position
    bbox = draw.textbbox((0, 0), title_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    text_x = (img.width - text_width) / 2
    text_y = (img.height - text_height) / 2 

    # Add text to the image
    draw.text((text_x, text_y), title_text, fill="black", font=font)

    # Save the modified image
    img.save(title_image_name)

    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the modified image as a clip
    image_clip = ImageClip(title_image_name, duration=3)

    # Concatenate image and video
    final_clip = concatenate_videoclips([image_clip, video_clip])

     # Write the result to a file
    try:
        final_clip.write_videofile(output_video_name, codec="mpeg4")
    except Exception as e:
        print(f"An error occurred: {e}")

# If no file was selected, maybe print a message or exit
else:
    print("No file selected.")
    sys.exit()
