#!/usr/bin/python3
"""Script that distriutes an archive to your web servers"""
from fabric.api import put, run, env
import os
env.hosts = ['54.84.46.163', '52.87.28.143']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        fname_with_ext = archive_path.split("/")[-1]
        fname_no_ext = fname_with_ext.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, fname_no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(
            fname_with_ext, path, fname_no_ext))
        run("rm -f /tmp/{}".format(fname_with_ext))
        run("mv {0}{1}/web_static/* {0}{1}".format(path, fname_no_ext))
        run("rm -rf {}{}/web_static".format(path, fname_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(path, fname_no_ext))
        return True
    except Exception as e:
        return False
