import json
import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email import encoders

BASE_URL = "https://remoteok.com/api/"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
REQUEST_HEADER = {
    'User-Agent':USER_AGENT,
    'Accept-Language':'en-US, en;q=0.5'
}
def get_job_posting():
    res = requests.get(url = BASE_URL, headers=REQUEST_HEADER)
    return res.json()

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    for i in range(0, len(headers)):
        job_sheet.write(0, i, headers[i])
    for i in range(0, len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(0, len(values)):
            job_sheet.write(i + 1, x, values[x])
    wb.save('remote_jobs.xls')

def send_email(send_from, password, send_to, subject, body, file_path=None):
    # Create a multipart message
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)  # Use COMMASPACE to join multiple recipients
    msg['Date'] = formatdate(localtime=True)  # Use formatdate to set the Date header
    msg['Subject'] = subject
    # Attach the message body
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file, if provided
    if file_path:
        with open(file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={basename(file_path)}')
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(send_from, password)
        server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()


if __name__=='__main__':
    print("Hello Master Harry, our GOAT")
    json_data = get_job_posting()
    output_jobs_to_xls(json_data[1:])
    # Example usage
    send_from = 'harishthepirate@gmail.com'
    password = 'parLakbaSH@97'
    send_to = ['harishthesuccessor@gmail.com','harishparamathmananda@gmail.com']
    subject = 'Job Alert'
    body = 'Hi, This is a list of jobs available on remote so try to apply.'
    file_path = r'C:\Users\Harish Paramathma\git\Mastering_BS4_Selenium\remote_jobs.xls'

    send_email(send_from, password, send_to, subject, body, file_path)