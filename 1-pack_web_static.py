#!/usr/bin/python3
"""Create an archive using fabric"""

from fabric.api import *
from datetime import datetime
from os.path import isdir


def do_pack():
    """Function to create an archive using python3"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local('mkdir versions')
        file_name = "versions/web_static_" + date + ".tgz"
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except Exception:
        return None
