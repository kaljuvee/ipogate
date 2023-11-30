import streamlit as st

st.title("Company Background")

def main():    

    # Background Section
    st.header("Background")
    default_background_text = '''
Company is a deep-tech company founded in 2020 and primarily engaged in the development and sale of products and services for increasing road safety. The
company’s core competency lies in high value-adding and continuously improved software and expertise in the field. In addition to developing software, Bercman also engages in in-house hardware development,but relies on contractual partners for manufacturing
operations. 
    '''
    background = st.text_area("Edit the company's background", default_background_text, height=150)

    # Future Plans Section
    st.header("Future Plans")
    default_plan_text = '''
    Bercman is actively looking for opportunities to further
develop its core technologies, expand its partner
network with new resellers, and increase sales in Europe.
The company’s preferred target markets in the medium
term are densely populated countries in western and
central Europe.

    '''
    future_plans = st.text_area("Edit the company's future plans", default_plan_text, height=150)

    # Company Legal Information Section
    st.header("Company Legal Information")
        default_legal_text = '''
AS Company is a public limited company established and registered on <date> in Estonia.
The main information for Bercman:
Registry code: 1212212121;
Address: <address>
Website: https://www.bercman.com/
Email: info @ bercman. com;
Phone: +372 XXXXXXX
VAT number: EEXXXXXX;
Main activity: other manufacturing n.e.c. (32991 EMTAK 2008). 
    '''
    legal_info = st.text_area("Enter the company's legal information", default_legal_text , height=150)

    # Validate Button
    if st.button('Validate'):
        # Placeholder for future action
        st.write("Validation process will be implemented here.")

# Run the main function
if __name__ == "__main__":
    main()
