import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASEDIR)
MODE = 'Salt'  #ssh   salt

PLUGINS = {
    'disk':"client.src.plugins.disk.DiskPlugin",

}

NIC_PATH = os.path.join(BASEDIR,"conf","nic")

