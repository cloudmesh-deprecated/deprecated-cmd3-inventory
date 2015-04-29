from cloudmesh_base.Shell import Shell
from cloudmesh_base.ConfigDict import ConfigDict
from cloudmesh_base.util import path_expand
from cloudmesh_base.tables import dict_printer
from pprint import pprint
import json
import yaml
import hostlist
import sys

class inventory(object):

    order = ["cluster",
             "host",
             "label",
             "service",
             "project",
             "owners",
             "comment"]

    entry = {}
    for key in order:
        entry[key] = ""
        
    def __init__(self):
        self.data = {}
        pass

    def read(self, filename, format="yaml"):
        stream = open(filename, "r")
        self.data = yaml.safe_load(stream)
        stream.close()

    def save(self, filename, format="yaml"):
        with open(filename, 'w') as yaml_file:
            yaml_file.write(self.list (format=format))

    def add(self, **kwargs):
        new_entry = dict(self.entry)
        for key, value in kwargs.iteritems():
            new_entry[key] = value
        if "host" not in kwargs:
            print "ERROR no id specified"
            sys.exit(1)

        hosts = hostlist.expand_hostlist(kwargs['host'])
        for host in hosts:
            element = dict(new_entry)
            element['host'] = host
            self.data[host] = element

    def list(self, format='dict'):
        return dict_printer(self.data, output=format)


    def _str(self, data, with_empty=False):
        print
        for key in data:
            print "O", key
            if self.data[key] is '' or self.data[key] is None:
                pass
            else:
                print self.data[key]


class command_system(object):
    @classmethod
    def status(cls, host):
        msg = "Unknown host"
        try:
            msg = Shell.ping("-c", "1", host)
        except:
            pass
        if "1 packets transmitted, 1 packets received" in msg:
            return True
        elif "Unknown host" in msg:
            return False
        else:
            return False


if __name__ == "__main__":
    i = inventory()

    i.add(host="i1", cluster="india", label="india")
    i.add(host="i2", cluster="india", label="gregor")
    i.add(host="d[1-4]", cluster="delta", label="delta")

    #i.list(format="json")
    #i.list(format="pprint")
    print(i.list(format="yaml"))
    i.save("test.yaml")

    n = inventory()
    n.read("test.yaml")
    print( n.list('table'))