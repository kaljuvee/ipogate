import streamlit as st

st.title("1. Company Background")

def main():    

    # Background Section
    st.header("Background")
    background = st.text_area("Enter the company's background", height=150)

    # Future Plans Section
    st.header("Future Plans")
    future_plans = st.text_area("Describe the company's future plans", height=150)

    # Company Legal Information Section
    st.header("Company Legal Information")
    legal_info = st.text_area("Enter the company's legal information", height=150)

    # Validate Button
    if st.button('Validate'):
        # Placeholder for future action
        st.write("Validation process will be implemented here.")

# Run the main function
if __name__ == "__main__":
    main()
