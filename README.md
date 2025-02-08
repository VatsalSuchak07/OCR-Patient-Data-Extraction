# OCR Patient Data Extraction

## Overview
This project extracts patient assessment data from scanned images using OCR (Optical Character Recognition) and stores it in a structured format. The extracted data is saved as a JSON file and inserted into a PostgreSQL database.

## Features
- Extracts text from medical assessment forms using Tesseract OCR.
- Parses the extracted text into structured JSON format.
- Saves the JSON data locally.
- Stores the JSON data in a PostgreSQL database.

## Requirements
- Python 3.8+
- OpenCV (`cv2`)
- Tesseract OCR (`pytesseract`)
- PostgreSQL (`psycopg2`)
- PDF to Image (`pdf2image`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/OCR-Patient-Data.git
   cd OCR-Patient-Data
   ```

2. Install dependencies:
   ```sh
   pip install opencv-python pytesseract psycopg2 pdf2image
   ```

3. Set up Tesseract OCR:
   - Install Tesseract OCR from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
   - Update the `tesseract_cmd` path in the Python script if necessary.

## Usage
1. Place the scanned image in the project folder and rename it to `image.png`.
2. Run the Python script:
   ```sh
   python ocr_patient_data.py
   ```
3. The extracted data will be saved as `patient_data.json` and inserted into the database.

## Database Setup
1. Start PostgreSQL and create the database:
   ```sql
   CREATE DATABASE patient_db;
   \\c patient_db;

   CREATE TABLE forms_data (
       id SERIAL PRIMARY KEY,
       form_json JSONB NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

## File Structure
```
OCR-Patient-Data/
│── OCR.py   # Main script for OCR and data processing
│── sample.json     # Extracted JSON data
│── schme.sql          # SQL script for database setup
│── README.md             # Project documentation
```

## License
This project is open-source and available under the MIT License.

## Author
- Name: Vatsal Suchak
- GitHub: [VatsalSuchak07](https://github.com/VatsalSuchak07)

