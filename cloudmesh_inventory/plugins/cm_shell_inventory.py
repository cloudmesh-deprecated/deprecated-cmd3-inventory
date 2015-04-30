from __future__ import print_function
from cmd3.console import Console
from cmd3.shell import command


from cloudmesh_inventory.command_inventory import inventory
import hostlist
from cloudmesh_base.locations import config_file

# TODO: delete row
# TODO: add columns
# TODO: ATTRIBUTE=VALUE

class cm_shell_inventory:

    def activate_cm_shell_inventory(self):
        self.register_command_topic('system', 'inventory')

    @command
    def do_inventory(self, args, arguments):
        """
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
              inventory delete NAMES
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
        """
        # pprint(arguments)
        filename = config_file("/cloudmesh_inventory.yaml")

        sorted_keys = True
        if arguments["info"]:
            i = inventory()
            i.read()
            i.info()
        elif arguments["list"]:
            i = inventory()
            i.read()
            order = arguments["--columns"].split(",")
            print (order)
            print(i.list(format="table", order=order))
        elif arguments["NAMES"] is None:
            Console.error("Please specify a host name")
        elif arguments["set"]:
            hosts = hostlist.expand_hostlist(arguments["NAMES"])
            i = inventory()
            i.read()
            element = {}

            for attribute in i.order:
                try:
                    attribute = arguments["ATTRIBUTE"]
                    value = arguments["VALUE"]
                    if value is not None:
                        element[attribute] = value
                except:
                    pass
            element['host'] = arguments["NAMES"]
            i.add(**element)
            print (i.list(format="table"))
        elif arguments["add"]:
            hosts = hostlist.expand_hostlist(arguments["NAMES"])            
            i = inventory()
            i.read()
            element = {}

            for attribute in i.order:
                try:
                    value = arguments["--" + attribute]
                    if value is not None:
                        element[attribute] = value
                except:
                    pass
            element['host'] = arguments["NAMES"]
            i.add(**element)
            print (i.list(format="table"))
        elif arguments["delete"]:
            hosts = hostlist.expand_hostlist(arguments["NAMES"])
            i = inventory()
            i.read()

            for host in hosts:
                del i.data[host]
            i.save()

if __name__ == '__main__':
    command = cm_shell_inventory()
    command.do_system("iu.edu")
