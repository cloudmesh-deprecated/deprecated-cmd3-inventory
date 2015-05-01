A Simple Cloudmesh Inventory
============================


Sometimes its necessary to maintain a simple inventory.
Naturally if you know python you can do this with dicts.
However to manage a large number of items with repeated values
its is of advantage to do this from the commandline.

We have written such a tool that lets you easily manage the
resources in a table format.


Installation
---------------

Make sure you have a new version of python and pip. We tested with

* python 2.7.9
* pip 6.11

It may work with other python versions, but we have not tried it.

From Pip::

  pip install cloudmesh_inventory

From Source

::

    mkdir github
    cd github

    git clone https://github.com/cloudmesh/base.git
    cd base
    python setup.py install
    cd ..

    git clone https://github.com/cloudmesh/cmd3.git
    cd cmd3
    python setup.py install
    cd ..

    git clone https://github.com/cloudmesh/inventory.git
    cd cmd3
    python setup.py install
    cd ..

Configuration
---------------

Your inventory will be located at

*    ~/.cloudmesh/inventory.yaml

You can also change the yaml file by hand, but the
cm command is more convenient.

This location can be changed in the file

*    ~/.cloudmesh/cloudmesh_system.yaml

If you have not yet created a cmd3.yaml file you can
do this with::

  cm setup_yaml

Edit the file ~/.cloudmesh/cmd3.yaml and add to the plugin list:

* cloudmesh_inventory.plugin


Manpage
--------
