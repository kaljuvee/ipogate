import os
import streamlit as st
import yaml

# Load revenue multipliers
with open('config/revenue-multipliers.yaml', 'r') as file:
    revenue_multipliers = yaml.safe_load(file)

# Streamlit app
st.title("IPO Valuation Analysis")

# Input fields
revenue = st.number_input("Enter Annual Revenue", min_value=0.0, format="%.2f")
sector = st.selectbox("Select Sector", options=sorted(revenue_multipliers.keys()))

if st.button("Get Valuation"):
    if revenue and sector:
        # Get multiplier for selected sector
        multiplier = revenue_multipliers[sector]
        
        # Calculate base valuation
        base_valuation = revenue * multiplier
        
        # Calculate range (±20%)
        low_valuation = base_valuation * 0.8
        high_valuation = base_valuation * 1.2
        
        # Display results
        st.write(f"Sector Multiple: {multiplier}x")
        st.write(f"Base Valuation: ${base_valuation:,.2f}")
        st.write(f"Valuation Range:")
        st.write(f"Low (-20%): ${low_valuation:,.2f}")
        st.write(f"High (+20%): ${high_valuation:,.2f}")
