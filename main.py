import Plot, Video
import os


#Magnets
NumLeft = 4
NumRight = 4
val = 4000  #electromagnetic induction 
r = 5       #disk radius
x0 = 20     #coordinate of the 2nd disk


#Video
res = 100    #image resolution
num1 = 64    #number of frames
fps = 10     #fps
folder_name = "output1"
video_name = "result.mp4"

FilePath = f"{folder_name}\\{video_name}"

if __name__ == "__main__":
  if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    
  for j in range(0, num1):
    Plot.DrawImageNxM(res, j, val, r, x0, folder_name, NumLeft, NumRight)
  
  Video.images_to_video(folder_name, FilePath, fps, num1)

  if os.path.exists(FilePath):
      print(f'Rendered Video is lockated in "{FilePath}"')
  else:
      print(f"An error occurred")
