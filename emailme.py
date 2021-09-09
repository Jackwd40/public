import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

try:

    gmail_user = 'a9xdefender@gmail.com'
    gmail_password = 'F0ur160nien?'

    fromaddr = "a9xdefender@gmail.com"
    toaddr = "jdavies@conetrix.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "DATA"

    body = "DATA ENCLOSED"

    msg.attach(MIMEText(body, 'plain'))

    filename = "secure.tar.gz"
    attachment = open("./secure.tar.gz", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)





    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.close()


except Exception as e:
    print(e)
