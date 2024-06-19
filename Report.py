# # # # from datetime import datetime
# # # # import pandas as pd
# # # # from sqlalchemy import create_engine
# # # # import pdfkit
# # # # from jinja2 import Template
# # # # import os

# # # # # Sample data (replace with your actual data)
# # # # company_name = "Your Company"
# # # # logo_path = "C:\\prolite\\Skew_app\\logos-removebg-preview.png"# Adjust to the local path of your logo file
# # # # from_date = "2024-05-10 16:22:12"
# # # # to_date = "2024-05-10 16:22:17"
# # # # printed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # # # # Fetch data from the database
# # # # engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
# # # # con = engine.connect()

# # # # query = "SELECT TOP 100 * FROM plc_data"
# # # # df = pd.read_sql(query, con)

# # # # # HTML template
# # # # html_template = '''
# # # # <!DOCTYPE html>
# # # # <html>
# # # # <head>
# # # #     <meta charset="UTF-8">
# # # #     <title>Report</title>
# # # #     <style>
# # # #         body {
# # # #             font-family: Arial, sans-serif;
# # # #             margin: 40px;
# # # #         }
# # # #         .header {
# # # #             overflow: hidden;
# # # #         }
# # # #         .logo {
# # # #             max-width: 150px;
# # # #             max-height: 150px;
# # # #             width: auto;
# # # #             height: auto;
# # # #             float: left;
# # # #         }
# # # #         .header-content {
# # # #             margin-left: 170px;  /* Adjust according to logo width */
# # # #         }
# # # #         .company-name {
# # # #             text-align: center;
# # # #         }
# # # #         .date-range {
# # # #             text-align: center;
# # # #         }
# # # #         .printed-date {
# # # #             text-align: right;
# # # #         }
# # # #         table {
# # # #             width: 100%;
# # # #             border-collapse: collapse;
# # # #             margin: 20px 0;
# # # #         }
# # # #         table, th, td {
# # # #             border: 1px solid black;
# # # #         }
# # # #         th, td {
# # # #             padding: 10px;
# # # #             text-align: left;
# # # #         }
# # # #     </style>
# # # # </head>
# # # # <body>
# # # #     <div class="header">
# # # #         <img class="logo" src="{{ logo_path }}" alt="Company Logo">
# # # #         <div class="header-content">
# # # #             <h1 class="company-name">{{ company_name }}</h1>
# # # #             <p class="date-range">From: {{ from_date }} | To: {{ to_date }}</p>
# # # #             <p class="printed-date">Report generated on: {{ printed_date }}</p>
# # # #         </div>
# # # #     </div>
# # # #     <h1>Report Title</h1>
# # # #     <table>
# # # #         <thead>
# # # #             <tr>
# # # #                 {% for column in columns %}
# # # #                 <th>{{ column }}</th>
# # # #                 {% endfor %}
# # # #             </tr>
# # # #         </thead>
# # # #         <tbody>
# # # #             {% for row in data %}
# # # #             <tr>
# # # #                 {% for item in row %}
# # # #                 <td>{{ item }}</td>
# # # #                 {% endfor %}
# # # #             </tr>
# # # #             {% endfor %}
# # # #         </tbody>
# # # #     </table>
# # # # </body>
# # # # </html>
# # # # '''

# # # # # Render HTML with data
# # # # template = Template(html_template)
# # # # html_report = template.render(
# # # #     logo_path=logo_path,
# # # #     company_name=company_name,
# # # #     from_date=from_date,
# # # #     to_date=to_date,
# # # #     printed_date=printed_date,
# # # #     columns=df.columns,
# # # #     data=df.values.tolist()  # Convert DataFrame to list of lists for Jinja2
# # # # )

# # # # # Save HTML to file
# # # # with open('report.html', 'w') as file:
# # # #     file.write(html_report)

# # # # # Convert HTML to PDF
# # # # pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Replace with your wkhtmltopdf path
# # # # pdfkit.from_file('report.html', 'report.pdf', configuration=pdfkit_config)

# # # # print("Report generated and saved as PDF.")
# # # from datetime import datetime
# # # import pandas as pd
# # # from sqlalchemy import create_engine
# # # import pdfkit
# # # from jinja2 import Template
# # # import os
# # # import base64

# # # # Sample data (replace with your actual data)
# # # company_name = "Your Company"
# # # logo_path = "C:\\prolite\\Skew_app\\logos-removebg-preview.png"  # Adjust to the local path of your logo file
# # # from_date = "2024-05-10 16:22:12"
# # # to_date = "2024-05-10 16:22:17"
# # # printed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # # # Encode logo in base64
# # # with open(logo_path, "rb") as image_file:
# # #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
# # #     encoded_logo = f"data:image/png;base64,{encoded_string}"

