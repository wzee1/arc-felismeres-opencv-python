# @author Farkas Zoltán
VERSION = 1.0
RELEASE_DATE = "2024.11.24"
LICENSE = "MIT licenc"

from detect_faces import detect_faces_image, detect_faces_webcam
from recognize_faces import load_known_faces, recognize_faces

def main():
    print("---------------------------------")
    print("Üdvözlöm a programban!\nKészítette: Farkas Zoltán (DE-IK)")
    print("Kurzus: Képfeldolgozás 2024 ősz")
    print(f"Verzió: {VERSION} ({RELEASE_DATE})\nLicensz: {LICENSE}")
    print("---------------------------------\n")

    known_faces, known_names = load_known_faces("data/")

    while True:
        print("\n1.) Arcok detektálása")
        print("2.) Személyfelismerés")
        user_input = input("Válasszon egy opciót: ").lower()

        if user_input in ["1", "a"]:
            sub_input = input("Kép (1/a) vagy webkamera (2/b): ").lower()
            if sub_input in ["1", "a"]:
                image_path = input("Adja meg a kép elérési útvonalát: ")
                detect_faces_image(image_path)
            elif sub_input in ["2", "b"]:
                detect_faces_webcam()
        elif user_input in ["2", "b"]:
            image_path = input("Adja meg a kép elérési útvonalát: ")
            recognize_faces(image_path, known_faces, known_names)

        exit_input = input("\nKilépéshez írja be: 'exit'. Újrakezdéshez bármelyik gomb: ").lower()
        if exit_input in ["exit", "e", "kilepes"]:
            print("Köszönöm, hogy használta a programot!")
            break

if __name__ == "__main__":
    main()
