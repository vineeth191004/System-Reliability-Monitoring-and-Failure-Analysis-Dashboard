import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("predictive_maintenance.csv")

# Remove hidden spaces in column names
df.columns = df.columns.str.strip()

st.title("System Reliability Monitoring Dashboard")

# -----------------------------
# Dataset Preview
# -----------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head())

# -----------------------------
# Failure Rate
# -----------------------------

failure_rate = df["Target"].mean()

st.subheader("Machine Failure Rate")

st.write("Failure Rate:", round(failure_rate * 100, 2), "%")

# -----------------------------
# Failure Distribution
# -----------------------------

st.subheader("Failure Distribution")

failure_counts = df["Target"].value_counts()

fig1, ax1 = plt.subplots()

ax1.bar(["No Failure", "Failure"], failure_counts)

ax1.set_ylabel("Count")

ax1.set_title("Machine Failure Distribution")

st.pyplot(fig1)

# -----------------------------
# Failure Type Distribution
# -----------------------------

st.subheader("Failure Type Distribution")

fig2, ax2 = plt.subplots()

sns.countplot(x="Failure Type", data=df, ax=ax2)

plt.xticks(rotation=30)

st.pyplot(fig2)

# -----------------------------
# Risk Indicator Graph
# -----------------------------

st.subheader("Air Temperature vs Failure")

fig3, ax3 = plt.subplots()

sns.boxplot(x="Target", y="Air temperature [K]", data=df, ax=ax3)

st.pyplot(fig3)

# -----------------------------
# Tool Wear Risk Indicator
# -----------------------------

st.subheader("Tool Wear vs Failure")

fig4, ax4 = plt.subplots()

sns.boxplot(x="Target", y="Tool wear [min]", data=df, ax=ax4)

st.pyplot(fig4)

# -----------------------------
# Correlation Heatmap
# -----------------------------

st.subheader("Feature Correlation Heatmap")

numeric_df = df[[
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
    "Target"
]]

fig5, ax5 = plt.subplots(figsize=(8,6))

sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=True, ax=ax5)

st.pyplot(fig5)