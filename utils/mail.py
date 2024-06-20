# # from email.message import EmailMessage
# # from email.mime.base import MIMEBase
# # from email import encoders
# # import ssl
# # import smtplib

# # # Your code to use smtplib goes here



# # def send_email(): 
# #     # Define email sender and receiver
# #     email_sender = 'saravan2406@gmail.com'
# #     #email_password = os.environ.get("EMAIL_PASSWORD")
# #     email_password = 'utefbkprwxtdanvc'
# #     email_receiver = 'saravanan@proliteautomation.com','sureshgopi@proliteautomation.com'
# #     email_receiver2 = 'saravanan@proliteautomation.com'

# #     # Set the subject and body of the email
# #     subject = 'Urgent : Data Logger Connection Error!!!'
# #     body = """<style>
# #     body {
# #         font-family: Arial, sans-serif;
# #         background-color: #f4f4f4;
# #         margin: 0;
# #         padding: 20px;
# #     }
# #     .notice-container {
# #         background-color: #fff;
# #         border: 1px solid #ccc;
# #         padding: 20px;
# #         border-radius: 5px;
# #         box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
# #         max-width: 600px;
# #         margin: auto;
# #     }
# #     .notice-container p {
# #         margin: 0 0 10px;
# #     }
# #     .notice-container b {
# #         color: #d9534f;
# #     }
# # </style>

# # <div class="notice-container">
# #     <p><b>Urgent Notice:</b> Our records indicate that your data logger connection has been disrupted.<br>
# #     Please take immediate action to restore the connection to prevent any potential data loss.<br>
# #     Your prompt attention to this matter is greatly appreciated.</p><br>
# #     <p><b>Note:</b> Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
# #     If you require assistance or have any questions, please contact our support team directly.</p>
# # </div>
# # """
    
# #     # Define the HTML content
# #     html_content = """
# #     <!DOCTYPE html>
# #     <html lang="en">
# #     <head>
# #         <meta charset="UTF-8">
# #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
# #         <title>Urgent Notice</title>
# #         <style>
# #             body {
# #                 font-family: Arial, sans-serif;
# #                 background-color: #f4f4f4;
# #                 margin: 0;
# #                 padding: 0;
# #             }
# #             .container {
# #                 background-color: #ffffff;
# #                 padding: 20px;
# #                 border-radius: 8px;
# #                 box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
# #                 max-width: 600px;
# #                 margin: 40px auto;
# #                 border-top: 6px solid #d9534f;
# #             }
# #             .header {
# #                 font-size: 24px;
# #                 font-weight: bold;
# #                 color: #d9534f;
# #                 margin-bottom: 20px;
# #             }
# #             .content {
# #                 font-size: 16px;
# #                 color: #333333;
# #                 line-height: 1.6;
# #             }
# #             .content b {
# #                 color: #d9534f;
# #             }
# #             .footer {
# #                 font-size: 14px;
# #                 color: #777777;
# #                 margin-top: 20px;
# #             }
# #             .footer a {
# #                 color: #d9534f;
# #                 text-decoration: none;
# #             }
# #         </style>
# #     </head>
# #     <body>
# #         <div class="container">
# #             <div class="header">Urgent Notice</div>
# #             <div class="content">
# #                 <p>Our records indicate that your data logger connection has been disrupted.<br>
# #                 Please take immediate action to restore the connection to prevent any potential data loss.<br>
# #                 Your prompt attention to this matter is greatly appreciated.</p><br>
# #                 <p>Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
# #                 If you require assistance or have any questions, please mail to :<a href> support@proliteautomation.com</a> contact our support team directly.</p>
# #             </div>
# #             <div class="footer">
# #                 <p>Thank you,<br>
# #                 The Support Team</p>
# #             </div>
# #         </div>
# #     </body>
# #     </html>
# #     """
    
# #     em = EmailMessage()
# #     em['From'] = email_sender
# #     em['To'] = email_receiver
# #     #em['Cc'] = email_receiver2
# #     em['Subject'] = subject
# #     em.set_content(html_content, subtype='html')
# #     #em.set_content(body)
# #     # Make the message multipart
# #     #em.add_alternative(body, subtype='html')
# #     """
# #     # Attach the image file
# #     with open('plcimage.jpg', 'rb') as attachment_file:
# #         file_data = attachment_file.read()
# #         file_name = attachment_file.name.split("/")[-1]
# #     attachment = MIMEBase('application', 'octet-stream')
# #     attachment.set_payload(file_data)
# #     encoders.encode_base64(attachment)
# #     attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
# #     em.attach(attachment)
# #     """
# #     # Add SSL (layer of security)
# #     context = ssl.create_default_context()
# #     # Log in and send the email
# #     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
# #         smtp.login(email_sender, email_password)
# #         smtp.sendmail(email_sender, email_receiver, em.as_string())


# import os
# import smtplib
# import ssl
# from email.message import EmailMessage
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email import encoders

# def send_email(): 
#     # Define email sender and receiver
#     email_sender = 'saravan2406@gmail.com'
#     #email_password = os.environ.get("EMAIL_PASSWORD")
#     email_password = 'utefbkprwxtdanvc'
#     email_receiver = ['saravanan@proliteautomation.com', 'sureshgopi@proliteautomation.com']
#     email_receiver2 = 'saravanan@proliteautomation.com'

#     # Set the subject and body of the email
#     subject = 'Urgent : Data Logger Connection Error!!!'

