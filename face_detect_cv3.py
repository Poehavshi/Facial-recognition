'''
Обнаружение и вырезание лиц
с картинки при помощи каскадов Хаара
'''
import cv2

# Пути до файлов
imagePath = "Abdullah_Nasseef_0001.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Создаем каскад Хаара
faceCascade = cv2.CascadeClassifier(cascPath)

# Читаем изображение
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Обнаруживаем лицо на изображении
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

for (x, y, w, h) in faces:
    crop_image = image[y:y+h, x:x+w]

cv2.imshow("Cropped", crop_image)
cv2.imshow("Faces found", image)

if len(faces) != 0:
    cv2.imwrite(f'Square_faces\\{imagePath}_cropped.jpg', crop_image)

cv2.waitKey(0)
