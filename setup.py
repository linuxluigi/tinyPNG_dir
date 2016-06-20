from distutils.core import setup
from setuptools import setup

setup(
    name='tinypng_dir',
    version='0.1dev',
    author='Steffen Exler',
    author_email='steffen.exler@gmail.com',
    packages=['tinypng_dir',],
    entry_points = {
        "console_scripts": ['tinypng_dir = tinypng_dir.compress:main']
        },
    license='LICENSE',
    description='recursively compress any image in a directory',
    long_description=open('README.md').read(),
    install_requires=[
        "tinify >= 1.3.0",
        "appdirs >= 1.4.0",
    ],
)