# # # # Fetch data from the database
# # # engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
# # # con = engine.connect()

# # # query = "SELECT TOP 100 * FROM plc_data"
# # # df = pd.read_sql(query, con)

# # # # HTML template
# # # html_template = '''
# # # <!DOCTYPE html>
# # # <html>
# # # <head>
# # #     <meta charset="UTF-8">
# # #     <title>Report</title>
# # #     <style>
# # #         body {
# # #             font-family: Arial, sans-serif;
# # #             margin: 40px;
# # #         }
# # #         .header {
# # #             overflow: hidden;
# # #         }
# # #         .logo {
# # #             max-width: 150px;
# # #             max-height: 150px;
# # #             width: auto;
# # #             height: auto;
# # #             float: left;
# # #         }
# # #         .header-content {
# # #             margin-left: 170px;  /* Adjust according to logo width */
# # #         }
# # #         .company-name {
# # #             text-align: center;
# # #         }
# # #         .date-range {
# # #             text-align: center;
# # #         }
# # #         .printed-date {
# # #             text-align: right;
# # #         }
# # #         table {
# # #             width: 100%;
# # #             border-collapse: collapse;
# # #             margin: 20px 0;
# # #         }
# # #         table, th, td {
# # #             border: 1px solid black;
# # #         }
# # #         th, td {
# # #             padding: 10px;
# # #             text-align: left;
# # #         }
# # #     </style>
# # # </head>
# # # <body>
# # #     <div class="header">
# # #         <img class="logo" src="{{ encoded_logo }}" alt="Company Logo">
# # #         <div class="header-content">
# # #             <h1 class="company-name">{{ company_name }}</h1>
# # #             <p class="date-range">From: {{ from_date }} | To: {{ to_date }}</p>
# # #             <p class="printed-date">Report generated on: {{ printed_date }}</p>
# # #         </div>
# # #     </div>
# # #     <h1>Report Title</h1>
# # #     <table>
# # #         <thead>
# # #             <tr>
# # #                 {% for column in columns %}
# # #                 <th>{{ column }}</th>
# # #                 {% endfor %}
# # #             </tr>
# # #         </thead>
# # #         <tbody>
# # #             {% for row in data %}
# # #             <tr>
# # #                 {% for item in row %}
# # #                 <td>{{ item }}</td>
# # #                 {% endfor %}
# # #             </tr>
# # #             {% endfor %}
# # #         </tbody>
# # #     </table>
# # # </body>
# # # </html>
# # # '''

# # # # Render HTML with data
# # # template = Template(html_template)
# # # html_report = template.render(
# # #     encoded_logo=encoded_logo,
# # #     company_name=company_name,
# # #     from_date=from_date,
# # #     to_date=to_date,
# # #     printed_date=printed_date,
# # #     columns=df.columns,
# # #     data=df.values.tolist()  # Convert DataFrame to list of lists for Jinja2
# # # )

# # # # Save HTML to file
# # # with open('report.html', 'w') as file:
# # #     file.write(html_report)

# # # # Convert HTML to PDF
# # # pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Replace with your wkhtmltopdf path
# # # pdfkit.from_file('report.html', 'report.pdf', configuration=pdfkit_config)

# # # print("Report generated and saved as PDF.")

# # # from datetime import datetime
# # # import pandas as pd
# # # from sqlalchemy import create_engine
# # # import pdfkit
# # # from jinja2 import Template
# # # import os
# # # import base64

# # # # Sample data (replace with your actual data)
# # # company_name = "Your Company"
# # # logo_path = "C:\\prolite\\Skew_app\\logos-removebg-preview.png"  # Adjust to the local path of your logo file
# # # from_date = "2024-05-10 16:22:12"
# # # to_date = "2024-05-10 16:22:17"
# # # printed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # # # Encode logo in base64
# # # with open(logo_path, "rb") as image_file:
# # #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
# # #     encoded_logo = f"data:image/png;base64,{encoded_string}"

# # # # Fetch data from the database
# # # engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
# # # con = engine.connect()

# # # query = "SELECT TOP 100 * FROM plc_data"
# # # df = pd.read_sql(query, con)

