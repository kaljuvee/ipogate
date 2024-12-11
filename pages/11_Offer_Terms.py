import streamlit as st

st.title("Offer Terms")

# Numeric input fields
st.header("Enter Offering Details")
col1, col2 = st.columns(2)

with col1:
    initial_shares = st.number_input("Initial number of Offer Shares", min_value=0, value=1000)
    max_increase_percent = st.number_input("Maximum increase percentage", min_value=0, max_value=100, value=20)
    share_nominal_value = st.number_input("Share nominal value (EUR)", min_value=0.0, value=0.10, format="%.2f")
    share_premium = st.number_input("Share premium (EUR)", min_value=0.0, value=3.30, format="%.2f")

with col2:
    max_shares = st.number_input("Maximum number of Offer Shares", min_value=0, value=1200)
    post_offering_capital = st.number_input("Post-offering share capital (EUR)", min_value=0, value=100000)
    total_shares_after = st.number_input("Total number of shares after offering", min_value=0, value=10000)
    registration_date = st.date_input("Expected registration date")

# Generate button to create formatted text
if st.button('Generate Offer Terms'):
    offer_price = share_nominal_value + share_premium
    
    st.markdown("### Generated Offer Terms")
    
    # Offering Section
    st.markdown("#### Offering")
    st.markdown(f"""
    In the course of the Offering, the Company will issue and offer
up to {initial_shares:,} Offer Shares. If interest in the Offering is
high and the demand of investors exceeds the number
of Offer Shares, the Issuer may increase the number of
Offer Shares by up to {max_increase_percent}%, i.e. to a maximum of {max_shares:,}
Offer Shares.

Assuming that all {initial_shares:,} Offer Shares are subscribed
for by investors during the Offering, the registered share
capital of Company immediately after the issuing of the
new shares will be EUR {post_offering_capital:,} and the total number of
shares will correspondingly be {total_shares_after:,}.

The increase of the share capital by the amount of
the Offer Shares will presumably be registered in the
Commercial Register on or around {registration_date.strftime('%d %B %Y')} (the
date is subject to change).

The shares are freely transferrable and are not subject to
any restrictions on trading or pledging.
    """)
    
    # Eligibility Section
    st.markdown("#### Eligibility")
    st.markdown("""
    Participation in the Offering will be open to legal and
natural persons who are based in Estonia and who have
opened a securities account through a Nasdaq CSD
account operator (bank).
    """)
    
    # Offer Price Section
    st.markdown("#### Offer Price")
    st.markdown(f"""
    Offer Shares will be priced at {offer_price:.2f} euros per Offer Share,
comprising a nominal value of {share_nominal_value:.2f} cents and a share
premium of {share_premium:.2f} euros.
    """)
    
    # Save to session state if needed
    st.session_state['offering_text'] = {
        'initial_shares': initial_shares,
        'max_increase_percent': max_increase_percent,
        'max_shares': max_shares,
        'post_offering_capital': post_offering_capital,
        'total_shares_after': total_shares_after,
        'registration_date': registration_date,
        'share_nominal_value': share_nominal_value,
        'share_premium': share_premium,
        'offer_price': offer_price
    }

# Validate Button
if st.button('Confirm'):
    if 'offering_text' in st.session_state:
        st.success("Offer terms have been validated and saved.")
    else:
        st.error("Please generate the offer terms first before confirming.")
