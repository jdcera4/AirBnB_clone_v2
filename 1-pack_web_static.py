#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    function do pack
    """
    try:
        data = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is false:
            local("mkdir versions")
        file_name = "versions.web_static_{}.tgz".format(data)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
