import os
import random

def generate_patient_dataset():
    # Seed for consistent generation
    random.seed(42)

    # 1. Setup lists to randomize patient files
    first_names_male = ["Aarav", "Arjun", "Vihaan", "Reyansh", "Sai", "Pranav", "Aditya", "Rohan", "Rahul", "Amit"]
    first_names_female = ["Ananya", "Diya", "Isha", "Kavya", "Meera", "Priya", "Riya", "Sanya", "Neha", "Pooja"]
    last_names = ["Sharma", "Verma", "Gupta", "Kumar", "Singh", "Joshi", "Mehta", "Patel", "Reddy", "Nair"]

    conditions_pool = [
        {
            "primary_cond": "hypertension",
            "secondary_cond": "recent onset of chronic insomnia",
            "primary_drug": "Amlodipine 5mg daily",
            "primary_reason": "blood pressure",
            "bp_range": lambda: f"{random.randint(135, 155)}/{random.randint(85, 98)}",
            "secondary_drug": "Zolpidem 5mg at bedtime",
            "secondary_reason": "insomnia",
            "advice": "Patient advised to monitor for daytime drowsiness."
        },
        {
            "primary_cond": "Type 2 Diabetes Mellitus",
            "secondary_cond": "hypercholesterolemia",
            "primary_drug": "Metformin 500mg twice daily",
            "primary_reason": "glycemic control",
            "bp_range": lambda: f"{random.randint(118, 138)}/{random.randint(75, 88)}",
            "secondary_drug": "Atorvastatin 10mg once daily",
            "secondary_reason": "cholesterol management",
            "advice": "Patient instructed to maintain a low-glycemic diet and track fasting blood glucose."
        },
        {
            "primary_cond": "chronic generalized anxiety disorder",
            "secondary_cond": "acid reflux (GERD)",
            "primary_drug": "Escitalopram 10mg daily",
            "primary_reason": "anxiety",
            "bp_range": lambda: f"{random.randint(110, 130)}/{random.randint(70, 85)}",
            "secondary_drug": "Omeprazole 20mg every morning",
            "secondary_reason": "acid reflux",
            "advice": "Patient advised to avoid caffeine and food close to bedtime."
        },
        {
            "primary_cond": "osteoarthritis of the knee",
            "secondary_cond": "mild vitamin D3 deficiency",
            "primary_drug": "Naproxen 250mg as needed for joint pain",
            "primary_reason": "pain management",
            "bp_range": lambda: f"{random.randint(120, 140)}/{random.randint(78, 90)}",
            "secondary_drug": "Cholecalciferol 60,000 IU weekly",
            "secondary_reason": "vitamin D replacement",
            "advice": "Patient counseled on gastrointestinal side effects of NSAIDs and recommended light physical therapy."
        },
        {
            "primary_cond": "persistent asthma",
            "secondary_cond": "seasonal allergic rhinitis",
            "primary_drug": "Fluticasone propionate inhaler 2 puffs daily",
            "primary_reason": "asthma control",
            "bp_range": lambda: f"{random.randint(115, 128)}/{random.randint(72, 82)}",
            "secondary_drug": "Montelukast 10mg at bedtime",
            "secondary_reason": "allergies",
            "advice": "Patient advised to rinse mouth thoroughly after inhaler use to prevent oral thrush."
        }
    ]

    # 2. Create the output directory locally
    output_dir = "./raw_notes"
    os.makedirs(output_dir, exist_ok=True)

    # 3. Generate 50 unique text files
    for i in range(1, 51):
        gender = random.choice(["male", "female"])
        age = random.randint(24, 78)
       
        if gender == "male":
            name = f"{random.choice(first_names_male)} {random.choice(last_names)}"
            pronoun = "male"
        else:
            name = f"{random.choice(first_names_female)} {random.choice(last_names)}"
            pronoun = "female"
           
        cfg = random.choice(conditions_pool)
        bp = cfg["bp_range"]()
       
        note_text = (
            f"Patient is a {age}-year-old {pronoun} presenting with a history of {cfg['primary_cond']} "
            f"and {cfg['secondary_cond']}. Currently taking {cfg['primary_drug']} for {cfg['primary_reason']}. "
            f"Blood pressure today is {bp}. Adding {cfg['secondary_drug']} for {cfg['secondary_reason']}. "
            f"{cfg['advice']}"
        )
       
        filename = f"patient_{i:03d}.txt"
        file_path = os.path.join(output_dir, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(note_text)
           
    print(f"Success! Created 50 patient files inside the '{output_dir}' directory.")

if __name__ == "__main__":
    generate_patient_dataset()