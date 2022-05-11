import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #Connecting to the mail browser
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('arnavsample@gmail.com', 'password1604')

    subject = 'Hi babes!'
    body = 'Its me Arnav'

    message = 'Subject: ' + subject + '\n\n' + 'body: '+ body
    smtp.sendmail('arnavsample@gmail.com','nikhileshkumar225@gmail.com', message )
    print('Thanks')