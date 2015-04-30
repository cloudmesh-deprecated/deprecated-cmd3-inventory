A simple inventory
===========================


Sometimes its necessary to maitain a simple inventory.
Naturally if you know python you can do this with dicts.
However to manage a lare number of items with repeated values
its is of advantage to do this from the commandline.

We have written such a tool that lets you easily manage the
resources in a table format.

Installation
---------------

From Pip

    we have not yet uploaded the code to pypi

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

    git clone https://github.com/cloudmesh/system.git
    cd cmd3
    python setup.py install
    cd ..

Configuration
---------------

Your inventory will be located at

    ~/.cloudmesh/cloudmesh_inventory.yaml

This location can be changed in the file

    ~/.cloudmesh/cloudmesh_system.yaml
