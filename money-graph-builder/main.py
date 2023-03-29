#  Copyright (c) 2023, Konstantin <Zhbert> Nezhbert
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this
#  software and associated documentation files (the "Software"), to deal in the Software
#  without restriction, including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
#  to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or
#  substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.
import imaplib
import os
import email

import chardet as chardet

################################################################################
# Config
################################################################################

config = {
    # Email
    'EMAIL': os.environ["USER_EMAIL"],
    'PASSWD': os.environ["USER_PASSWD"],
    'EMAIL_SERVER': os.environ["EMAIL_SERVER"],
}

################################################################################
# Login to email server
################################################################################

mail = imaplib.IMAP4_SSL(config['EMAIL_SERVER'])
mail.login(config['EMAIL'], config['PASSWD'])

################################################################################
# Search files from target sender
################################################################################

mail.select('INBOX')
typ, data = mail.search(None, 'ALL')
data = data[0].split()
for i in data:
    status, data = mail.fetch(i, '(RFC822)')
    data = data[0][1]
    enc = chardet.detect(data)

    msg = email.message_from_bytes(data)
    if msg['From'] == 'noreply@ofd.ru':
        print(msg['Body'])
mail.close()
