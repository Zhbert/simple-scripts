#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2022.
#  Created by Zhbert.
#  Licensed by GPLv3.

import smtplib

from settings_file_service import *


def send_email(subject, address_to, address_from, body_text):
    email_body = "\r\n".join((
        "From: %s" % address_from,
        "To: %s" % address_to,
        "Subject: %s" % subject,
        "",
        body_text
    ))
    server = smtplib.SMTP(get_email_host(), get_email_port())
    server.ehlo()
    server.starttls()
    server.login(get_email_username(), get_email_password())
    server.sendmail(address_from, [address_to], email_body)
    server.quit()
