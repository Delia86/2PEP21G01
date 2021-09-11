import smtplib
import imaplib

def receive_mail(user,passw):

    imap=imaplib.IMAP4_SSL('imap.gmail.com',993)
    imap.login(user,passw)
    imap.select('Inbox')




def send_mail(user, passw, msg, to):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, passw)
    server.sendmail(user, to, msg)