# Bubble Sheet Marker using Optical Character Recognition (OCR)

## Introduction 
This series of Python and JavaScript files creates a desktop app where users can upload images of bubble sheet tests with 
answer keys to be marked by the computer. The script compares RGB values of individual bubbles to determine the answer
the student has chosen, and compares it to the answer key. It determines if the student has answered it correctly, and compiles all questions into a final mark. The mark is uploaded to a database that is hosted by Firebase. 

## Electron

* Python script is hosted on app created with Electron framework
* Uses pure JavaScript so users can upload images and input information
* Writes the data on a text file and activates Python script


## Python (ImageSlicer/Numpy)
* Reads data file and places into specific dictionaries
* Uses ImageSlicer module to seperate bubble sheet into individual bubbles
* Script analyzes each RGB value and uses numpy to seperate into lists based on the origin
* Figures out the darkest in the row (answer student had chosen) and cross-references with answer key
* Adds to overall score if student is right

## Firebase 
* Collects overall score and determines the percentage value
* Uploads student mark and name under a certain section in a local Firebase database

## Next Steps 
These are some future additions that can be made to the application.
* Reducing runtime 
* Expanding capabilities (true or false, short answers, etc.)
