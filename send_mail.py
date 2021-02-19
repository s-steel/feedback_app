import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments)
  # this is all setup for using mailtrap.io 
  port = 2525
  smtp_server = 'smtp.mailtrap.io'
  login = 'username_here'
  password = 'password_here'
  message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

  sender_email = 'email1@example.com'
  receiver_email = 'email2@example.com'
  msg = MIMText(message, 'html')
  msg['Subject'] = 'Vehicle Feedback'
  msg['From'] = sender_email
  msg['To'] = receiver_email

  # Send the email 
  with smtplib.SMTP(smtp_server, port) as server:
    server.login(login, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    