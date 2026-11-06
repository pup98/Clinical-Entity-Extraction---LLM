import ollama
from schema import ClinicalNote

def extract_clinical_entities(raw_text: str) -> ClinicalNote:
    system_instruction = (
        "You are an advanced medical NLP engine. Your job is to parse unstructured clinical narratives "
        "and extract specific clinical entities. You must strictly adhere to the requested JSON schema. "
        "Do not include any conversational text, pleasantries, or markdown wrappers outside the JSON."
    )
    
    response = ollama.chat(
        model='mistral:7b',
        messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': f"Extract data from this clinical note:\n\n{raw_text}"}
        ],
        # This parameter guarantees the local model shapes its output to your Pydantic object
        format = ClinicalNote.model_json_schema() 
    )
    
    raw_content = response['message']['content']
    
    # Validation step: converts raw ic object
    validated_data = ClinicalNote.model_validate_json(raw_content)
    return validated_data