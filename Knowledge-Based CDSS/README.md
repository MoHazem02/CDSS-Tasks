# Knowledge-Based Clinical Decision Support System (CDSS)

## Overview
This Knowledge-Based Clinical Decision Support System (CDSS) is a Python application designed to assist healthcare providers in diagnosing common diseases using multiple knowledge representation techniques. The system implements three different approaches to clinical reasoning: IF-THEN rules, semantic networks, and frames.

## Features
- **Multiple Knowledge Representation Techniques**:
  - IF-THEN Rules for straightforward clinical guideline implementation
  - Semantic Networks for visualizing relationships between symptoms and diseases
  - Frame-Based Representation for detailed patient and disease modeling
- **User-Friendly Interface**:
  - Intuitive PyQt5-based GUI with tabbed interface for different diagnostic approaches
  - Simple symptom checkboxes for quick data entry
  - Patient information management
- **Visualization Capabilities**:
  - Semantic network visualization of medical knowledge
  - Patient-disease frame relationship visualization

### If-Then
![image](https://github.com/user-attachments/assets/02070966-b7bb-4509-913a-7391a51115da)

### Semantic Network
![image](https://github.com/user-attachments/assets/0468079f-5a49-4096-9fe0-fb2362cfbca7)

### Frame-Based Visualization
![image](https://github.com/user-attachments/assets/27afdf4f-08c7-4658-93a0-35bbac9b16e7)


## System Requirements
- Python 3.7+
- PyQt5
- NetworkX
- Matplotlib

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/MoHazem02/knowledge-based-cdss.git
   cd knowledge-based-cdss
   ```

2. Install required packages:
   ```
   pip install pyqt5 networkx matplotlib
   ```

3. Run the application:
   ```
   python CDSS.py
   ```

## Usage

### IF-THEN Rules Module (Tab 1)
1. Select the symptoms exhibited by the patient using the checkboxes
2. Click the "Diagnose" button to apply rule-based reasoning
3. View the diagnosis in the diagnosis box
4. Click "Reset" to clear all selections

### Semantic Network Module (Tab 2)
1. Select patient symptoms using checkboxes
2. Click "Diagnose" to view semantic network visualization and diagnosis
3. The visualization shows relationships between symptoms and diseases
4. Click "Reset" to clear selections

### Frame-Based Module (Tab 3)
1. Enter patient information (first name, last name, age)
2. Select patient symptoms using checkboxes
3. Click "Diagnose" to create patient and disease frames and visualize their relationships
4. Click "New Patient" to reset the form

## File Structure

- **CDSS.py**: Main application file containing the PyQt5 GUI implementation
- **App_Manager.py**: Contains the implementation of all diagnostic modules:
  - IF-THEN rules implementation
  - Semantic network builder and visualizer
  - Frame-based diagnosis functions
- **FrameClass.py**: Defines the frame classes used in the frame-based module:
  - Base `Frame` class
  - `PatientFrame` for patient data
  - `DiseaseFrame` for disease information

## Implementation Details

### IF-THEN Rules Module
The IF-THEN rules module uses conditional statements to map symptoms to diseases:
- Fever + Cough + Shortness of Breath → Pneumonia
- Frequent Urination + Excessive Thirst + Weight Loss → Diabetes Mellitus
- Swelling + Joint Pain + Morning Stiffness → Rheumatoid Arthritis

### Semantic Network Module
The semantic network represents clinical concepts as nodes and their relationships as edges:
- Disease nodes connected to their associated symptom nodes
- NetworkX and Matplotlib used for visualization

### Frame-Based Module
The frame-based approach uses object-oriented structures to represent:
- Patient frames with personal information and symptoms
- Disease frames with associated symptoms
- Inheritance hierarchy to manage common properties
- Visualization of the relationship between patient symptoms and diagnosed disease

## Future Enhancements
- Addition of more diseases and symptoms
- Integration with electronic health record systems
- Implementing certainty factors for more nuanced diagnosis
- Adding treatment recommendations based on diagnosis

## Contributors
- Mohamed Hazem
