from distutils.core import setup

setup(
    name='tinyPNG_dir',
    version='0.1dev',
    author='Steffen Exler',
    author_email='steffen.exler@gmail.com',
    packages=['tinypng_dir',],
    license='LICENSE',
    description='recursively compress any image in a directory',
    long_description=open('README.md').read(),
    install_requires=[
        "tinify >= 1.3.0",
        "appdirs >= 1.4.0",
    ],
)
