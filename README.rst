A Simple Cloudmesh Inventory
===========================


Sometimes its necessary to maintain a simple inventory.
Naturally if you know python you can do this with dicts.
However to manage a large number of items with repeated values
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

    git clone https://github.com/cloudmesh/inventory.git
    cd cmd3
    python setup.py install
    cd ..

Configuration
---------------

Your inventory will be located at

    ~/.cloudmesh/inventory.yaml

You can also change the yaml file by hand, but the
cm command is more convenient.

This location can be changed in the file

    ~/.cloudmesh/cloudmesh_system.yaml


Manpage
--------


  Usage:
      system add NAMES [--label=LABEL]
                       [--service=SERVICES]
                       [--project=PROJECT]
                       [--owners=OWNERS]
                       [--comment=COMMENT]
                       [--cluster=CLUSTER]
                       [--ip=IP]
      system list [NAMES] [--format=FORMAT]
      system info

  Arguments:

    NAMES     Name of the resources (example i[10-20])

    FORMAT    The format of the output is either txt,
              yaml, dict, table [defaults: table].

    OWNERS    a comma separated list of owners for this resource

    LABEL     a unique label for this resource

    SERVICE   a string that identifies the service

    PROJECT   a string that identifies the project

    COMMENT   a comment

  Options:

     -v       verbose mode

  Description:

    add -- adds a system resource to the resource inventory

    list -- lists the resources in the given format

  Examples:

    cm system add x[0-3] --service=openstack

        adds hosts x0, x1, x2, x3 and puts the string
        openstack into the service column

    cm lits

        lists the repository
