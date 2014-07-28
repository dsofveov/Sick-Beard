import smtplib
import os

import sickbeard

from sickbeard import logger

HOSTNAME = os.uname()[1]
DEFAULT_SENDER = 'sickbeard@' + HOSTNAME

class SMTPNotifier:

    def _send_email(self, server_address, server_port, subject, message, to_address, from_address=DEFAULT_SENDER):
        logger.log(u"SMTP: _send_email " +message+" to " + to_address + " via " + server_address + ":" +server_port, logger.INFO)
        email_server = smtplib.SMTP(server_address, server_port)
        try:
            email_server.sendmail(from_address, to_address, message)
        except:
            logger.log(u"SMTP: _send_email " +message+" to " + to_address + " via " + server_address + ":" +server_port + "fail", logger.INFO)




    def _notify(self, server_address, server_port, subject, message, to_address, from_address, force=False):
        if not sickbeard.USE_SMTP and not force:
            return False

        return self._send_email(server_address, server_port, subject, message, to_address, from_address)

#######################################################################
# Public functions
#######################################################################


    def notify_snatch(self, ep_name):
        if sickbeard.SMTP_NOTIFY_ONSNATCH:
            self._notify(notifyStrings[NOTIFY_SNATCH], ep_name)

    def notify_download(self, ep_name):
        if sickbeard.SMTP_NOTIFY_ONSNATCH:
            self._notify(notifyStrings[NOTIFY_DOWNLOAD], ep_name)

    def test_notify(self, server_address, server_port, to_address):
        return self._notify(server_address, server_port, "Test", "This is a test notification from Sick Beard", to_address)

    def update_library(self, ep_obj=None):
        pass


notifier = SMTPNotifier