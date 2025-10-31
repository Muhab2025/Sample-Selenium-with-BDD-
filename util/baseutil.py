from datetime import datetime


def generate_email_with_timestamp():
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "myname"+timestamp+"@gmail.com"