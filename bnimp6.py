# ============================================================
# B. Uma Maheshwar
# Bayesian Network for Student Grade Prediction
# Exact Inference using Variable Elimination
# ============================================================

# -------- Step 1: Import Required Libraries --------
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

import networkx as nx
import matplotlib.pyplot as plt


# -------- Step 2: Define Bayesian Network Structure --------
model = DiscreteBayesianNetwork([

    ('Attendance', 'StudyLevel'),
    ('Motivation', 'StudyLevel'),
    ('Motivation', 'TimeManagement'),

    ('StudyLevel', 'Performance'),
    ('TimeManagement', 'Performance'),
    ('PriorKnowledge', 'Performance'),
    ('SleepQuality', 'Performance'),
    ('StressLevel', 'Performance'),
    ('HealthCondition', 'Performance'),
    ('ExamDifficulty', 'Performance'),

    ('Performance', 'Grade')

])


# -------- Step 3: Define Prior Probabilities --------

cpd_attendance = TabularCPD('Attendance', 2, [[0.3], [0.7]])
cpd_motivation = TabularCPD('Motivation', 2, [[0.35], [0.65]])
cpd_prior = TabularCPD('PriorKnowledge', 2, [[0.45], [0.55]])
cpd_sleep = TabularCPD('SleepQuality', 2, [[0.4], [0.6]])
cpd_stress = TabularCPD('StressLevel', 2, [[0.4], [0.6]])
cpd_health = TabularCPD('HealthCondition', 2, [[0.3], [0.7]])
cpd_difficulty = TabularCPD('ExamDifficulty', 2, [[0.5], [0.5]])


# -------- Step 4: Conditional Probability Tables --------

# StudyLevel depends on Attendance and Motivation
cpd_study = TabularCPD(
    'StudyLevel', 2,
    [
        [0.70, 0.50, 0.45, 0.20],   # Low
        [0.30, 0.50, 0.55, 0.80]    # High
    ],
    evidence=['Attendance', 'Motivation'],
    evidence_card=[2, 2]
)


# TimeManagement depends on Motivation
cpd_time = TabularCPD(
    'TimeManagement', 2,
    [
        [0.6, 0.3],   # Poor
        [0.4, 0.7]    # Good
    ],
    evidence=['Motivation'],
    evidence_card=[2]
)


# Performance depends on 7 parent variables
cpd_performance = TabularCPD(
    variable='Performance',
    variable_card=2,
    values=[
        [0.8] * 128,   # Poor Performance
        [0.2] * 128    # Good Performance
    ],
    evidence=[
        'StudyLevel',
        'TimeManagement',
        'PriorKnowledge',
        'SleepQuality',
        'StressLevel',
        'HealthCondition',
        'ExamDifficulty'
    ],
    evidence_card=[2,2,2,2,2,2,2]
)


# Grade depends on Performance
cpd_grade = TabularCPD(
    'Grade', 2,
    [
        [0.8, 0.1],   # Fail
        [0.2, 0.9]    # Pass
    ],
    evidence=['Performance'],
    evidence_card=[2]
)


# -------- Step 5: Add CPDs to Model --------
model.add_cpds(
    cpd_attendance,
    cpd_motivation,
    cpd_prior,
    cpd_sleep,
    cpd_stress,
    cpd_health,
    cpd_difficulty,
    cpd_study,
    cpd_time,
    cpd_performance,
    cpd_grade
)


# -------- Step 6: Check Model --------
print("Model Valid:", model.check_model())


# ============================================================
# EXACT INFERENCE USING VARIABLE ELIMINATION
# ============================================================

# Create inference object
inference = VariableElimination(model)


# -------- Query 1 --------
# Probability of Grade given Good Conditions

result1 = inference.query(
    variables=['Grade'],
    evidence={
        'Attendance':1,
        'Motivation':1,
        'SleepQuality':1,
        'StressLevel':1,
        'HealthCondition':1,
        'ExamDifficulty':1
    },
    elimination_order='MinFill'   # Variable Elimination strategy
)

print("\nExact Inference Result (Good Conditions):")
print(result1)


# -------- Query 2 --------
# Probability of Grade given Poor Conditions

result2 = inference.query(
    variables=['Grade'],
    evidence={
        'Attendance':0,
        'Motivation':0,
        'SleepQuality':0,
        'StressLevel':0,
        'HealthCondition':0,
        'ExamDifficulty':1
    },
    elimination_order='MinFill'
)

print("\nExact Inference Result (Poor Conditions):")
print(result2)



# -------- Step 7: Visualize Bayesian Network --------

G = nx.DiGraph()
G.add_nodes_from(model.nodes())
G.add_edges_from(model.edges())

plt.figure(figsize=(10,6))

nx.draw(
    G,
    with_labels=True,
    node_size=3000,
    node_color='lightblue',
    font_size=9,
    font_weight='bold'
)

plt.title("Bayesian Network for Student Grade Prediction")
plt.show()