# # # # HTML template
# # # html_template = '''
# # # <!DOCTYPE html>
# # # <html>
# # # <head>
# # #     <meta charset="UTF-8">
# # #     <title>Report</title>
# # #     <style>
# # #         body {
# # #             font-family: Arial, sans-serif;
# # #             margin: 40px;
# # #         }
# # #         .header {
# # #             margin-bottom: 20px;
# # #             overflow: hidden;
# # #         }
# # #         .logo {
# # #             max-width: 150px;
# # #             max-height: 150px;
# # #             width: auto;
# # #             height: auto;
# # #             float: left;
# # #         }
# # #         .header-content {
# # #             text-align: center;
# # #             margin-left: 170px; /* Adjust according to logo width */
# # #         }
# # #         .printed-date {
# # #             text-align: right;
# # #         }
# # #         .report-title {
# # #             text-align: center;
# # #             margin-top: 20px;
# # #         }
# # #         table {
# # #             width: 100%;
# # #             border-collapse: collapse;
# # #             margin-top: 20px;
# # #         }
# # #         table, th, td {
# # #             border: 1px solid black;
# # #         }
# # #         th, td {
# # #             padding: 10px;
# # #             text-align: left;
# # #         }
# # #     </style>
# # # </head>
# # # <body>
# # #     <div class="header">
# # #         <img class="logo" src="{{ encoded_logo }}" alt="Company Logo">
# # #         <div class="header-content">
# # #             <h1 class="company-name">{{ company_name }}</h1>
# # #             <p class="date-range">From: {{ from_date }} | To: {{ to_date }}</p>
# # #         </div>
# # #         <div class="printed-date">
# # #             <p>Report generated on: {{ printed_date }}</p>
# # #         </div>
# # #     </div>
# # #     <h1 class="report-title">Report Title</h1>
# # #     <table>
# # #         <thead>
# # #             <tr>
# # #                 {% for column in columns %}
# # #                 <th>{{ column }}</th>
# # #                 {% endfor %}
# # #             </tr>
# # #         </thead>
# # #         <tbody>
# # #             {% for row in data %}
# # #             <tr>
# # #                 {% for item in row %}
# # #                 <td>{{ item }}</td>
# # #                 {% endfor %}
# # #             </tr>
# # #             {% endfor %}
# # #         </tbody>
# # #     </table>
# # # </body>
# # # </html>
# # # '''

# # # # Render HTML with data
# # # template = Template(html_template)
# # # html_report = template.render(
# # #     encoded_logo=encoded_logo,
# # #     company_name=company_name,
# # #     from_date=from_date,
# # #     to_date=to_date,
# # #     printed_date=printed_date,
# # #     columns=df.columns,
# # #     data=df.values.tolist()  # Convert DataFrame to list of lists for Jinja2
# # # )

# # # # Save HTML to file
# # # with open('report.html', 'w') as file:
# # #     file.write(html_report)

# # # # Convert HTML to PDF
# # # pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Replace with your wkhtmltopdf path
# # # pdfkit.from_file('report.html', 'report.pdf', configuration=pdfkit_config)

# # # print("Report generated and saved as PDF.")

# # from datetime import datetime
# # import pandas as pd
# # from sqlalchemy import create_engine
# # import pdfkit
# # from jinja2 import Template
# # import os
# # import base64

# # # Sample data (replace with your actual data)
# # company_name = "Your Company"
# # logo_path = "C:\\prolite\\Skew_app\\logos-removebg-preview.png"  # Adjust to the local path of your logo file
# # from_date = "2024-05-10 16:22:12"
# # to_date = "2024-05-10 16:22:17"
# # printed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # # Encode logo in base64
# # with open(logo_path, "rb") as image_file:
# #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
# #     encoded_logo = f"data:image/png;base64,{encoded_string}"

# # # Fetch data from the database
# # engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
# # con = engine.connect()

# # query = "SELECT TOP 100 * FROM plc_data"
# # df = pd.read_sql(query, con)

# # # HTML template
# # html_template = '''
# # <!DOCTYPE html>
# # <html>
# # <head>
# #     <meta charset="UTF-8">
# #     <title>Report</title>
# #     <style>
# #         /* General styling for the report */
# #         body {
# #             font-family: Arial, sans-serif;
# #             margin: 20px;
# #         }

# #         h1, h2, h3 {
# #             text-align: center;
# #             margin: 0;
# #             padding: 10px 0;
# #         }

# #         /* Header section */
# #         .header {
# #             text-align: center;
# #             margin-bottom: 20px;
# #         }

# #         .header .company-name,
# #         .header .report-title {
# #             font-size: 20px;
# #             font-weight: bold;
# #         }

