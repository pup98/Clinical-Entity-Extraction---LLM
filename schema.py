from pydantic import BaseModel, Field
from typing import List, Optional

class Medication(BaseModel):
    name: str = Field(description='name of medication')
    dosage: Optional[str] = Field(None, description='dose strength')
    condition: Optional[str] = Field(None, description='medical condition')

class ClinicalNote(BaseModel):
    demographics: dict = Field(description="Age and gender if present. Keys: 'age','gender'")
    diagnosis: List[str] = Field(description="List of medical condition identified")
    medication: List[Medication] = Field(default= [], description="List of all medications extracted from text")

