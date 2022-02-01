#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2022.
#  Created by Zhbert.
#  Licensed by GPLv3.

import smtplib


def send_email(host, port, subject, address_to, address_from, body_text):
    email_body = "\r\n".join((
        "From: %s" % address_from,
        "To: %s" % address_to,
        "Subject: %s" % subject,
        "",
        body_text
    ))
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login('USERNAME', 'PASSWORD')
    server.sendmail(address_from, [address_to], email_body)
    server.quit()
