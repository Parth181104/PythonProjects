# import smtplib as s

# ob = s.SMTP('smtp.gmail.com',587)
# ob.ehlo()
# ob.starttls()
# ob.login('parthdatar18@gmail.com', 'Partha@1811')
# subject = "TESTING MAIL FOR AUTO-SENDER"
# body = "I love python"
# message = "subject:{}\n\n{}".format(subject,body)
# listadd=['harsheetpatel6121@gmail.com', "datarvrushali101@gmail.com"]
# ob.sendmail('parthdatar18@gmail.com',listadd,message)
# print("Mails Sent")
# ob.quit()

import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = 'anishpatel6678@gmail.com'
receiver_emails = ['parthdatar18@gmail.com', 'datarvrushali101@gmail.com']
subject = "TESTING MAIL FOR AUTO-SENDER"
body = "I love python"

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(receiver_emails)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Establish a secure session with Gmail's SMTP server using TLS
    with s.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.ehlo()
        server.login(sender_email, 'anishpatel@123')  # Replace with your password or use a secure method
        server.sendmail(sender_email, receiver_emails, msg.as_string())
    print("Mails Sent Successfully")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
