import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Function to load users from a YAML file
users_file = 'pages/users.yaml'
def load_users():
    with open(users_file, 'r') as file:
        return yaml.safe_load(file)['users']

# Function to save users to a YAML file
def save_users(users):
    with open(users_file, 'w') as file:
        yaml.dump({'users': users}, file)

# Load users
users = load_users()
# Debug: Print loaded users
st.write("Loaded users:", users)

# Create user data for authenticator
names = list(users.keys())
hashed_passwords = [users[name]['password'] for name in names]
emails = [users[name]['email'] for name in names]

# Create credentials dictionary for authenticator
credentials = {
    #'usernames': {name: users[name]['password'] for name in users.keys()}, # Dictionary of usernames and hashed passwords
    'usernames': {name: users[name]['password'] for name in users},
    'names': {name: name for name in users.keys()},  # Optional, can be the same as usernames
    # 'emails': {name: users[name]['email'] for name in users.keys()}  # Optional, include if emails are used
}

st.write("Credentials:", credentials)

# Initialize authenticator
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name='vaxart_cookie',
    key='KxvlOKPEhd-JeEqBOkvjiw',
    cookie_expiry_days=30
)
# Display login form
name, authentication_status, username = authenticator.login('Login', 'main')
st.write("Authentication Status:", authentication_status)

if authentication_status:
    st.write(f'Welcome *{name}*')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

    # Password change form
    with st.form("change_password"):
        st.write("Change Password")
        old_password = st.text_input("Enter your old password", type="password")
        new_password = st.text_input("Enter a new password", type="password")
        confirm_password = st.text_input("Confirm new password", type="password")
        submit_button = st.form_submit_button("Change Password")

        if submit_button:
            # Verify old password using bcrypt
            old_password_hashed = users[name]['password'].encode()
            if bcrypt.checkpw(old_password.encode(), old_password_hashed):
                # Check if new passwords match
                if new_password == confirm_password:
                    # Update password
                    users[name]['password'] = stauth.Hasher([new_password]).generate()[0]  # Hash new password
                    save_users(users)
                    st.success("Password changed successfully!")
                else:
                    st.error("New passwords do not match.")
            else:
                st.error("The old password you entered is incorrect.")

elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

if st.button('Logout', key='logout_button'):
    authenticator.logout('Logout', 'main')