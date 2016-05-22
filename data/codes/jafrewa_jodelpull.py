import argparsefrom jodelrest import RESTClientimport osimport jsonfrom requests.exceptions import ConnectionError
__author__ = 'Jan'
parser = argparse.ArgumentParser(description='Write Jodel\' to JSON')parser.add_argument("-f", "--from-file", help="read the Location from a file", required=True)parser.add_argument("-o", "--outputfile", help="the file the Jodel's should be written to")parser.add_argument("--tor", action='store_true', help="enable to add tor support")args = parser.parse_args()
if args.from_file: if os.path.isfile(args.from_file): with open(args.from_file) as data_file:            location = json.load(data_file) else: print 'File does not exist : %s' % args.from_file exit(0)
try:    rc = RESTClient(location, None, args.tor)
 if args.outputfile:        filename = args.outputfile
 if not str(filename).endswith('.json'):            filename = "%s%s" % (filename, '.json')
 with open(filename, 'w') as outfile:            outfile.write(rc.get_posts_raw()) else: print rc.get_posts_raw()except ConnectionError: pass
