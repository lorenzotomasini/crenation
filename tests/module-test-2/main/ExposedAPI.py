import logging
import time
from crenation_utils.agents.Exceptions import ModuleNotFound
from crenation_utils.agents.Starter import ExposedAPI
from crenation_utils.annotation.Annotations import public_api
from model.Entities import Entry

__author__ = 'lto'
log = logging.getLogger(__name__)

#
# answ = self.api_invoker.invoke_method(module_name, method_name, *params)
#

class AnObject(object):
    def __init__(self):
        self.name = 'name'
        self.dependecies = []

    def add_dependecy(self, dep):
        self.dependecies.append(dep)

    def __str__(self):
        return "AnObject [name=%s]" % self.name

class Dependecy(object):

    def __init__(self, name=None):
        self.name = name


class TemplateModuleExposedAPI(ExposedAPI):
    def __init__(self):
        pass

    @public_api
    def template_method(self, string):
        log.debug("i'm here in module-template: %s" % string)

    def invoke_method(self):
        # def register_to_event(self, method_name, event_name, *args):
        self.api_invoker.register_to_event('template_method', 'template-event', 'parameter')
        time.sleep(1)
        self.api_invoker.fire_event('template-event')
        # answer = None
        #
        # entry = Entry()
        # entry.name = 'dns-manager-getter'
        # entry.ip = 'test'
        # entry.port = 'test'
        # obj = self.db_manager.put(entry)
        # log.debug("Received %s" % obj)
        # try:
        # answer = self.db_manager.get(entry.__class__.__name__, {'name': 'dns-manager-getter'})
        # log.debug('received %s' % answer)
        # except ModuleNotFound as e:
        # log.warning("Module api not found")

