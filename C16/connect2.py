"""https://www.geeksforgeeks.org/python-fetch-your-gmail-emails-from-a-particular-user/"""

import imaplib
import re

username = 'pinkiwinkiwinki555'
password = '1234pinki'
imap_url = 'imap.gmail.com'


def get_mail(username, password):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(username, password)
    con.select('Inbox')
    result, data =con.search(None, 'FROM', 'ozy24us@hotmail.com')
    msgs = []
    for num in data[0].split():
        message_data = con.fetch(num, '(RFC822)')[1]
        msgs.append(message_data)
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple:
                content = str(sent[1], 'utf-8')
                yield content  # re.match('', content).

if __name__ == '__main__':
    mails = get_mail(username, password)
    for mail in mails:
        print(mail)