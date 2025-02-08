CREATE DATABASE patient_db;

\c patient_db;

CREATE TABLE forms_data (
    id SERIAL PRIMARY KEY,
    form_json JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
