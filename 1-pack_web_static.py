#!/usr/bin/python3
"""
Write a Fabric script that generates a .tgz
archive from the contents of the web_static folder
"""
from datetime import datetime
import tarfile
import os


def do_pack():
    """generates a .tgs archive"""
    source_directory = "web_static"
    directory = "versions"
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    output_archive_name = f"web_static_{current_time}.tgz"
    # confirm if the source path exists
    if not os.path.exists(source_directory):
        return None
    # make destination file if it does not exist
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


archive_path = do_pack()
print(f"{archive_path}")
