import streamlit as st
import pandas as pd

st.title("Digilocal Audience Request Tool")

# Full region list
regions_list = ['NORTH 1','NORTH 2','NORTH 3','NORTH 4',
                'WEST 1','WEST 2', 'WEST 3',
                'EAST 1','EAST 2',
                'SOUTH 1','SOUTH 2','SOUTH 3']

# Sample nested dictionary (you can expand this with real store data)
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
    # You can continue adding for all 12 regions here...
}

# Multi-select for cascading dropdowns
selected_regions = st.multiselect("Select Region(s)", regions_list)
selected_states = []
selected_cities = []
selected_store_codes = []

if selected_regions:
    # Collect unique states for selected regions
    states_set = set()
    for reg in selected_regions:
        if reg in location_data:
            states_set.update(location_data[reg].keys())
    selected_states = st.multiselect("Select State(s)", sorted(states_set))

    # Collect unique cities for selected states
    cities_set = set()
    for reg in selected_regions:
        for state in selected_states:
            if reg in location_data and state in location_data[reg]:
                cities_set.update(location_data[reg][state].keys())
    selected_cities = st.multiselect("Select City(s)", sorted(cities_set))

    # Collect store codes for selected cities
    stores_set = set()
    for reg in selected_regions:
        for state in selected_states:
            for city in selected_cities:
                if (reg in location_data and
                    state in location_data[reg] and
                    city in location_data[reg][state]):
                    stores_set.update(location_data[reg][state][city].keys())
    selected_store_codes = st.multiselect("Select Store Code(s)", sorted(stores_set))

# Time Frame Dropdown
time_frame = st.selectbox("Select Time Frame", ['Last Year', 'Last 3 Years', 'Last 5 Years'])

# Dummy filtered data — you can hook actual logic later
dummy_data = [
    ["RUDRENDRANATHTEGORE@GMAIL.COM", "919831000000", "RUDRENDRANATH", "TAGORE", "IN", "400001"],
    ["HDJH@GMAIL.COM", "919832000000", "SATYAJIT", "BISWAS", "IN", "400002"],
    ["SUJAYASANYAL123@GMAIL.COM", "919830000000", "SUJAYA", "SANYAL", "IN", "411001"],
    ["NABANITADEBNATH63@GMAIL.COM", "919903000000", "N", "SAHA", "IN", "380001"]
]
df = pd.DataFrame(dummy_data, columns=["email", "phone", "first name", "last name", "country", "zip"])

# Filter the dummy dataframe based on selected store codes (simulate filtering)
if selected_store_codes:
    df = df[df["zip"].isin([
        location_data[reg][state][city][store]
        for reg in selected_regions
        for state in selected_states
        for city in selected_cities
        for store in selected_store_codes
        if (reg in location_data and
            state in location_data[reg] and
            city in location_data[reg][state] and
            store in location_data[reg][state][city])
    ])]

# Generate Button
if st.button("Generate CSVs"):
    st.success("✅ Data ready to download!")
    
    # Google CSV format
    google_df = df[["email", "phone", "first name", "last name", "country", "zip"]]
    st.markdown(f"📧 **Google CSV Rows**: {len(google_df)}")
    st.download_button("📥 Download Google Format CSV",
                       data=google_df.to_csv(index=False),
                       file_name="google_format.csv", mime='text/csv')

    # Facebook CSV format
    fb_df = df.rename(columns={
        "email": "registered_email",
        "first name": "firstname",
        "last name": "lastname"
    })[["registered_email", "phone", "firstname", "lastname"]]
    st.markdown(f"📘 **Facebook CSV Rows**: {len(fb_df)}")
    st.download_button("📥 Download Meta Format CSV",
                       data=fb_df.to_csv(index=False),
                       file_name="meta_format.csv", mime='text/csv')
