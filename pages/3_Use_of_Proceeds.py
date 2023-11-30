import streamlit as st

st.title("Use of Proceeds")

def main():    

    # Background Section
    st.header("Use of Proceeds")
        default_proceeds_text = '''
Bercman intends to use the revenue from the offer
for growth and product development. The estimated
revenue from the offer is approximately XXXX euros,
in the case of over-subscription, the offer will amount
to XXXX euros. The cost of preparing the offer is
approximately XXXX euros. The net proceeds from the
offer are therefore XXXX euros. Bercman intends to
use the net income to finance the following steps:
(i) investments into the optimisation of our product
Smart Pedestrian Crosswalk, including the expansion
of the engineering and software team to increase
vertical integration;
(ii) expansion of the sales team and increase of export
activities through international distributors;
(iii) investments into a project in development – a product
that meets the requirements of railway management
systems;
(iv)investments into product development and communication;
The purpose of applying for admission to trading
is to make Bercman more transparent and credible
for shareholders, investors, partners, and customers.
Nasdaq is a quality label that plays an important role in
the company’s sales strategy.  
    '''
    proceeds = st.text_area("Edit the company's background", default_proceeds_text, height=150)

    # Validate Button
    if st.button('Validate'):
        # Placeholder for future action
        st.write("Validation process will be implemented here.")

# Run the main function
if __name__ == "__main__":
    main()
