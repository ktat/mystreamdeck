import time
import os
import sys

class Alert:
    # if app reuquire thread, true
    use_thread = True
    # dict: key is page name and value is key number.
    page_key = {}
    # need to stop thread
    stop = False

    _check_function = None
    _check_interval = 300
    _retry_interval = 60
    _previous_checke_time = 0
    in_alert = False

    def __init__ (self, mydeck, config):
        alert_key_config = {}
        if config.get("check_interval"):
            self._check_interval = config.get("check_interval")
        if config.get("retry_interval"):
            self._retry_interval = config.get("retry_interval")
        if config.get("key_cofnig"):
            alert_key_config = config.get("key_cofnig")
            
        self._previous_checke_time = 0
        self.mydeck = mydeck

    def set_check_func(self, f):
        self._check_function = f

    def set_conf(self, conf):
        self.mydeck.key_config()['~ALERT'] = conf

    def start(self):
        while True:
            current = time.time()
            interval = self._check_interval
            if self.in_alert:
                interval = self._retry_interval
            if current - self._previous_checke_time > interval:
                self._previous_checke_time = current
                if self._check_function():
                    self.mydeck.handler_alert()
                    self.in_alert = True
                    self.mydeck.set_alert(1)
                else:
                    self.mydeck.handler_alert_stop()
                    self.in_alert =False
                    self.mydeck.set_alert(0)

            if self.mydeck._exit:
                break
            time.sleep(1)
        sys.exit()

    def key_setup(self):
        return True
