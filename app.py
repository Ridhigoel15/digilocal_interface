import streamlit as st

st.title("Digilocal Audience Request Tool")
st.write("✅ App loaded")

region = st.selectbox("Select Region", ['NORTH 1','NORTH 2'], key="region")
state = st.selectbox("Select State", ['Delhi','Punjab'], key="state")
city = st.selectbox("Select City", ['Delhi','Amritsar'], key="city")
store_code = st.selectbox("Select Store Code", ['PXI','CBB'], key="store")
pincode = st.selectbox("Select Pincode", ['110001','143001'], key="pincode")

if st.button("Generate CSV"):
    st.write("Pretend we're running the query here!")
