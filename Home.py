
import streamlit as st
import yaml

def load_industry_multipliers():
    with open('multipliers.yaml', 'r') as file:
        industry_multipliers = yaml.safe_load(file)
    return industry_multipliers

def get_user_input(industry_multipliers):
    ebit = st.text_input('Enter EBIT:', '0')
    try:
        ebit = float(ebit)
    except ValueError:
        st.error('Please enter a valid number for EBIT')
        ebit = None
    sector = st.selectbox('Select Industry Sector:', options=list(industry_multipliers.keys()))
    return ebit, sector

def calculate_valuation(ebit, sector, industry_multipliers):
    if ebit is not None and sector in industry_multipliers:
        multiplier = industry_multipliers[sector]
        valuation = ebit * multiplier
        return valuation
    return None

def display_result(valuation):
    if valuation is not None:
        st.write(f'The estimated valuation is: ${valuation:,.2f}')
    else:
        st.write('Please enter valid inputs to calculate the valuation.')

def main():
    st.title('Valuation Calculator')
    industry_multipliers = load_industry_multipliers()
    ebit, sector = get_user_input(industry_multipliers)
    valuation = calculate_valuation(ebit, sector, industry_multipliers)
    display_result(valuation)

if __name__ == "__main__":
    main()
