import streamlit as st
import json
import os
import glob

def load_json_files():
    # Get all JSON files from the data directory
    json_files = glob.glob('data/*.json')
    # Extract just the filenames without path and extension
    return [os.path.basename(f) for f in json_files]

def load_json_data(filename):
    with open(os.path.join('data', filename), 'r', encoding='utf-8') as file:
        return json.load(file)

st.title("Company Background")

# File selector
json_files = load_json_files()
selected_file = st.selectbox("Select a company file", json_files)

# Generate button
if st.button('Generate from JSON'):
    if selected_file:
        data = load_json_data(selected_file)
        
        # Extract relevant information
        company_overview = data.get('company_overview', {})
        basic_info = data.get('basic_information', {})
        future_plans = data.get('future_plans', {})
        
        # Set session state values
        st.session_state['background'] = (
            f"{basic_info.get('-_company_name', '')} is {company_overview.get('-_founding_story', '')} "
            f"{company_overview.get('-_core_business_description', '')} "
            f"The company's main activities include {basic_info.get('-_main_activity', '')}"
        )
        
        st.session_state['future_plans'] = (
            f"{future_plans.get('-_development_strategy', '')} "
            f"{future_plans.get('-_expansion_goals', '')} "
            f"{future_plans.get('-_product_roadmap', '')}"
        )
        
        st.session_state['legal_info'] = (
            f"{basic_info.get('-_company_name', '')} is a {basic_info.get('-_company_type', 'company')} "
            f"established and registered on {basic_info.get('-_foundation_date', '')}.\n"
            f"Address: {basic_info.get('-_address', '')}\n"
            f"Website: {basic_info.get('-_website', '')}\n"
            f"Email: {basic_info.get('-_email', '')}\n"
            f"Phone: {basic_info.get('-_phone', '')}\n"
            f"Main activity: {basic_info.get('-_main_activity', '')}"
        )

# Background Section
st.header("Background")
background = st.text_area(
    "Edit the company's background", 
    st.session_state.get('background', ''),
    height=150
)

# Future Plans Section
st.header("Future Plans")
future_plans = st.text_area(
    "Edit the company's future plans", 
    st.session_state.get('future_plans', ''),
    height=150
)

# Company Legal Information Section
st.header("Company Legal Information")
legal_info = st.text_area(
    "Enter the company's legal information", 
    st.session_state.get('legal_info', ''),
    height=150
)

# Validate Button
if st.button('Confirm'):
    # Placeholder for future action
    st.write("Validation process will be implemented here.")