# #         .header .date-range,
# #         .header .generated-date {
# #             font-size: 14px;
# #             margin: 5px 0;
# #         }

# #         /* Table styling */
# #         table {
# #             width: 100%;
# #             border-collapse: collapse;
# #             margin-top: 20px;
# #         }

# #         th, td {
# #             border: 1px solid #000;
# #             padding: 8px;
# #             text-align: left;
# #         }

# #         th {
# #             background-color: #f2f2f2;
# #         }

# #         /* Aligning timestamp and other data */
# #         .date-range,
# #         .generated-date {
# #             display: inline-block;
# #             width: 45%;
# #             text-align: left;
# #         }

# #         /* Ensuring no content overflow */
# #         th, td {
# #             white-space: nowrap;
# #         }

# #         /* Specific styling for each data column */
# #         td.id {
# #             width: 10%;
# #         }

# #         td.timestamp {
# #             width: 20%;
# #         }

# #         td.name {
# #             width: 20%;
# #         }

# #         td.datatype {
# #             width: 10%;
# #         }

# #         td.value {
# #             width: 10%;
# #         }

# #     </style>
# # </head>
# # <body>
# #     <div class="header">
# #         <img class="logo" src="{{ encoded_logo }}" alt="Company Logo">
# #         <div class="header-content">
# #             <h1 class="company-name">{{ company_name }}</h1>
# #             <p class="date-range">From: {{ from_date }} | To: {{ to_date }}</p>
# #             <p class="printed-date">Report generated on: {{ printed_date }}</p>
# #         </div>
# #     </div>
# #     <h1 class="report-title">Report Title</h1>
# #     <table>
# #         <thead>
# #             <tr>
# #                 {% for column in columns %}
# #                 <th>{{ column }}</th>
# #                 {% endfor %}
# #             </tr>
# #         </thead>
# #         <tbody>
# #             {% for row in data %}
# #             <tr>
# #                 {% for item in row %}
# #                 <td>{{ item }}</td>
# #                 {% endfor %}
# #             </tr>
# #             {% endfor %}
# #         </tbody>
# #     </table>
# # </body>
# # </html>
# # '''

# # # Render HTML with data
# # template = Template(html_template)
# # html_report = template.render(
# #     encoded_logo=encoded_logo,
# #     company_name=company_name,
# #     from_date=from_date,
# #     to_date=to_date,
# #     printed_date=printed_date,
# #     columns=df.columns,
# #     data=df.values.tolist()  # Convert DataFrame to list of lists for Jinja2
# # )

# # # Save HTML to file
# # with open('report.html', 'w') as file:
# #     file.write(html_report)

# # # Convert HTML to PDF
# # pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Replace with your wkhtmltopdf path
# # pdfkit.from_file('report.html', 'report.pdf', configuration=pdfkit_config)

# # print("Report generated and saved as PDF.")


# from datetime import datetime
# import pandas as pd
# from sqlalchemy import create_engine
# import pdfkit
# from jinja2 import Template
# import os
# import base64

# # Sample data (replace with your actual data)
# company_name = "Your Company"
# logo_path = "C:\\prolite\\Skew_app\\logos-removebg-preview.png"  # Adjust to the local path of your logo file
# from_date = "2024-05-10 16:22:12"
# to_date = "2024-05-10 16:22:17"
# printed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # Encode logo in base64
# with open(logo_path, "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
#     encoded_logo = f"data:image/png;base64,{encoded_string}"

# # Fetch data from the database
# engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
# con = engine.connect()

# query = "SELECT TOP 100 * FROM plc_data"
# df = pd.read_sql(query, con)

# # HTML template
# html_template = '''
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Report</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             margin: 40px;
#         }
#         .header {
#             margin-bottom: 20px;
#             overflow: hidden;
#         }
#         .logo {
#             max-width: 150px;
#             max-height: 150px;
#             width: auto;
#             height: auto;
#             float: left;
#         }
#         .header-content {
#             text-align: center;
#             margin-left: 170px; /* Adjust according to logo width */
#         }
#         .printed-date-container {
#             overflow: hidden;
#             margin-top: 20px;
#         }
#         .printed-date {
#             text-align: right;
#             float: right;
#             font-size: 12px;
#             font-family: Arial, sans-serif;
#         }
#         .report-title {
#             text-align: center;
#             margin-top: 20px;
#         }
#         table {
#             width: 100%;
#             border-collapse: collapse;
#             margin-top: 20px;
#         }
#         table, th, td {
#             border: 1px solid black;
#         }
#         th, td {
#             padding: 10px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <div class="header">
#         <img class="logo" src="{{ encoded_logo }}" alt="Company Logo">
#         <div class="header-content">
#             <h1 class="company-name">{{ company_name }}</h1>
#             <p class="date-range">From: {{ from_date }} | To: {{ to_date }}</p>
#         </div>
#     </div>
#     <div class="printed-date-container">
#         <p class="printed-date">Report generated on: {{ printed_date }}</p>
#     </div>
#     <h1 class="report-title">Report Title</h1>
#     <table>
#         <thead>
#             <tr>
#                 {% for column in columns %}
#                 <th>{{ column }}</th>
#                 {% endfor %}
#             </tr>
#         </thead>
#         <tbody>
#             {% for row in data %}
#             <tr>
#                 {% for item in row %}
#                 <td>{{ item }}</td>
#                 {% endfor %}
#             </tr>
#             {% endfor %}
#         </tbody>
#     </table>
# </body>
# </html>
# '''

