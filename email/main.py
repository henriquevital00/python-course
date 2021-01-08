import smtplib

my_email = input('Enter your mail: ')
password = input('Enter your password: ')

send_to = input('Send to: ')

subject = input('Subject: ')
message = input('Enter the message: ')

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,
                    to_addrs=send_to,
                    msg='{}\n\n{}'.format(subject, message))
connection.close()
