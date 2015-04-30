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
    def do_system(self, args, arguments):
        """
        ::

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
            print(i.list())
        elif arguments["NAMES"] is None:
            Console.error("Please specify a host name")
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


if __name__ == '__main__':
    command = cm_shell_inventory()
    command.do_system("iu.edu")
