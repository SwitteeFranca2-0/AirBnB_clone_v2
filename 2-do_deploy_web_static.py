#!/usr/bin/python3
"""Fab Script that distributes python scripts to all servers"""

from fabric.api import run, put, env, local
from os.path import exists
env.hosts = ['ubuntu@100.25.211.145', 'ubuntu@52.3.249.150']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distribute the archive to the webservers"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[1]
        dir = '/data/web_static/releases/' + file[:-4]
        run('sudo mkdir -p {}'.format(dir))
        archive = '/tmp/' + file
        run('sudo tar -xvf {} -C {}'.format(archive, dir))
        run('sudo rm {}'.format(archive))
        run('sudo mv {0}/web_static/* {0}'.format(dir))
        run('sudo rm -rf {}/web_static'.format(dir))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {} /data/web_static/current'.format(dir))
        return True
    except Exception:
        return False