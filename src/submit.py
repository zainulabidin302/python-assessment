import requests
import sys
import re   
import os
import base64

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
def validate_email(email):   
    return re.search(regex,email)

REMOTE_HOST="http://localhost:5000/"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 submit.py [email]")
        sys.exit(1)

    email_address = sys.argv[1]    
    if not validate_email(email_address):
        print("Invalid email address")
        sys.exit(1)
    try:
        payload = {
            'email_address': email_address
        }
        for file_name in ['python_basics.py', 'sql_basics.py']:
            with open('src/' + file_name, 'rb') as f:
                payload[file_name] = base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        print('error', e)
        sys.exit(1)
    try:
        result = requests.post(
            REMOTE_HOST + "/submit",
            json=payload,
        )
        print(result.json())
    except Exception as e:
        print("Failed to submit code: {}".format(e))
        print("Please contact hello@techlev.dev")
        sys.exit(1)