#     # Path to the uploaded image
#     image_path = 'C:\\Users\\Acer\\Desktop\\skew\\SKEW\\Icons\\Logo_mixed_colour_sample1-removebg-preview.png'
#     with open(image_path, 'rb') as image_file:
#         img_data = image_file.read()

#     # Define the HTML content
#     html_content = """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Urgent Notice</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background-color: #f4f4f4;
#                 margin: 0;
#                 padding: 0;
#             }
#             .container {
#                 background-color: #ffffff;
#                 padding: 20px;
#                 border-radius: 8px;
#                 box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#                 max-width: 600px;
#                 margin: 40px auto;
#                 border-top: 6px solid #d9534f;
#                 text-align: center; /* Center the content */
#             }
#             .header {
#                 font-size: 24px;
#                 font-weight: bold;
#                 color: #d9534f;
#                 margin-bottom: 20px;
#             }
#             .content {
#                 font-size: 16px;
#                 color: #333333;
#                 line-height: 1.6;
#                 text-align: left; /* Align content to the left */
#             }
#             .content b {
#                 color: #d9534f;
#             }
#             .footer {
#                 font-size: 14px;
#                 color: #777777;
#                 margin-top: 20px;
#             }
#             .footer a {
#                 color: #d9534f;
#                 text-decoration: none;
#             }
#             .logo {
#                 display: block;
#                 margin: 0 auto 10px;
#             }
#             .logo-text {
#                 font-size: 20px;
#                 font-weight: bold;
#                 color: #d9534f;
#             }
#         </style>
#     </head>
#     <body>
#         <div class="container">
#             <img src="cid:logo" alt="Logo" class="logo">
#             <div class="logo-text">SKEW</div>
#             <div class="header">Urgent Notice</div>
#             <div class="content">
#                 <p>Our records indicate that your data logger connection has been disrupted.<br>
#                 Please take immediate action to restore the connection to prevent any potential data loss.<br>
#                 Your prompt attention to this matter is greatly appreciated.</p><br>
#                 <p>Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
#                 If you require assistance or have any questions, please mail to: <a href="mailto:support@proliteautomation.com">support@proliteautomation.com</a> contact our support team directly.</p>
#             </div>
#             <div class="footer">
#                 <p>Thank you,<br>
#                 The Support Team<br>
#                 Software Name</p>
#             </div>
#         </div>
#     </body>
#     </html>

#     """

#     # Create the root message and fill in the from, to, and subject headers
#     msg = MIMEMultipart('related')
#     msg['From'] = email_sender
#     msg['To'] = ", ".join(email_receiver)
#     msg['Subject'] = subject

#     # Attach the HTML content to the email
#     msg_alternative = MIMEMultipart('alternative')
#     msg.attach(msg_alternative)
#     msg_alternative.attach(MIMEText(html_content, 'html'))

#     # Attach the image
#     image_part = MIMEImage(img_data, name=os.path.basename(image_path))
#     image_part.add_header('Content-ID', '<logo>')
#     msg.attach(image_part)

#     # Add SSL (layer of security)
#     context = ssl.create_default_context()
#     # Log in and send the email
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(email_sender, email_password)
#         smtp.sendmail(email_sender, email_receiver, msg.as_string())

import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders

def send_email(): 
    # Define email sender and receiver
    email_sender = 'saravan2406@gmail.com'
    email_password = 'utefbkprwxtdanvc'
    email_receiver = ['saravanan@proliteautomation.com', 'sureshgopi@proliteautomation.com']

    # Set the subject and body of the email
    subject = 'Urgent : Data Logger Connection Error!!!'

    # Path to the uploaded image
    image_path = 'C:\\Users\\Acer\\Desktop\\skew\\SKEW\\Icons\\Logo_mixed_colour_sample1-removebg-preview.png'
    with open(image_path, 'rb') as image_file:
        img_data = image_file.read()

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
                text-align: center; /* Center the content */
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
                text-align: left; /* Align content to the left */
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
            .logo {
                display: block;
                margin: 0 auto 10px;
            }
            .logo-text {
                font-size: 20px;
                font-weight: bold;
                color: #d9534f;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="cid:logo" alt="Logo" class="logo" style="width: 150px;">
            <div class="logo-text">SKEW</div>
            <div class="header">Urgent Notice</div>
            <div class="content">
                <p>Our records indicate that your data logger connection has been disrupted.<br>
                Please take immediate action to restore the connection to prevent any potential data loss.<br>
                Your prompt attention to this matter is greatly appreciated.</p><br>
                <p>Please note that this email is sent from an automated system, and replies to this message will not be monitored.<br>
                If you require assistance or have any questions, please mail to: <a href="mailto:support@proliteautomation.com">support@proliteautomation.com</a> contact our support team directly.</p>
            </div>
            <div class="footer">
                <p>Thank you,<br>
                The Support Team<br>
                SKEW </p>
            </div>
        </div>
    </body>
    </html>
    """

    # Create the root message and fill in the from, to, and subject headers
    msg = MIMEMultipart('related')
    msg['From'] = email_sender
    msg['To'] = ", ".join(email_receiver)
    msg['Subject'] = subject

    # Attach the HTML content to the email
    msg_alternative = MIMEMultipart('alternative')
    msg.attach(msg_alternative)
    msg_alternative.attach(MIMEText(html_content, 'html'))

    # Attach the image
    image_part = MIMEImage(img_data, name=os.path.basename(image_path))
    image_part.add_header('Content-ID', '<logo>')
    msg.attach(image_part)

    # Add SSL (layer of security)
    context = ssl.create_default_context()
    
    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())


