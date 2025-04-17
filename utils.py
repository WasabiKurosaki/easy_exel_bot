import os

def init_dir(download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

def check_if_exel():
    ...