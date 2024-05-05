This script is part of a larger to add facial recognition to my laptop. It uses OpenCV and the DeepFace library to continuously check the webcam feed against a reference image of my face. If a match is found, it displays "VERIFIED" on the video stream; otherwise, it shows "NOT VERIFIED". Threading is used to prevent interruptions to the video stream during the matching process, so it should be smooth.
The compute resources for the deepface library is a lot because of how it uses tensorflow so you'll need a computer with a good CPU lol.

## To use

You'll need to make sure you have opencv and the [deepface framework](https://github.com/serengil/deepface).

### Installation

Clone the repository: 
```
git clone https://github.com/Fadeleke57/deep-face.git
```
Navigate to the project directory: 
```
cd deep-face
```

Install dependencies:
```
pip install -r requirement.txt
``` 
