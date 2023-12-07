import os
import cv2

"""
load image using imread
load xml using cv2.Cascade

detect faces
put face list in a list

draw rectangle
generate new image
"""
def detect_faces(input_dir):
    # set output params
    output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'detected_faces')

    ## new path
    img_name = 'humans.jpeg'.split('.')
    new_img = img_name[0] + '-detected.' + img_name[1]
    new_img_path = os.path.join(output_dir, new_img)

    humans = cv2.imread(os.path.join(input_dir, 'humans.jpeg'), 1)
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    face_list = face_classifier.detectMultiScale(humans, 1.1, 4)
    print(face_list)

    #draw rectangle
    for (x, y, w, h) in face_list:
        cv2.rectangle(humans, (x, y), (x+w, y+h), (255, 255, 255), 4)

    #write file
    cv2.imwrite(new_img_path, face_list)




