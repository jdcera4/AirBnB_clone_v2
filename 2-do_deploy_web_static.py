#!/usr/bin/python3
""" Fabric File """
from fabric.api import *
from datetime import datetime
import os.path
env.hosts = ['34.74.126.117', '34.235.137.233']


def do_deploy(archive_path):
    """ Deploy an archive """

    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path[9:]
        Extension = file_name[:-4]

        put(archive_path, '/tmp/' + file_name)
        run("mkdir -p /data/web_static/releases/" + Extension)
        run('tar -xzf /tmp/' + file_name +
            " -C /data/web_static/releases/" +
            Extension)
        run("rm /tmp/" + file_name)
        run("mv /data/web_static/releases/" + file_name[0:-4] + "/web_static/* "
            + "/data/web_static/releases/web_static_20210826102615/")
        run("rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            Extension + " /data/web_static/current")

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
