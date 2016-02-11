import logging
from crenation_utils.agents.Starter import ExposedAPI
from crenation_utils.annotation.Annotations import public_api

__author__ = 'lto'
log = logging.getLogger(__name__)


class TemplateModuleExposedAPI(ExposedAPI):
    def __init__(self):
        pass

    @public_api
    def api_method(self, string):
        log.debug("i'm here in api: %s" % string)
