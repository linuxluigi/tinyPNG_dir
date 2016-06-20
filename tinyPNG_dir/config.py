import __future__
from appdirs import AppDirs
import os
import sys
import tinify

dirs = AppDirs("tinyPNG_dir", "milliiard.:")

def get_config_file():
    conf_file = os.path.join(dirs.user_data_dir, 'api-key.conf')
    return conf_file

def test_api_key(api_key):
    try:
      tinify.key = api_key
      tinify.validate()
      print ("compressions this month: %i" % tinify.compression_count)
      return True
    except tinify.Error:
      return False

def load_config():
    conf_file = get_config_file()

    if not os.path.exists(dirs.user_data_dir):
        os.makedirs(dirs.user_data_dir)

    if os.path.isfile(conf_file):
        with open(conf_file, 'r') as myfile:
            conf=myfile.read().replace('\n', '')
            return conf
    else:
        return write_config()

def write_config():
    api_key = None
    api_success = False
    while api_success == False:
        api_key = input("Please write your TinyPNG API key: ")
        api_success = test_api_key(api_key)
        if api_success:
            conf_file = open(get_config_file(), "w")
            conf_file.write(api_key)
            conf_file.close()
            print ("TinyPNG API key saved")
            print (get_config_file())
        else:
            print ("no valid api key, please try again")
    return api_key

def get_api_key():
    conf = load_config()
    if test_api_key(conf):
        return conf
    else:
        print ("API Key error, please delete your conf file")
        print (get_config_file())
        sys.exit()
