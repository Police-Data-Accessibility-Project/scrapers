import logging

class LogOwnerMixin(object):
    def __init__(self, *args, log_name=None, **kwargs):
        if log_name is None:
            if hasattr(self, 'log_name'):
                log_name = self.log_name
            else:
                log_name = self.__class__.__name__
        self.log_name = log_name
        self.logger = logging.getLogger(log_name)
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warn = self.logger.warn
        self.error = self.logger.error
        self.crit = self.logger.critical
        super(LogOwnerMixin, self).__init__(self, *args, **kwargs)