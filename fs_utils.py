import tarfile
import os.path
from shutil import rmtree

'''
Filesystem helper funcitons
'''

def extract_tar_gz(filename, destination_dir):
    with tarfile.open(filename, 'r:gz') as _tar:
        _tar.extractall(destination_dir)

def make_tar_gz(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
def rm_tree(path_to_dir):
    try:
        rmtree(path_to_dir)
    except FileNotFoundError:
        pass