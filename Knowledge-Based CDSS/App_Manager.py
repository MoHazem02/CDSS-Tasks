import networkx as nx
import matplotlib.pyplot as plt
from FrameClass import *


def if_then_diagnose(window):
    if window.tab1_fever.isChecked() and window.tab1_cough.isChecked() and window.tab1_sob.isChecked():
        diagnosis = "Pneumonia"
    elif window.tab1_urination.isChecked() and window.tab1_thirst.isChecked() and window.tab1_weight_loss.isChecked():
        diagnosis = "Diabetes Mellitus"
    elif window.tab1_swelling.isChecked() and window.tab1_joint_pain.isChecked() and window.tab1_stiffness.isChecked():
        diagnosis = "Rheumatoid Arthritis"
    else:
        diagnosis = "Unknown"
    
    window.tab1_diag.setText(diagnosis)

def tab1_reset(window):
    window.tab1_fever.setChecked(False)
    window.tab1_cough.setChecked(False)
    window.tab1_sob.setChecked(False)
    window.tab1_urination.setChecked(False)
    window.tab1_thirst.setChecked(False)
    window.tab1_weight_loss.setChecked(False)
    window.tab1_swelling.setChecked(False)
    window.tab1_joint_pain.setChecked(False)
    window.tab1_stiffness.setChecked(False)
    window.tab1_diag.setText("No Disease")

def semantic_diagnose(window):
    build_semantic_network()
    if window.tab2_fever.isChecked() and window.tab2_cough.isChecked() and window.tab2_sob.isChecked():
        diagnosis = "Pneumonia"
    elif window.tab2_urination.isChecked() and window.tab2_thirst.isChecked() and window.tab2_weight_loss.isChecked():
        diagnosis = "Diabetes Mellitus"
    elif window.tab2_swelling.isChecked() and window.tab2_joint_pain.isChecked() and window.tab2_stiffness.isChecked():
        diagnosis = "Rheumatoid Arthritis"
    else:
        diagnosis = "Unknown"
    
    window.tab2_diag.setText(diagnosis)

def build_semantic_network():
    G = nx.Graph()

    # Add nodes
    G.add_node("Pneumonia")
    G.add_node("Diabetes Mellitus")
    G.add_node("Rheumatoid Arthritis")
    G.add_node("Fever")
    G.add_node("Cough")
    G.add_node("Shortness of Breath")
    G.add_node("Frequent Urination")
    G.add_node("Excessive Thirst")
    G.add_node("Weight Loss")
    G.add_node("Swelling")
    G.add_node("Joint Pain")
    G.add_node("Stiffness")

    # Add edges
    G.add_edge("Pneumonia", "Fever")
    G.add_edge("Pneumonia", "Cough")
    G.add_edge("Pneumonia", "Shortness of Breath")
    G.add_edge("Diabetes Mellitus", "Frequent Urination")
    G.add_edge("Diabetes Mellitus", "Excessive Thirst")
    G.add_edge("Diabetes Mellitus", "Weight Loss")
    G.add_edge("Rheumatoid Arthritis", "Swelling")
    G.add_edge("Rheumatoid Arthritis", "Joint Pain")
    G.add_edge("Rheumatoid Arthritis", "Stiffness")

    # Draw the network
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10, font_weight='bold')
    plt.title("Semantic Network of Clinical Concepts")
    plt.show()

def tab2_reset(window):
    window.tab2_fever.setChecked(False)
    window.tab2_cough.setChecked(False)
    window.tab2_sob.setChecked(False)
    window.tab2_urination.setChecked(False)
    window.tab2_thirst.setChecked(False)
    window.tab2_weight_loss.setChecked(False)
    window.tab2_swelling.setChecked(False)
    window.tab2_joint_pain.setChecked(False)
    window.tab2_stiffness.setChecked(False)
    window.tab2_diag.setText("No Disease")

