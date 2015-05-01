
::

  Usage:
      inventory add NAMES [--label=LABEL]
                          [--service=SERVICES]
                          [--project=PROJECT]
                          [--owners=OWNERS]
                          [--comment=COMMENT]
                          [--cluster=CLUSTER]
                          [--ip=IP]
      inventory set NAMES for ATTRIBUTE to VALUES
      inventory delete NAMES
      inventory clone NAMES from SOURCE
      inventory list [NAMES] [--format=FORMAT] [--columns=COLUMNS]
      inventory info

  Arguments:

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

