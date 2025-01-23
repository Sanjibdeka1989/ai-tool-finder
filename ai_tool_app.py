import pandas as pd
import streamlit as st

# Load the data
data = pd.read_csv("Datasheet - AI Tool.csv")  # Adjust path as necessary
data.columns = data.columns.str.strip()  # Strip any extra spaces from column names

# Debugging: Print the column names
st.write("Column Names in Dataset:", data.columns)

# Check if the required columns are present
required_columns = ["Categories", "Sub-Categories", "AI Tool", "A Brief Description"]
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    st.error(f"The following required columns are missing from the dataset: {missing_columns}")
else:
    st.title("AI Tool Finder")

    # Step 1: Select a Category
    categories = data["Categories"].dropna().unique()
    selected_category = st.selectbox("Select a Category:", ["-- Select --"] + list(categories)

    if selected_category != "-- Select --":
        # Step 2: Select a Sub-Category
        sub_categories = data[data["Categories"] == selected_category]["Sub-Categories"].dropna().unique()
        selected_sub_category = st.selectbox("Select a Sub-Category:", ["-- Select --"] + list(sub_categories))

        if selected_sub_category != "-- Select --":
            # Step 3: Select an AI Tool
            tools = data[data["Sub-Categories"] == selected_sub_category]["AI Tool"].dropna().unique()
            selected_tool = st.selectbox("Select a Tool:", ["-- Select --"] + list(tools))

            if selected_tool != "-- Select --":
                # Step 4: Display the Description
                description = data[data["AI Tool"] == selected_tool]["A Brief Description"].iloc[0]
                st.subheader(f"Description of {selected_tool}")
                st.write(description)
                st.write(data.columns)



