# @author Farkas Zoltán

import cv2
import numpy as np
import os

# Előre betanított modell:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def load_known_faces(directory):
    print("Képek betöltése folyamatban...")

    known_faces, known_names = [], []

    # Adott mappában keressük az előre megadott emberek arcait
    # "data" mappában "keresztnev_vezeteknev" formátumban
    for name in os.listdir(directory):
        person_path = os.path.join(directory, name)
        for image_file in os.listdir(person_path):
            image_path = os.path.join(person_path, image_file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Haar Cascade modell szerint felismeri az arcokat a képen
            faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

            # Talált arcokat elmentem a tömbökben
            for (x, y, w, h) in faces:
                face = image[y:y + h, x:x + w]
                face_resized = cv2.resize(face, (100, 100))
                known_faces.append(face_resized)
                known_names.append(name)

    print("Képek betöltve!")
    return known_faces, known_names


def recognize_faces(image_path, known_faces, known_names):
    if not os.path.exists(image_path):
        print("HIBA: Nem található a kép a megadott útvonalon!")
        return

    image_original = cv2.imread(image_path, 1)
    image = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

    # Haar Cascade modell szerint felismeri az arcokat a képen
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = image[y:y + h, x:x + w]  # Felismert arc körbevágása
        face_resized = cv2.resize(face, (100, 100))

        # A betanított arcokkal összehasonlítás
        # Mean Squared Error:
        # --> Kiszámítja az átlagos négyzetes eltérést a két arc között
        # --> Minél kisebb az érték, annál inkább egyezőek a képek
        min_distance = float('inf')
        matched_name = "Ismeretlen" # Alapérték

        for i, known_face in enumerate(known_faces):
            distance = np.mean((known_face - face_resized) ** 2)  # MSE-hez kell
            threshold = 100
            if distance < min_distance and distance < threshold:
                min_distance = distance
                matched_name = known_names[i]
                matched_name = matched_name.replace("_", " ")

        print(f"A képen lévő ember: {matched_name}")

        cv2.rectangle(image_original, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image_original, matched_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Felismert ember", image_original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