def visualize_patient_diagnosis(patient, disease):
    """Create a visualization of the patient and diagnosed disease frames"""
    G = nx.Graph()
    
    # Add patient node
    patient_id = f"Patient: {patient.get_full_name()}"
    G.add_node(patient_id, color="lightblue", type="patient")
    
    # Add patient attributes
    for attr, value in patient.attributes.items():
        if attr not in ["first_name", "last_name"]:  # Skip these as they're in the ID
            attr_id = f"{attr}: {value}"
            G.add_node(attr_id, color="lightgreen", type="attribute")
            G.add_edge(patient_id, attr_id)
    
    # Add symptoms
    for symptom in patient.symptoms:
        G.add_node(symptom, color="yellow", type="symptom")
        G.add_edge(patient_id, symptom)
    
    # Add disease
    if disease:
        G.add_node(disease.name, color="red", type="disease")
        for symptom in disease.symptoms:
            if symptom in patient.symptoms:
                G.add_edge(disease.name, symptom)
    
    # Visualize
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)
    
    # Draw nodes with different colors based on type
    node_colors = [G.nodes[n].get("color", "gray") for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    
    plt.title(f"Patient Diagnosis Frame Visualization")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def frames_diagnose(window):
    # Get patient information from UI
    first_name = window.tab3_first_name.text()
    last_name = window.tab3_last_name.text()
    
    # Handle age - convert to int if possible, otherwise use 0
    try:
        age = int(window.tab3_age.text())
    except (ValueError, TypeError):
        age = 0
    
    # Create patient frame
    patient = PatientFrame(first_name, last_name, age)
    
    # Add symptoms based on checkboxes
    if window.tab3_fever.isChecked():
        patient.add_symptom("Fever")
    if window.tab3_cough.isChecked():
        patient.add_symptom("Cough")
    if window.tab3_sob.isChecked():
        patient.add_symptom("Shortness of Breath")
    if window.tab3_urination.isChecked():
        patient.add_symptom("Frequent Urination")
    if window.tab3_thirst.isChecked():
        patient.add_symptom("Excessive Thirst")
    if window.tab3_weight_loss.isChecked():
        patient.add_symptom("Weight Loss")
    if window.tab3_swelling.isChecked():
        patient.add_symptom("Swelling")
    if window.tab3_joint_pain.isChecked():
        patient.add_symptom("Joint Pain")
    if window.tab3_stiffness.isChecked():
        patient.add_symptom("Stiffness")
    
    # Create disease frames with default symptoms
    disease_frames = [
        DiseaseFrame("Pneumonia", ["Fever", "Cough", "Shortness of Breath"]),
        DiseaseFrame("Diabetes Mellitus", ["Frequent Urination", "Excessive Thirst", "Weight Loss"]),
        DiseaseFrame("Rheumatoid Arthritis", ["Swelling", "Joint Pain", "Stiffness"])
    ]
    
    # Diagnostic logic
    diagnosed_disease = None
    for disease in disease_frames:
        if disease.matches_symptoms(patient.symptoms):
            diagnosed_disease = disease
            break
    
    # Set diagnosis in UI
    diagnosis_text = diagnosed_disease.name if diagnosed_disease else "Unknown"
    window.tab3_diag.setText(diagnosis_text)
    
    # Visualize the diagnosis
    visualize_patient_diagnosis(patient, diagnosed_disease)

def tab3_reset(window):
    window.tab3_fever.setChecked(False)
    window.tab3_cough.setChecked(False)
    window.tab3_sob.setChecked(False)   
    window.tab3_urination.setChecked(False)
    window.tab3_thirst.setChecked(False)
    window.tab3_weight_loss.setChecked(False)
    window.tab3_swelling.setChecked(False)
    window.tab3_joint_pain.setChecked(False)
    window.tab3_stiffness.setChecked(False)
    window.tab3_first_name.setText("")
    window.tab3_last_name.setText("")
    window.tab3_age.setText("")
    window.tab3_diag.setText("No Disease")
