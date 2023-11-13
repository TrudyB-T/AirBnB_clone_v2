#!/usr/bin/python3
""" deploys """
from fabric.api import *


env.hosts = ["34.229.189.163","35.175.128.242"]
env.user = "ubuntu"


def do_clean(number=0):
    """ clean up"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
