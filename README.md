# System Reliability Monitoring and Failure Analysis Dashboard

## Overview

This project focuses on analyzing machine operational data to identify **failure trends, reliability risks, and system performance indicators**.  
A **Streamlit-based dashboard** is developed to visualize reliability metrics, failure patterns, and correlations between operational parameters.

The goal of this project is to demonstrate how **data analysis and monitoring tools can support reliability engineering and predictive maintenance tasks**.

---

## Project Objectives

- Analyze machine operational data for reliability insights
- Detect **failure patterns and anomaly indicators**
- Monitor system health through visual dashboards
- Identify relationships between machine parameters and failures
- Support **data-driven reliability decision making**

---

## Dataset

The project uses the **AI4I Predictive Maintenance Dataset**.

Dataset features include:

| Feature | Description |
|------|------|
| Type | Machine type |
| Air temperature [K] | Ambient air temperature |
| Process temperature [K] | Machine process temperature |
| Rotational speed [rpm] | Speed of machine rotation |
| Torque [Nm] | Mechanical load |
| Tool wear [min] | Tool wear time |
| Target | Machine failure (0 = No failure, 1 = Failure) |
| Failure Type | Category of failure |

Dataset Source:  
UCI Machine Learning Repository

---

## Features of the Dashboard

The dashboard provides the following monitoring capabilities:

### 1. Failure Rate Monitoring
Displays overall machine failure percentage in the dataset.

### 2. Failure Distribution Analysis
Shows the number of machines that failed vs those that did not.

### 3. Failure Type Analysis
Visualizes different types of machine failures.

### 4. Risk Indicator Analysis
Evaluates how operational parameters influence machine failures.

Examples:
- Air Temperature vs Failure
- Tool Wear vs Failure

### 5. Feature Correlation Analysis
Heatmap showing relationships between machine parameters and failures.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Machine Learning Concepts

---

## Project Structure
