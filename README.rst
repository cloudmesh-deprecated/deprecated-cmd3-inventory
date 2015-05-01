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

Make sure you have a new version of python. We use 2.7.9. Make sure to
have a new version of pip. We use 6.1.1

From Pip::

  pip install cmd3
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

    ~/.cloudmesh/inventory.yaml

You can also change the yaml file by hand, but the
cm command is more convenient.

This location can be changed in the file

    ~/.cloudmesh/cloudmesh_system.yaml

If you have not yet created a cmd3.yaml file you can
do this with::

  cm setup_yaml

Edit the file ~/.cloudmesh/cmd3.yaml and add to the plugin list:

  - cloudmesh_inventory.plugin


Manpage
--------

::
   
  Usage:
  
      inventory add NAMES [--label=LABEL]
                          [--service=SERVICES]
                          [--project=PROJECT]
                          [--owners=OWNERS]
                          [--comment=COMMENT]
                          [--cluster=CLUSTER]
                          [--ip=IP]
      inventory NAMES set ATTRIBUTE to VALUE
      inventory NAMES map ATTRIBUTE to VALUES
      inventory delete NAMES
      inventory clone NAMES from SOURCE
      inventory list [NAMES] [--format=FORMAT] [--columns=COLUMNS]
      inventory info

  Arguments::

    NAMES     Name of the resources (example i[10-20])

    FORMAT    The format of the output is either txt,
              yaml, dict, table [default: table].

    OWNERS    a comma separated list of owners for this resource

    LABEL     a unique label for this resource

    SERVICE   a string that identifies the service

    PROJECT   a string that identifies the project

    SOURCE    a single host name to clone from

    COMMENT   a comment

  Options:

     -v       verbose mode

  Description:

    add -- adds a resource to the resource inventory

    list -- lists the resources in the given format

    delete -- deletes objects from the table

  Examples:

    cm inventory add x[0-3] --service=openstack

        adds hosts x0, x1, x2, x3 and puts the string
        openstack into the service column

    cm lits

        lists the repository
