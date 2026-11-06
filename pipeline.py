
import os
import pandas as pd
from extractor import extract_clinical_entities

def run_batch_pipeline(input_dir: str, output_path: str):
    processed_records = []
    
    # Read files sequentially from your local directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)
            with open(file_path, "r") as f:
                raw_text = f.read()
            
            print(f"Processing: {filename}...")
            try:
                # 1. Run extraction
                structured_data = extract_clinical_entities(raw_text)
                print('llm output', structured_data)
                record_dict = structured_data.model_dump()
                record_dict['source_file'] = filename
                print(record_dict)
                processed_records.append(record_dict)
            except Exception as e:
                # Operational safeguarding: log failures without crashing the entire batch
                print(f"Failed to parse {filename} due to: {e}")
                
    # 2. Flatten and normalize data for analytics
    # Because 'medication' is a nested list, you can normalize it into a flat tabular format
    flat_rows = []
    print('appended output:', processed_records)
    for record in processed_records:
        for med in record['medication']:
            flat_rows.append({
                "File_Source": record['source_file'],
                "Age": record['demographics'].get('age'),
                "Gender": record['demographics'].get('gender'),
                # "Blood_Pressure": record['demographics'].get('blood_pressure'),
                "Medication_Name": med['name'],
                "Dosage": med['dosage'],
                "Condition_Treated": med['condition']
            })

    # 3. Save to highly compressed Parquet format
    if flat_rows:
        df = pd.DataFrame(flat_rows)
        df.to_parquet(f"{output_path}/clinical_entities.parquet", index=False)
        df.to_csv(f"{output_path}/clinical_entities.csv", index=False)
        print(f"\nPipeline run successful. Saved structured dataset to {output_path}")
    else:
        print("No records successfully processed.")

if __name__ == "__main__":
    # Ensure you create a 'raw_notes' folder with text files before running
    run_batch_pipeline(input_dir="./bronze", output_path="./gold")
