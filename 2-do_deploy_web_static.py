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
        archiveName = archive_path[9:]
        archiveNameMinusExtension = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" + archiveNameMinusExtension)
        run('tar -xzvf /tmp/' + archiveName +
            " -C /data/web_static/releases/" +
            archiveNameMinusExtension + " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archiveNameMinusExtension + " /data/web_static/current")

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
