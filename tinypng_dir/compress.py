import __future__

from appdirs import AppDirs
import os
from .config import get_api_key
import tinify
import fnmatch

def get_directory():
    directory_success = False
    while directory_success == False:
        directory = input("Your directory that your want to compress: ")
        if os.path.exists(directory):
            directory_success = True
        else:
            print ("Directory not exist, please try again!")
    return directory

def get_images(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(('.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG')):
                images.append(os.path.join(root, filename))
    return images

def compress_image(images):
    for image in images:
        source = tinify.from_file(image)
        source.to_file(image)
        print (image)

def main():
    tinify.key = get_api_key()
    directory = get_directory()
    images = get_images(directory)
    compress_image (images)
