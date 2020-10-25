"""A sample job that prints string."""
import logging

import requests
from ndscheduler.corescheduler import job

logger = logging.getLogger(__name__)

class LedChangeColorJob(job.JobBase):
    COLOR_CHANGE_URL = "http://{}:8080/set_{}?{}={}"

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': 'Change the color or procedure of given LED',
            'arguments': [
                # argument1
                {'type': 'string', 'description': 'Hostname of RPi with LED'},

                # argument2
                {'type': 'string', 'description': 'Type of change (color/procedure)'},

                # argument3
                {'type': 'string', 'description': 'Name of color/procedure'}
            ],
            'example_arguments': '["porchled", "color", "rainbow"]'
        }

    def run(self, argument1, argument2, argument3, *args, **kwargs):
        print('LedChangeColorJob: Argument1: %s, Argument2: %s, Argument3: %s' % (argument1, argument2, argument3))
        if argument1.endswith(".local") is not True:
            argument1 = argument1 + ".local"
        url = self.COLOR_CHANGE_URL.format(argument1, argument2, argument2, argument3)
        print(url)
        r = requests.get(url=url)
        print("Status code from attempt: " + str(r.status_code))
        return ""


if __name__ == "__main__":
    job = LedChangeColorJob.create_test_instance()
