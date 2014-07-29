import smtplib
import os

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import sickbeard

from sickbeard import logger
from sickbeard.common import notifyStrings, NOTIFY_SNATCH, NOTIFY_DOWNLOAD

HOSTNAME = os.uname()[1]
DEFAULT_SENDER = 'sickbeard@' + HOSTNAME

class SMTPNotifier:

    def _send_email(self, server_address, server_port, subject, message, to_address, from_address=DEFAULT_SENDER):
        email_server = smtplib.SMTP(server_address, int(server_port))

        email = MIMEMultipart()

        email['From'] = from_address
        email['To'] = to_address
        email['Subject'] = subject

        email.attach(MIMEText(message, 'plain'))

        try:
            email_server.sendmail(from_address, to_address, email.as_string())
            return True

        except:
            logger.log(u"SMTP: _send_email " +message+" to " + to_address + " via " + server_address + ":" +server_port + "fail", logger.INFO)
            return False




    def _notify(self, server_address, server_port, subject, message, to_address, from_address, force=False):
        if not sickbeard.USE_SMTP and not force:
            return False
        else:
            return self._send_email(server_address, server_port, subject, message, to_address, from_address)

#######################################################################
# Public functions
#######################################################################


    def notify_snatch(self, ep_name):
        if sickbeard.SMTP_NOTIFY_ONSNATCH:
            server_address = sickbeard.SMTP_HOST
            server_port = sickbeard.SMTP_PORT
            to_address = sickbeard.SMTP_ADDRESS
            self._notify(server_address, server_port, notifyStrings[NOTIFY_SNATCH], ep_name, to_address, from_address=DEFAULT_SENDER)

    def notify_download(self, ep_name):
        if sickbeard.SMTP_NOTIFY_ONDOWNLOAD:
            server_address = sickbeard.SMTP_HOST
            server_port = sickbeard.SMTP_PORT
            to_address = sickbeard.SMTP_ADDRESS
            self._notify(server_address, server_port, notifyStrings[NOTIFY_DOWNLOAD], ep_name, to_address, from_address=DEFAULT_SENDER)

    def test_notify(self, server_address, server_port, to_address, from_address=DEFAULT_SENDER, force=True):
        return self._notify(server_address, server_port, "Test", "This is a test notification from Sick Beard", to_address, from_address, True)

    def update_library(self, ep_obj=None):
        pass


notifier = SMTPNotifier