import streamlit as st
import yaml

REV_PATH = 'config/revenue-multipliers.yaml'
EBIDTA_PATH = 'config/ebidta-multipliers.yaml'

st.title('Valuation Calculator')

def load_rev_multipliers():
    with open(REV_PATH, 'r') as file:
        rev_multipliers = yaml.safe_load(file)
    return rev_multipliers

def load_ebidta_multipliers():
    with open(EBIDTA_PATH, 'r') as file:
        ebidta_multipliers = yaml.safe_load(file)
    return ebidta_multipliers
    
def get_user_input(rev_multipliers):
    ebidta = st.text_input('Enter EBIDTA:', '0')
    revenue = st.text_input('Enter revenue:', '0')
    try:
        ebidta = float(ebidta)
        revenue = float(revenue)
    except ValueError:
        st.error('Please entervalid numbers for EBIDTA an Revenue')
        ebidta = None
        revenue = None
    sector = st.selectbox('Select Industry Sector:', options=list(rev_multipliers.keys()))
    return ebidta, revenue, sector

def calculate_valuation(ebidta, revenue, sector, rev_multipliers, ebidta_multipliers):
    if ebit is not None and sector in rev_multipliers:
        rev_multiplier = rev_multipliers[sector]
        ebidta_multiplier = ebidta_multipliers[sector]
        valuation = (ebidta * ebidta_multiplier + rrevenue * ev_multiplier) / 2
        return valuation
    return None

def display_result(valuation, sector, ebidta, revenue):
    if valuation is not None:
        st.write(f'The estimated valuation is: ${valuation:,.2f}')
        st.write(f'Based on estimated revenue: ${revenue:,.2f}')
        st.write(f'Based on estimated EBIDTA: ${ebidta:,.2f}')
        st.write(f'The company sector is: ${sector}')
    else:
        st.write('Please enter valid inputs to calculate the valuation.')

def main():
    rev_multipliers = load_rev_multipliers()
    ebidta_multipliers = load_ebidta_multipliers()
    ebidta, revenue, sector = get_user_input(rev_multipliers)
    valuation = calculate_valuation(ebidta, sector, rev_multipliers, ebidta_multipliers)
    display_result(valuation, sector, ebidta, revenue)

if __name__ == "__main__":
    main()
