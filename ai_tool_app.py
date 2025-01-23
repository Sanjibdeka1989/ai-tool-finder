import streamlit as st
import pandas as pd

# Load data from the local Excel file
@st.cache_data
def load_data():
    file_path = "/home/adminuser/Downloads/GitHub/ai-tool-finder/Datasheet - AI Tool.xlsx"
    return pd.read_excel(file_path)

# Load the data
data = load_data()

# Streamlit app
st.title("AI Tool Finder")

# Step 1: Select a Category
data.columns = data.columns.str.strip()
categories = data["Categories"].dropna().unique()
selected_category = st.selectbox("Select a Category:", ["-- Select --"] + list(categories))

if selected_category != "-- Select --":
    # Step 2: Select a Sub-Category
    filtered_subcategories = data[data["Categories"] == selected_category]["Sub-Categories"].dropna().unique()
    selected_subcategory = st.selectbox("Select a Sub-Category:", ["-- Select --"] + list(filtered_subcategories))

    if selected_subcategory != "-- Select --":
        # Step 3: Select a Tool
        filtered_tools = data[(data["Categories"] == selected_category) & (data["Sub-Categories"] == selected_subcategory)]["AI Tool"].dropna().unique()
        selected_tool = st.selectbox("Select a Tool:", ["-- Select --"] + list(filtered_tools))

        if selected_tool != "-- Select --":
            # Step 4: Show the description
            tool_description = data[(data["AI Tool"] == selected_tool)]["A Brief Description"].values[0]
            st.subheader("Tool Description:")
            st.write(tool_description)

st.caption("Data sourced from Excel file.")



