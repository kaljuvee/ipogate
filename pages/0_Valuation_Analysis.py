import os
import streamlit as st
import yaml

# Load revenue multipliers
with open('config/revenue-multipliers.yaml', 'r') as file:
    revenue_multipliers = yaml.safe_load(file)

# Streamlit app
st.title("IPO Valuation Analysis")

# Create options with multipliers for display
sector_options = {f"{sector} ({multiplier}x)": sector 
                 for sector, multiplier in revenue_multipliers.items()}

# Input fields
revenue_millions = st.number_input("Enter Annual Revenue (in millions)", min_value=0.0, format="%.2f")
sector_display = st.selectbox("Select Sector", options=sorted(sector_options.keys()))

# Get actual sector name from display name
sector = sector_options[sector_display]

if st.button("Get Valuation"):
    if revenue_millions and sector:
        # Get multiplier for selected sector
        multiplier = revenue_multipliers[sector]
        
        # Calculate base valuation (already in millions since input is in millions)
        base_valuation = revenue_millions * multiplier
        
        # Calculate range (±20%)
        low_valuation = base_valuation * 0.8
        high_valuation = base_valuation * 1.2
        
        # Display results
        st.write(f"Sector Multiple: {multiplier}x")
        st.write(f"Base Valuation: ${base_valuation:,.2f}M")
        st.write(f"Valuation Range:")
        st.write(f"Low (-20%): ${low_valuation:,.2f}M")
        st.write(f"High (+20%): ${high_valuation:,.2f}M")

# Add attribution at bottom
st.markdown("---")  # Add a horizontal line
st.markdown("Revenue Multipliers provided by Aswath Damodaran at New York University (<a href='http://www.damodaran.com/' target='_blank'>http://www.damodaran.com/</a>)", unsafe_allow_html=True)
