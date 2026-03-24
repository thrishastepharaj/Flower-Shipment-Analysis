import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Flower Shipment App", layout="wide")

# Title
st.title("🌸 Flower Shipment Analysis Dashboard")

# Load dataset
df = pd.read_csv(r"D:\iris\Flower shipment.csv")

# Sidebar
st.sidebar.header("Filter Options")

# Show dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Dataset")
    st.dataframe(df)

# Show summary
if st.sidebar.checkbox("Show Summary"):
    st.subheader("Statistical Summary")
    st.write(df.describe())

# Column selection
column = st.sidebar.selectbox("Select Column", df.columns)

# Filter input
value = st.sidebar.text_input("Enter value to filter")

if value:
    filtered_df = df[df[column].astype(str).str.contains(value)]
    st.subheader("Filtered Data")
    st.write(filtered_df)
else:
    filtered_df = df

# ---------------- CHARTS ---------------- #

st.subheader("📊 Data Visualization")

# Select numeric column for chart
num_col = st.selectbox("Select numeric column for chart", df.select_dtypes(include=['int64','float64']).columns)

# Bar chart
st.write("Bar Chart")
st.bar_chart(filtered_df[num_col])

# Line chart
st.write("Line Chart")
st.line_chart(filtered_df[num_col])

# Histogram using matplotlib
st.write("Histogram")
fig, ax = plt.subplots()
ax.hist(filtered_df[num_col])
st.pyplot(fig)