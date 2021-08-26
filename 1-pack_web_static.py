#!/usr/bin/python3
""" Fabric File """

from fabric.api import local
from datetime import datetime


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
