import ssl
from email.message import EmailMessage
import smtplib

def email_sender(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'receiver' in request.args and 'subject' in request.args and 'message' in request.args:
        # Define email sender and receiver
        email_sender = 'Sender Email Address'     # need to be replaced
        email_password = 'Gmail App Passwords'    # need to be replaced
        email_receiver = request.args.get('receiver')

        # Set the subject and body of the email
        subject = request.args.get('subject')
        body = request.args.get('message')

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        return "Email has been sent!"
    elif request_json and 'receiver' in request_json:
        return request_json
    else:
        return f'Hello World!'