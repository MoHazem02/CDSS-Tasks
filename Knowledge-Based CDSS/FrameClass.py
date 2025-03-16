# Base frame class for inheritance
class Frame:
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes or {}
    
    def get_attribute(self, attr_name, default=None):
        return self.attributes.get(attr_name, default)
    
    def set_attribute(self, attr_name, value):
        self.attributes[attr_name] = value

# Patient profile frame
class PatientFrame(Frame):
    def __init__(self, first_name, last_name, age, symptoms=None):
        super().__init__("Patient", {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        })
        self.symptoms = symptoms or []
    
    def add_symptom(self, symptom):
        if symptom and symptom not in self.symptoms:
            self.symptoms.append(symptom)
    
    def get_full_name(self):
        return f"{self.attributes['first_name']} {self.attributes['last_name']}"

# Disease frame with default symptoms
class DiseaseFrame(Frame):
    def __init__(self, name, symptoms=None, risk_factors=None):
        super().__init__(name, {"risk_factors": risk_factors or []})
        self.symptoms = symptoms or []
    
    def matches_symptoms(self, patient_symptoms):
        # Check if all required symptoms for this disease are present
        return all(symptom in patient_symptoms for symptom in self.symptoms)