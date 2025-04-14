import streamlit as st
import pandas as pd

st.title("Digilocal Audience Request Tool")

# Dropdowns
region = st.selectbox("Select Region", ['NORTH 1','NORTH 2','NORTH 3','NORTH 4','WEST 1','WEST 2', 'WEST 3','EAST 1','EAST 2','SOUTH 1','SOUTH 2','SOUTH 3'])
store = st.text_input("Enter Store Code (e.g., PXI, CBB, etc.)")
time_frame = st.selectbox("Select Time Frame", ['Last Year','Last 3 Years', 'Last 5 Years'])
audience_type = st.selectbox("Select Audience Type", [
    "All Buyers", "Gold Coin Buyers", "Frequent Buyers", 
    "Online Purchasers", "Festive Buyers", "Diamond Buyers"
])


# Generate Button
if st.button("Generate CSVs"):
    st.write("Backend will now run the SQL query...")
    # Place function to run the query here
    # Simulate result table
    dummy_data = {
        "EMAIL": ["user1@example.com", "user2@example.com"],
        "PHONE": ["+919999999999", "+918888888888"],
        "First Name": ["John", "Jane"],
        "Last Name": ["Doe", "Smith"]
    }
    df = pd.DataFrame(dummy_data)

    # Show data
    st.dataframe(df)

    # Download buttons
    st.download_button("Download Google Format CSV", data=df.to_csv(index=False), file_name="google_format.csv", mime='text/csv')
    st.download_button("Download Meta Format CSV", data=df.to_csv(index=False), file_name="meta_format.csv", mime='text/csv')

