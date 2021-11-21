import os
from tinderbotz.session import Session

if __name__ == "__main__":
    session = Session()                             # Instance of the Session Class

    email = os.getenv('GMAIL_USER')                 # Create a variable for Gmail username
    password = os.getenv('GMAIL_PASS')              # Create a variable for Gmail password
    
    session.login_using_google(email, password)     # I chose to log in using Gmail

    session.like(amount=25, ratio="84.5%", sleep=3) # Edit amount (i.e., the number of times you want to swipe right), ratio (i.e, percentage chance of attempting a right swipe), and sleep (i.e., the number of seconds to wait between swipes)
