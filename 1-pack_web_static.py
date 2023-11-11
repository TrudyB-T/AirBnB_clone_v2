#!/usr/bin/python3
"""Creates a .tgz archive using the contents of the web_static folder."""

from fabric.api import local
import time


def do_pack():
    """Generates an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except Exception:
        return None
