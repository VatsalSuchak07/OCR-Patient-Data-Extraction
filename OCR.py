import cv2
import pytesseract
import json
import psycopg2
from pdf2image import convert_from_path


def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(gray)
    return text


def parse_text_to_json(text):
    lines = text.split('\n')
    data = {
        "patient_name": "",
        "dob": "",
        "injection": "No",
        "exercise_therapy": "No",
        "tasks_difficulty": {},
        "patient_changes_since_last_treatment": "",
        "patient_changes_since_start_of_treatment": "",
        "functional_changes_last_three_days": "",
        "pain_symptoms": {},
        "medical_assessment": {}
    }

    for line in lines:
        if "Patient Name" in line:
            data["patient_name"] = line.split(":")[-1].strip()
        elif "DOB" in line:
            data["dob"] = line.split(":")[-1].strip()
        elif "INJECTION" in line:
            data["injection"] = "Yes" if "YES" in line else "No"
        elif "Exercise Therapy" in line:
            data["exercise_therapy"] = "Yes" if "YES" in line else "No"
        elif "Pain:" in line:
            values = [int(s) for s in line.split() if s.isdigit()]
            data["pain_symptoms"] = {
                "pain": values[0], "numbness": values[1], "tingling": values[2], "burning": values[3],
                "tightness": values[4]
            }
        elif "Weight:" in line:
            parts = line.split()
            data["medical_assessment"] = {
                "weight": parts[-2], "height": parts[-1]
            }

    return json.dumps(data, indent=4)


def store_data_in_db(json_data):
    conn = psycopg2.connect(
        dbname="patient_db",
        user="user",
        password="password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO forms_data (form_json) VALUES (%s)", (json_data,))
    conn.commit()
    cursor.close()
    conn.close()


def save_json_to_file(json_data, filename="patient_data.json"):
    with open(filename, "w") as json_file:
        json_file.write(json_data)


def main():
    file_path = "image.png"
    text = extract_text_from_image(file_path)
    json_data = parse_text_to_json(text)
    save_json_to_file(json_data)
    store_data_in_db(json_data)
    print("Data successfully stored in the database and saved to JSON file.")


if __name__ == "__main__":
    main()
