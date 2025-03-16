import networkx as nx
import matplotlib.pyplot as plt


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

def frames_diagnose(window):
    pass

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
    window.tab3_diag.setText("No Disease")
    