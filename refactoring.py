import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MyMail:
    '''Class for interaction with gmail

    '''
    gmail_smpt = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    def __init__(self, login: str='login@gmail.com', password: str='qwerty'):
        self.login = login
        self.password = password

    def send_message(self, recipients: list, subject: str, message: str):
        '''Send message method
        '''
        mime_msg = MIMEMultipart()
        mime_msg['From'] = self.login
        mime_msg['To'] = ', '.join(recipients)
        mime_msg['Subject'] = subject
        mime_msg.attach(MIMEText(message))

        smpt = smtplib.SMTP(self.gmail_smpt, 587)
        # identify ourselves to smtp gmail client
        smpt.ehlo()
        # secure our email with tls encryption
        smpt.starttls()
        # re-identify ourselves as an encrypted connection
        smpt.ehlo()

        smpt.login(self.login, self.password)
        smpt.sendmail(self.login, recipients, mime_msg.as_string())

        smpt.quit()

    def receive_message(self, header: str=None):
        '''Receive message method
        '''
        imap = imaplib.IMAP4_SSL(self.gmail_imap)
        imap.login(self.login, self.password)
        imap.list()
        imap.select("inbox")

        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        status, data = imap.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        status, data = imap.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)

        imap.logout()