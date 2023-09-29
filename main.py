import os
from util.renameFiles import renameFiles
from util.prepareImages import prepareImages
from util.createVideo import createVideo
import prompt

print("Enter the Keyword:")
keyword = prompt.string()
print("")

print("Enter the Cropped Offset:")
offset = prompt.integer()
print("")

print("Enter the Image Duration:")
duration = prompt.string()
print("")

print("Enter the Output file (example: output, if you want file to be output.mp4):")
output = prompt.string()
print("")


success = renameFiles()
print("Renaimed all files to fit!", end='\r')

if success:
    for (dirpath, dirnames, filenames) in os.walk("images"):
        for file in filenames:
            if file.endswith(".png"):
                print("Processing " + file + "                       ", end='\r')
                prepareImages(keyword, file, offset)
    
    print("Creating the final video...", end='\r')
    createVideo(float(duration), output)
    for (dirpath, dirnames, filenames) in os.walk("cache/cropped"):
        for file in filenames:
            if file.endswith(".png"):
                os.remove(dirpath + '/' + file)
    print("Finished!")