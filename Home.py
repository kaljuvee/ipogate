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

def calculate_valuation(ebitda, revenue, sector, rev_multipliers, ebidta_multipliers):
    if ebitda is not None and sector in rev_multipliers:
        rev_multiplier = rev_multipliers[sector]
        ebidta_multiplier = ebidta_multipliers[sector]
        valuation = (ebitda * ebidta_multiplier + revenue * rev_multiplier) / 2
        return valuation
    return None

def display_result(valuation, sector, ebitda, revenue):
    if valuation is not None:
        st.write(f'The estimated valuation is: ${valuation:,.2f}')
        st.write(f'Based on estimated revenue: ${revenue:,.2f}')
        st.write(f'Based on estimated EBITDA: ${ebitda:,.2f}')
        st.write(f'The company sector is: {sector}')
    else:
        st.write('Please enter valid inputs to calculate the valuation.')

def main():
    rev_multipliers = load_rev_multipliers()
    ebidta_multipliers = load_ebidta_multipliers()
    ebitda, revenue, sector = get_user_input(rev_multipliers)

    # Add a button to trigger the calculation
    if st.button('Calculate Valuation'):
        valuation = calculate_valuation(ebitda, revenue, sector, rev_multipliers, ebidta_multipliers)
        display_result(valuation, sector, ebitda, revenue)
    else:
        st.write('Enter the details and press "Calculate Valuation" to see the results.')

if __name__ == "__main__":
    main()
