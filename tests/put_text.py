import cv2 as cv

image = cv.imread("myface.jpg")
print(image)
height, width, _ = image.shape


text = "Hello, OpenCV!"
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
color = (255, 255, 255)  
text_size = cv.getTextSize(text, font, font_scale, thickness)[0]
text_x = int((width - text_size[0]) / 2)
text_y = int((height + text_size[1]) / 2)
cv.putText(image, text, (text_x, text_y), font, font_scale, color, thickness)


cv.imshow("Image with Text", image)
cv.waitKey(0)
cv.destroyAllWindows()