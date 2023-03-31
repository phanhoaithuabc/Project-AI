import cv2
import numpy as np
import face_recognition

thutrain = face_recognition.load_image_file('thutrain.jpg')
thutrain = cv2.cvtColor(thutrain, cv2.COLOR_BGR2RGB)
thutest = face_recognition.load_image_file('thutest1.jpg')
thutest = cv2.cvtColor(thutest, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(thutrain)[0]
encodethu = face_recognition.face_encodings(thutrain)[0]
cv2.rectangle(thutrain, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255,0,522), 2)

faceLocTest = face_recognition.face_locations(thutest)[0]
encodetest = face_recognition.face_encodings(thutest)[0]
cv2.rectangle(thutest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,522), 2)

result = face_recognition.compare_faces([encodethu], encodetest)
facedis = face_recognition.face_distance([encodethu], encodetest)
print(result, facedis)
cv2.putText(imgTest,f'{result} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

# cv2.imshow('thu', thutrain)
# cv2.waitKey(0)