from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import ssl
import smtplib

# Your code to use smtplib goes here



def send_email(): 
    # Define email sender and receiver
    email_sender = 'saravan2406@gmail.com'
    #email_password = os.environ.get("EMAIL_PASSWORD")
    email_password = 'utefbkprwxtdanvc'
    email_receiver = 'saravanan@proliteautomation.com','sureshgopi@proliteautomation.com'
    email_receiver2 = 'saravanan@proliteautomation.com'

    # Set the subject and body of the email
    subject = 'Urgent : Data Logger Connection Error!!!'
    body = """<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        margin: 0;
        padding: 20px;
    }
    .notice-container {
        background-color: #fff;
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: auto;
    }
    .notice-container p {
        margin: 0 0 10px;
    }
    .notice-container b {
        color: #d9534f;
    }
</style>

<div class="notice-container">
    <p><b>Urgent Notice:</b> Our records indicate that your data logger connection has been disrupted.<br>
    Please take immediate action to restore the connection to prevent any potential data loss.<br>
    Your prompt attention to this matter is greatly appreciated.</p><br>
    <p><b>Note:</b> Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
    If you require assistance or have any questions, please contact our support team directly.</p>
</div>
"""
    
    # Define the HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Urgent Notice</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                max-width: 600px;
                margin: 40px auto;
                border-top: 6px solid #d9534f;
            }
            .header {
                font-size: 24px;
                font-weight: bold;
                color: #d9534f;
                margin-bottom: 20px;
            }
            .content {
                font-size: 16px;
                color: #333333;
                line-height: 1.6;
            }
            .content b {
                color: #d9534f;
            }
            .footer {
                font-size: 14px;
                color: #777777;
                margin-top: 20px;
            }
            .footer a {
                color: #d9534f;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">Urgent Notice</div>
            <div class="content">
                <p>Our records indicate that your data logger connection has been disrupted.<br>
                Please take immediate action to restore the connection to prevent any potential data loss.<br>
                Your prompt attention to this matter is greatly appreciated.</p><br>
                <p>Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
                If you require assistance or have any questions, please mail to :<a href> support@proliteautomation.com</a> contact our support team directly.</p>
            </div>
            <div class="footer">
                <p>Thank you,<br>
                The Support Team</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    #em['Cc'] = email_receiver2
    em['Subject'] = subject
    em.set_content(html_content, subtype='html')
    #em.set_content(body)
    # Make the message multipart
    #em.add_alternative(body, subtype='html')
    """
    # Attach the image file
    with open('plcimage.jpg', 'rb') as attachment_file:
        file_data = attachment_file.read()
        file_name = attachment_file.name.split("/")[-1]
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file_data)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
    em.attach(attachment)
    """
    # Add SSL (layer of security)
    context = ssl.create_default_context()
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
