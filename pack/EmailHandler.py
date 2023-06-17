# Jake Prisby

# Desc.: This file handles all interactions with the email account itself

import imaplib
from .Logger import Logger

# Desc.: Email Handler object
class EmailHandler():
    
    # Desc.: Constructor for the email handler
    # Input: uname- username/email address
    #        passw - password/app password if 2FA is enabled
    #        period - integer which represent the oldest emails you want to remain in days. Ex: 31 will result in emails older than 31 days being deleted
    def __init__(self, uname: str, passw: str, period: int= 31):
        self.uname = uname
        self.passw = passw
        self.period = period
        self.logger = Logger() 

    # Desc.: This method does the process of cleaning the gmail inbox
    def cleanup(self):

        from datetime import datetime, timedelta
        START_TIME = datetime.now() # Get start time of program in datetime format
        cutoff_datetime = START_TIME - timedelta(days= self.period) # Get date value of the cutoff day

        import email
        from email.header import decode_header
        months = { 1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC' } # Dictionary of month in correct string format
        cutoff_str = str(cutoff_datetime.day) + '-' + months[cutoff_datetime.month] + '-' + str(cutoff_datetime.year)

        # Login to email
        imap = imaplib.IMAP4_SSL('imap.gmail.com')
        imap.login(self.uname, self.passw)

        # Search for emails that meet criteria
        imap.select('INBOX')
        status, messages = imap.search(None, 'BEFORE "' + cutoff_str + '" UNFLAGGED')

        # Now that email lists have been created, delete all emails in the messages list that are not included in the starred_messages list
        messages = messages[0].split(b' ')
        if len(messages) > 0:
            for mail in messages:
                try:
                    _, msg = imap.fetch(mail, "(RFC822)")
                    for response in msg:
                        if isinstance(response, tuple):
                            msg = email.message_from_bytes(response[1])
                            # decode the email subject
                            try:
                                subject = decode_header(msg["Subject"])[0][0]
                                if isinstance(subject, bytes):
                                    # if it's a bytes type, decode to str
                                    subject = subject.decode('utf-8', errors= 'ignore')
                                print("Deleting: ", subject)
                                self.logger.write_info("Deleting:" + str(subject))
                            except TypeError:
                                print("Deleting: No Subject")
                    # mark the mail as deleted
                    imap.store(mail, "+FLAGS", "\\Deleted")
                except Exception as e:
                    print('Failed to deleted email: ' + str(e))
                    self.logger.write_error('Failed to deleted email: ' + str(e))

            imap.expunge() # Empty trash
            imap.close() # close the mailbox
            imap.logout() # logout from the account

        RUNTIME = datetime.datetime.now() - START_TIME
        self.logger.write_info('TOTAL RUNTIME: ' + str(RUNTIME))

# Desc.: Tests gmail credentials
# Input: uname - Username or email address
#        passw - password, NOTE: if 2FA is enabled then an app password needs to be used
def test_creds(uname: str, passw:str) -> bool:
    try:
        test_imap = imaplib.IMAP4_SSL('imap.gmail.com')
        test_imap.login(uname, passw)
    except Exception as e:
        raise Exception("ERRROR: Credentials failed to login, " + str(e))