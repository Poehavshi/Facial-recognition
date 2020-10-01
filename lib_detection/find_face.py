import face_recognition
import cv2
image = face_recognition.load_image_file("test_image.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)
for top, right, bottom, left in face_locations:
    crop_image = image[top:bottom, left:right]
cv2.imshow("Show", crop_image)
cv2.waitKey(0)
