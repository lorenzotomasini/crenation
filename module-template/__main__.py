import argparse
import sys
from threading import Thread
from crenation_utils.agents.Starter import Starter
from crenation_utils.utils.Utils import get_log_format
import pkg_resources
import logging
from main.ExposedAPI import TemplateModuleExposedAPI

__author__ = 'lto'

log = logging.getLogger(__name__)
usage = "\nThis is the template module for the platform Crenation"

LEVELS = {'0': logging.DEBUG,
          '1': logging.INFO,
          '2': logging.WARNING,
          '3': logging.ERROR,
          '4': logging.CRITICAL,
}


def main():
    config_file_name = pkg_resources.resource_filename('etc', 'config.ini')

    starter = Starter(config_file_name=config_file_name, _cls_exposed_api=TemplateModuleExposedAPI)
    starter.start()
    try:
        while True:
            cmd = raw_input(">> ")
            if cmd in ['EXIT', 'exit', 'Exit']:
                starter.stop()
                sys.exit(0)
            if cmd in ['start']:
                starter.exposed_api.invoke_method()
    except KeyboardInterrupt:
        log.info("Ctrl-C received")
        starter.stop()
        sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Template Module', usage=usage)
    parser.add_argument('-l', '--log-level',
                        help='possible values are [0, 1, 2, 3, 4] where 0 is the maximum and 4 is lowest')

    if len(sys.argv) > 1:
        args = vars(parser.parse_args(sys.argv[1:]))
        log_level = args.get('log_level')
        level = LEVELS.get(log_level)
        logging.basicConfig(format=get_log_format(), level=level)
    else:
        logging.basicConfig(level=logging.INFO)
    main()