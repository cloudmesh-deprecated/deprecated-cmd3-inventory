#!/usr/bin/env python

version = "1.0"


requirements = [
    'future',
    'sh',
    'docopt',
    'pyaml',
    'simplejson',
    'nose',
    'python-hostlist',
    'prettytable',
    'pytimeparse',
    ]

from setuptools import setup, find_packages
from setuptools.command.install import install
import glob
import os

package_name = "cloudmesh_system"

try:
    from cloudmesh_base.util import banner
except:
    os.system("pip install cloudmesh_base")

from cloudmesh_base.util import banner
from cloudmesh_base.util import path_expand
from cloudmesh_base.Shell import Shell
from cloudmesh_base.util import auto_create_version
from cloudmesh_base.util import auto_create_requirements


banner("Installing Cloudmesh System" + package_name)

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]



requirements = parse_requirements('requirements.txt')

home = os.path.expanduser("~")

auto_create_version(package_name, version)


data_files= [ (home + '/.cloudmesh/' + d.lstrip('cloudmesh_system/'),
                [os.path.join(d, f) for f in files]) for d, folders, files in os.walk('cloudmesh_system/etc')]


import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('cloudmesh_system/etc'):
  for filename in fnmatch.filter(filenames, '*'):
    matches.append(os.path.join(root, filename).lstrip('cloudmesh_system/'))
data_dirs = matches


class SetupYaml(install):
    """Copies a cloudmesh_system yaml file to ~/.cloudmesh."""

    description = __doc__

    def run(self):
        banner("Setup the cloudmesh_system.yaml file")

        cloudmesh_system_yaml = path_expand("~/.cloudmesh/cloudmesh_system.yaml")

        if os.path.isfile(cloudmesh_system_yaml):
            print ("ERROR: the file {0} already exists".format(cloudmesh_system_yaml))
            print
            print ("If you like to reinstall it, please remove the file")
        else:
            print ("Copy file:  {0} -> {1} ".format(path_expand("etc/cloudmesh_system.yaml"), cloudmesh_system_yaml))
            Shell.mkdir("~/.cloudmesh")

            shutil.copy("etc/cloudmesh_system.yaml",
                        path_expand("~/.cloudmesh/cloudmesh_system.yaml"))



class UploadToPypi(install):
    """Upload the package to pypi."""
    def run(self):
        os.system("Make clean Install")
        os.system("python setup.py.in install")
        banner("Build Distribution")
        os.system("python setup.py.in sdist --format=bztar,zip upload")


class RegisterWithPypi(install):
    """Upload the package to pypi."""
    def run(self):
        banner("Register with Pypi")
        os.system("python setup.py.in register")


class InstallBase(install):
    """Install the package."""
    def run(self):
        banner("Installing Cloudmesh " + package_name)
        install.run(self)


class InstallRequirements(install):
    """Install the requirements."""
    def run(self):
        banner("Installing Requirements for Cloudmesh " + package_name)
        os.system("pip install -r requirements.txt")


class InstallAll(install):
    """Install requirements and the package."""
    def run(self):
        banner("Installing Requirements for Cloudmesh " + package_name)
        os.system("pip install -r requirements.txt")
        banner("Installing Cloudmesh " + package_name)
        install.run(self)

setup(
    name='MODULE',
    version=version,
    description='A set of simple base functions and classes useful for cloudmesh and other programs',
    # description-file =
    #    README.rst
    author='The Cloudmesh Team',
    author_email='laszewski@gmail.com',
    url='http://github.org/cloudmesh/base',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Boot',
        'Topic :: System :: Systems Administration',
        'Framework :: Flask',
        'Environment :: OpenStack',
    ],
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    data_files= data_files,
    package_data={'cloudmesh_system': data_dirs},
    cmdclass={
        'install': InstallBase,
        'requirements': InstallRequirements,
        'all': InstallAll,
        'pypi': UploadToPypi,
        'pypiregister': RegisterWithPypi,
        'yaml': SetupYaml,
        },
)