# # Render HTML with data
# template = Template(html_template)
# html_report = template.render(
#     encoded_logo=encoded_logo,
#     company_name=company_name,
#     from_date=from_date,
#     to_date=to_date,
#     printed_date=printed_date,
#     columns=df.columns,
#     data=df.values.tolist()  # Convert DataFrame to list of lists for Jinja2
# )

# # Save HTML to file
# with open('report.html', 'w') as file:
#     file.write(html_report)

# # Convert HTML to PDF
# pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Replace with your wkhtmltopdf path
# pdfkit.from_file('report.html', 'report.pdf', configuration=pdfkit_config)

# print("Report generated and saved as PDF.")


from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import pdfkit
from jinja2 import Template
import base64

# Sample data (replace with your actual data)
company_name = "PROLITE AUTOMATION"
logo_path = "C:\prolite\Skew_app\logo.png"  # Adjust to the local path of your logo file
from_date = "2024-05-10 16:22:12"
to_date = "2024-05-10 16:22:17"
printed_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Encode logo in base64
with open(logo_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    encoded_logo = f"data:image/png;base64,{encoded_string}"

# Fetch data from the database
engine = create_engine('mssql+pyodbc://SURESHGOPI/PLCDB2?driver=SQL+Server')
con = engine.connect()

query = "SELECT TOP 100 * FROM plc_data"
df = pd.read_sql(query, con)

# HTML template
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
            position: relative;
        }
        .logo {
            max-width: 150px;
            max-height: 150px;
            width: auto;
            height: auto;
        }
        .company-name {
            margin: 10px 0;
            font-size: 18px; /* Decreased font size */
        }
        .date-range {
            text-align: left;
            position: absolute;
            left: 0;
            bottom: 0;
            margin-top: 20px;
        }
        .from-date,
        .to-date {
            margin: 5px 0;
        }
        .printed-date-container {
            text-align: right;
            margin-top: -20px; /* Adjust to align with header */
        }
        .printed-date {
            font-size: 12px;
            font-family: Arial, sans-serif;
        }
        .report-title {
            text-align: center;
            margin-top: 20px;
            font-size: 24px; /* Decreased font size */
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="header">
        <img class="logo" src="{{ encoded_logo }}" alt="Company Logo">
        <h1 class="company-name">{{ company_name }}</h1>
        <div class="date-range">
            <p class="from-date">From: {{ from_date }}</p>
            <p class="to-date">To: {{ to_date }}</p>
        </div>
    </div>
    <div class="printed-date-container">
        <p class="printed-date">Report generated on: {{ printed_date }}</p>
    </div>
    <h1 class="report-title">Data From PLC S7-1200</h1>
    <table>
        <thead>
            <tr>
                {% for column in columns %}
                <th>{{ column }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in data %}
            <tr>
                {% for item in row %}
                <td>{{ item }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
'''

# Render HTML with data
template = Template(html_template)
html_report = template.render(
    encoded_logo=encoded_logo,
    company_name=company_name,
    from_date=from_date,
    to_date=to_date,
    printed_date=printed_date,
    columns=df.columns,
    data=df.values.tolist()  # Convert DataFrame to list of lists for Jinja2
)

# Save HTML to file
html_file_path = 'report.html'
pdf_file_path = 'report.pdf'

try:
    with open(html_file_path, 'w') as file:
        file.write(html_report)
    print(f"HTML report generated and saved as {html_file_path}")

    # Convert HTML to PDF
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Replace with your wkhtmltopdf path
    pdfkit.from_file(html_file_path, pdf_file_path, configuration=pdfkit_config)
    print(f"PDF report generated and saved as {pdf_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
