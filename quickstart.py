from tinderbotz.session import Session

if __name__ == "__main__":
    session = Session()                             # Instance of the Session Class
    session.like(amount=25, ratio="84.5%", sleep=3) # Edit amount (i.e., the number of times you want to swipe right), ratio (i.e, percentage chance of attempting a right swipe), and sleep (i.e., the number of seconds to wait between swipes)
