import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #Connecting to the mail browser
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('arnavsample@gmail.com', 'password1604')

    subject = 'You were caught overspeeding!'
    body = 'Your speed was 125kmph'

    message = 'Subject: ' + subject + '\n\n' + 'body: '+ body
    smtp.sendmail('arnavsample@gmail.com','arnavsample@gmail.com', message )
    print('Thanks')