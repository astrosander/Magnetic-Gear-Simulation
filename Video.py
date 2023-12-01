import cv2
import os

def images_to_video(image_folder, video_name, fps, frame_number):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images=[]

    images = [f"{i}.png" for i in range(frame_number)]


    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

