import os
import streamlit as st
import yaml

# Load multipliers
with open('config/revenue-multipliers.yaml', 'r') as file:
    revenue_multipliers = yaml.safe_load(file)

with open('config/ebidta-multipliers.yaml', 'r') as file:
    ebitda_multipliers = yaml.safe_load(file)

# Streamlit app
st.title("IPO Valuation Analysis")

# Create options with multipliers for display
revenue_sector_options = {f"{sector} ({multiplier}x)": sector 
                        for sector, multiplier in revenue_multipliers.items()}

ebitda_sector_options = {f"{sector} ({multiplier}x)": sector 
                        for sector, multiplier in ebitda_multipliers.items()}

# Input fields
col1, col2 = st.columns(2)

with col1:
    revenue_millions = st.number_input("Enter Annual Revenue (in millions)", min_value=0.0, format="%.2f")
    revenue_sector_display = st.selectbox("Select Sector (Revenue Multiple)", options=sorted(revenue_sector_options.keys()))
    revenue_sector = revenue_sector_options[revenue_sector_display]

with col2:
    ebitda_millions = st.number_input("Enter Annual EBITDA (in millions)", min_value=0.0, format="%.2f")
    ebitda_sector_display = st.selectbox("Select Sector (EBITDA Multiple)", options=sorted(ebitda_sector_options.keys()))
    ebitda_sector = ebitda_sector_options[ebitda_sector_display]

if st.button("Get Valuation"):
    st.write("---")
    total_valuations = 0
    valid_methods = 0
    
    if revenue_millions > 0:
        # Revenue-based valuation
        revenue_multiplier = revenue_multipliers[revenue_sector]
        base_valuation_revenue = revenue_millions * revenue_multiplier
        low_valuation_revenue = base_valuation_revenue * 0.8
        high_valuation_revenue = base_valuation_revenue * 1.2
        
        st.subheader("Revenue Multiple Valuation")
        st.write(f"Revenue Multiple: {revenue_multiplier}x")
        st.write(f"Base Valuation: ${base_valuation_revenue:,.2f}M")
        st.write(f"Valuation Range:")
        st.write(f"Low (-20%): ${low_valuation_revenue:,.2f}M")
        st.write(f"High (+20%): ${high_valuation_revenue:,.2f}M")
        
        total_valuations += base_valuation_revenue
        valid_methods += 1
        
    if ebitda_millions > 0:
        # EBITDA-based valuation
        ebitda_multiplier = ebitda_multipliers[ebitda_sector]
        base_valuation_ebitda = ebitda_millions * ebitda_multiplier
        low_valuation_ebitda = base_valuation_ebitda * 0.8
        high_valuation_ebitda = base_valuation_ebitda * 1.2
        
        st.subheader("EBITDA Multiple Valuation")
        st.write(f"EBITDA Multiple: {ebitda_multiplier}x")
        st.write(f"Base Valuation: ${base_valuation_ebitda:,.2f}M")
        st.write(f"Valuation Range:")
        st.write(f"Low (-20%): ${low_valuation_ebitda:,.2f}M")
        st.write(f"High (+20%): ${high_valuation_ebitda:,.2f}M")
        
        total_valuations += base_valuation_ebitda
        valid_methods += 1
    
    # Show average if both methods were used
    if valid_methods == 2:
        st.write("---")
        st.subheader("Average Valuation")
        average_valuation = total_valuations / valid_methods
        st.write(f"Average Base Valuation: ${average_valuation:,.2f}M")
        st.write(f"Average Range:")
        st.write(f"Low (-20%): ${average_valuation * 0.8:,.2f}M")
        st.write(f"High (+20%): ${average_valuation * 1.2:,.2f}M")

# Add attribution at bottom
st.markdown("---")
st.markdown("Revenue and EBITDA Multipliers provided by Aswath Damodaran at New York University (<a href='http://www.damodaran.com/' target='_blank'>http://www.damodaran.com/</a>)", unsafe_allow_html=True)
