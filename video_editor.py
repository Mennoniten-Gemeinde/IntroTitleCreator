import sys
from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Tk

# Initialize Tkinter root
root = Tk()
root.withdraw()  # We don't need a full GUI, so keep the root window from appearing

# Show an "Open" dialog box and return the path to the selected file
video_path = filedialog.askopenfilename(title="Select video", filetypes=[("Video files", "*.mp4 *.avi *.mkv"), ("All files", "*.*")])

# If a file was selected, proceed with the rest of the script
if video_path:
    title_text = input("Enter the video title: ")

    # Define the size of the image (you might need to adjust this based on the video resolution)
    width, height = 1920, 1080  # Adjust as necessary

    # Create a new image with a white background
    img = Image.new('RGB', (width, height), 'white')

    # Initialize ImageDraw
    draw = ImageDraw.Draw(img)

    # Choose a font and size
    font = ImageFont.load_default()  # Or specify a font path to use different fonts

    # Initialize ImageDraw
    draw = ImageDraw.Draw(img)

    # Print list of attributes of ImageDraw object
    print(dir(draw))

    # Choose a font and size
    font = ImageFont.load_default()

    # Define text size and position
    bbox = draw.textbbox((0,0), title_text, font=font)
    text_width, text_height = bbox[2]-bbox[0], bbox[3]-bbox[1]
    text_x = (width - text_width)/2
    text_y = (height - text_height)/2



    # Add text to the image
    draw.text((text_x, text_y), title_text, fill="black", font=font)






    # Save the image
    img.save('title_image.jpg')


    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Load the image as a clip
    image_clip = ImageClip('title_image.jpg', duration=3)

    # Concatenate image and video
    final_clip = concatenate_videoclips([image_clip, video_clip])

    # Write the result to a file
    final_clip.write_videofile('output_video.mp4', codec="libx264")

# If no file was selected, maybe print a message or exit
else:
    print("No file selected.")
    sys.exit()
