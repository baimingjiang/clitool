
import logging
from clitool import utils

class BaseObject(object):

    def __init__(self, options):
        super(BaseObject, self).__init__()
        self._options = options

    @property
    def logger(self):
        pass

    @property
    def project_name(self):
        return self.get_config('project.name')

    def get_option(self, key):
        if key in self._options:
            return self._options[key]
        return None
    
    def get_config(self, key):
        return utils.getConfig(key)
