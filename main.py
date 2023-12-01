import Plot, Video
import os

#Variables
res = 20    #image resolution
num1 = 20   #number of frames
val = 4000  #electromagnetic induction 
r = 5       #disk radius
x0 = 20     #coordinate of the 2nd disk
fps = 10    #fps

folder_name = "output"
video_name = "result.mp4"

FilePath = f"{folder_name}\\{video_name}"


if __name__ == "__main__":
  Plot.DrawImage(res, num1, val, r, x0, folder_name)

  print("Adding to video..")
  Video.images_to_video(folder_name, FilePath, fps, num1)

  if os.path.exists(FilePath):
      print(f'Rendered Video is lockated in "{FilePath}"')
  else:
      print(f"An error occurred")
