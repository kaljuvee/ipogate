import streamlit as st

st.title("Offer Terms")

def main():    

    # Background Section
    st.header("Offering")
    default_offering_text = '''
    In the course of the Offering, tje Company will issue and offer
up to XXXX Offer Shares. If interest in the Offering is
high and the demand of investors exceeds the number
of Offer Shares, the Issuer may increase the number of
Offer Shares by up to XX%, i.e. to a maximum of XXX,000
Offer Shares.
Assuming that all XXXX Offer Shares are subscribed
for by investors during the Offering, the registered share
capital of Company immediately after the issuing of the
new shares will be EUR XXXXX and the total number of
shares will correspondingly be XXXX.
The increase of the share capital by the amount of
the Offer Shares will presumably be registered in the
Commercial Register on or around <date> (the
date is subject to change).
The shares are freely transferrable and are not subject to
any restrictions on trading or pledging. 
    '''
    
    offering = st.text_area("Edit the company's offering details", default_offering_text, height=150)
    

    default_eligibility_text = '''
Participation in the Offering will be open to legal and
natural persons who are based in Estonia and who have
opened a securities account through a Nasdaq CSD
account operator (bank). 
    '''

    # Eligibility
    st.header("Eligibility")
    eligibility = st.text_area("Edit eligiblity details: ", default_eligibility_text, height=150)


    default_price_text = '''
Offer Shares will be priced at 3.4 euros per Offer Share,
comprising a nominal value of 10 cents and a share
premium of 3.3 euros.
    '''
    # Offer price
    st.header("Offer Price")
    offer_price = st.text_area("Edit offer price details: ", default_price_text, height=150)

    default_period_text = '''
Offer Shares will be priced at 3.4 euros per Offer Share,
comprising a nominal value of 10 cents and a share
premium of 3.3 euros.
    '''


    # Offer period
    st.header("Offer Period")
    offer_period = st.text_area("Edit offer period details: ", default_period_text, height=150)

    # Validate Button
    if st.button('Validate'):
        # Placeholder for future action
        st.write("Validation process will be implemented here.")

# Run the main function
if __name__ == "__main__":
    main()
