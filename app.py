# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'GenghisKhan' and password == '1227':   
        account_sid = 'ACd7a685a77e661028056126dfc220ffd9'
        auth_token = 'c15563aacfd048892d0909014b113ca4'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VAae31a8dc627e1e43786ee798caec0b66') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'ACd7a685a77e661028056126dfc220ffd9'
    auth_token = 'c15563aacfd048892d0909014b113ca4'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('VAae31a8dc627e1e43786ee798caec0b66') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://chinesegoogledocs.onrender.com/")


if __name__ == "__main__":
    app.run()

