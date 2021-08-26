#!/usr/bin/python3
""" Fabric File """

from fabric.api import local, env, put, run
from datetime import datetime
import os.path
env.host = ['34.74.126.117', '34.235.137.233']


def do_deploy(archive_path):
    """
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path[9:]
        path_ = file_name[:-4]
        put(path_, '/tmp/' + file_name)
        run('mkdir -p /data/web_static/releases/' + file_name)
        run('tar -xzvf /tmp/' + archiveName +
            " -C /data/web_static/releases/" +
            archiveNameMinusExtension + " --strip-components=1")
        run('rm -rf /tmp/' + file_name)
        run ('rm -rf /data/web_static/current')
        run('sudo ln -sf /data/web_static/releases/' + path_ +
           ' /data/web_static/current')
        return True
    except:
        return False

def do_pack():
    """ function do pack """

    try:
        now = datetime.now()

        file_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        name_path = "versions/" + file_name

        local("mkdir -p versions")

        local("tar -czvf " + name_path + " web_static")

        return name_path
    except:
        return None
