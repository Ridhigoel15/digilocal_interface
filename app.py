import streamlit as st
import pandas as pd

st.title("Digilocal Request Tool")

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

# Dropdowns
region = st.selectbox("Select Region", [""] + list(location_data.keys()), key="region")

states = list(location_data[region].keys()) if region else []
state = st.selectbox("Select State", [""] + states, key="state")

cities = list(location_data[region][state].keys()) if region and state else []
city = st.selectbox("Select City", [""] + cities, key="city")

stores = list(location_data[region][state][city].keys()) if region and state and city else []
store_code = st.selectbox("Select Store Code", [""] + stores, key="store")

# Pincode
pincode = location_data[region][state][city][store_code] if region and state and city and store_code else ""
if pincode:
    st.write(f"📍 Pincode: {pincode}")

# Time Frame
time_frame = st.selectbox("Select Time Frame", ['Last Year', 'Last 3 Years', 'Last 5 Years'])

# Sample dummy raw data (Replace with SQL output in future)
raw_data = {
    "email": ["rudrendranathtegore@gmail.com", "hdjh@gmail.com"],
    "phone": ["919831000000", "919832000000"],
    "first name": ["RUDRENDRANATH", "SATYAJIT"],
    "last name": ["TAGORE", "BISWAS"],
}

df_raw = pd.DataFrame(raw_data)

# Add additional required fields
df_google = df_raw.copy()
df_google["country"] = "IN"
df_google["zip"] = pincode if pincode else ""

df_facebook = df_raw.rename(columns={
    "email": "registered_email",
    "first name": "firstname",
    "last name": "lastname"
})

# Show counts
st.subheader("📊 Data Preview & Counts")
st.write(f"Google CSV: **{len(df_google)}** entries")
st.write(f"Facebook CSV: **{len(df_facebook)}** entries")

# Show DataFrames
with st.expander("🔍 Preview Google Format"):
    st.dataframe(df_google)

with st.expander("🔍 Preview Facebook Format"):
    st.dataframe(df_facebook)

# Download buttons
st.subheader("⬇️ Download CSVs")
st.download_button("Download Google Format CSV", data=df_google.to_csv(index=False), file_name="google_format.csv", mime='text/csv')
st.download_button("Download Meta Format CSV", data=df_facebook.to_csv(index=False), file_name="meta_format.csv", mime='text/csv')
