#!/usr/bin/python3
"""Import necessary modules"""

from datetime import datetime
import tarfile
import os
from fabric.api import put, run, env
env.hosts = ['54.84.46.163', '52.87.28.143']


def do_pack():
    """generates a .tgs archive"""
    source_directory = "web_static"
    directory = "versions"
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output_archive_name = f"web_static_{current_time}.tgz"
    # confirm if the source path exists
    if not os.path.exists(source_directory):
        return None
    if not os.path.exists(directory):
        os.makedirs(directory)
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output_archive_name = f"{directory}/web_static_{current_time}.tgz"
    try:
        with tarfile.open(output_archive_name, "w:gz") as tar:
            tar.add(source_directory, arcname="")
        return output_archive_name
    except Exception as e:
        return None

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

def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)
