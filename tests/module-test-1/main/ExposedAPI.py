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

    def start_test_1(self, *args):
        self.api_invoker.invoke_method('module-test-1', 'start_test_2', "", {}, )

