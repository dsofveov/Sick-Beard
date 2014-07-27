import smtplib

import sickbeard

from sickbeard import logger

class SMTPNotifier:
    def _notify(self):
        pass

    def notify_snatch(self, ep_name):
        pass

    def notify_download(self, ep_name):
        pass

    def test_notify(self, accessToken, sound):
        pass
        
    def update_library(self, ep_obj=None):
        pass