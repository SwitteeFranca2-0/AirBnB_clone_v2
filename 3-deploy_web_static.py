#!/usr/bin/python3
"""Creating an archive and sendin git to web servers"""

from fabric.api import run, local, env, put
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['ubuntu@100.25.211.145']
env.users = 'ubuntu'

do_pack = __import__('1-pack_web_static').do_pack
do_send = __import__('2-do_deploy_web_static').do_deploy


def do_deploy():
    """create archive an deploy it"""
    try:
        archive_path = do_pack()
        end = do_send(archive_path)
        return end
    except Exception as e:
        print(e)
        return False
