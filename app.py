import streamlit as st
import pandas as pd

st.title("Digilocal Audience Request Tool")

# Sample nested dictionary structure for cascading dropdowns
location_data = {
    "WEST 3": {
        "Maharashtra": {
            "Mumbai": {
                "PXI": "400001",
                "CBB": "400002"
            },
            "Pune": {
                "PNQ1": "411001"
            }
        },
        "Gujarat": {
            "Ahmedabad": {
                "AMD": "380001"
            }
        }
    },
    "NORTH 1": {
        "Delhi": {
            "New Delhi": {
                "NDL1": "110001"
            }
        }
    }
}

# Dropdown 1: Region
region = st.selectbox("Select Region", [""] + list(location_data.keys()), key="region")

# Dropdown 2: State
states = list(location_data[region].keys()) if region else []
state = st.selectbox("Select State", [""] + states, key="state")

# Dropdown 3: City
cities = list(location_data[region][state].keys()) if region and state else []
city = st.selectbox("Select City", [""] + cities, key="city")

# Dropdown 4: Store Code
stores = list(location_data[region][state][city].keys()) if region and state and city else []
store_code = st.selectbox("Select Store Code", [""] + stores, key="store")

# Dropdown 5: Pincode (auto selected)
pincode = location_data[region][state][city][store_code] if region and state and city and store_code else ""
if pincode:
    st.write(f"📍 Pincode: {pincode}")

# Time Frame Dropdown
time_frame = st.selectbox("Select Time Frame", ['Last Year', 'Last 3 Years', 'Last 5 Years'])

# Generate Button
if st.button("Generate CSVs"):
    st.write("✅ Backend will now run the SQL query...")

    # Dummy data – replace this with actual SQL result later
    dummy_data = {
        "EMAIL": ["user1@example.com", "user2@example.com"],
        "PHONE": ["+919999999999", "+918888888888"],
        "First Name": ["John", "Jane"],
        "Last Name": ["Doe", "Smith"]
    }
    df = pd.DataFrame(dummy_data)

    # Show data
    st.dataframe(df)

    # Download Buttons
    st.download_button("Download Google Format CSV", data=df.to_csv(index=False), file_name="google_format.csv", mime='text/csv')
    st.download_button("Download Meta Format CSV", data=df.to_csv(index=False), file_name="meta_format.csv", mime='text/csv')
