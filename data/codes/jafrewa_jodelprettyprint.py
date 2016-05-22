import sysimport dateutil.parserimport textwrapimport simplejson as json
__author__ = 'xai'

def print_post(post, indent=0):    date = dateutil.parser.parse(post['created_at']).strftime("%c")    message = textwrap.fill(post['message'].encode('UTF-8'), width=(80 - indent), initial_indent=indent * ' ' + '| ', subsequent_indent=indent * ' ' + '| ') print '%s,----[ %s ]%s\n%s\n\n' % (indent * ' ', date, (50 - indent) * '-', message)
 try: for child in post['children']:            print_post(child, indent + 4) except KeyError: pass

dump = json.load(sys.stdin)
for post in reversed(dump['posts']):    print_post(post, 0)