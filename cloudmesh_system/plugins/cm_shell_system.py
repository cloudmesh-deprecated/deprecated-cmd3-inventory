from __future__ import print_function
import os
from cmd3.console import Console
from cmd3.shell import command

from cloudmesh_system.command_system import command_system
import hostlist
from pprint import pprint


class cm_shell_system:

    def activate_cm_shell_system(self):
        self.register_command_topic('mycommands', 'system')

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
              system list [NAMES] [--format=FORMAT]

          Arguments:

            NAMES     Name of the resources (example i[10-20])

            FORMAT    The format of the output is either txt,
                      yaml, json, table [default=table].

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

            
        """
        pprint(arguments)

        if arguments["NAMES"] is None:
            Console.error("Please specify a host name")
        else:
            hosts = hostlist.expand_hostlist(arguments["NAMES"])            
            Console.info("Hosts {0}".format(str(hosts)))
            # status = command_system.status(host)
            #if status:
            #    Console.info("machine " + host + " has been found. ok.")
            #else:
            #    Console.error("machine " + host + " not reachable. error.")
        pass

if __name__ == '__main__':
    command = cm_shell_system()
    command.do_system("iu.edu")
    #command.do_system("iu.edu-wrong")
