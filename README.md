# Newspaper Effect
Wondering how youtube channels do this cool effect? Do it for free with this repository in seconds!

## Examples
Created using the example images, `Keyword`: **Area 51**, Cropped `Cropped Offset`: **200** and `Image Duration` set to **0.3**.

https://github.com/OGMatrix/Newspaper-Effect/assets/49974161/5e01d4a1-9d84-4621-acee-28fde1c90dc5

## How it works


- Loops through each images and transcribes your news posts via pytesseract
- After transcribing it searches for your entered keywords and creates a cropped image of it centered (if the title has enough height to the top of the page)
- Using moviepy it creates the video with a delay of 0.3 seconds between each image

## Installation
Install the project using git clone
```
$ git clone https://github.com/OGMatrix/Newspaper-Effect.git
```

After that you have to install the required pip libraries using
```
$ pip install -r requirements.txt
```

When it is done with installing you can open the ```setup.bat```. After its finished you have finished setting up the project!

## How to use
- First you have to collect as much images as you want from the news pages in **English**  <br>**ATTENTION:**<br> - It is recommended that the title has a specific height from the top of the page <br> - It is recommended to take the sreenshots in F12 and ALT + DRUCK and then copy it into **```images```** directory <br> - It is recommended that before the headline in the newspaper there is no text that includes your keyword
- After collecting the images you can start the project with<br>``` python main.py ```
- When you start it you are prompted to configure your video<br>- ```Keyword (Phrase)```: Enter the keyword of the news headline, that you want to focus in the output video.<br>- ```Cropped Offset```: Enter the offset you want to get (how much of the image is shown around the keyword). (**Recommended** is 250 or 200, which is also used in the example video)<br>- ```Image Duration```: The duration between the images in the video in seconds. (**Recommended** is 0.3)<br>- ```Output File```: Enter the name of the file. (It is saved with this name)
- After it says that its finished your final video is saved in the **```output```** directory with the name you entered.
- You have to try and find the settings that fit to you!
