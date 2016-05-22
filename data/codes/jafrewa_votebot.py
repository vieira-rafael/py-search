from jodelrest import RESTClientfrom tqdm import *import json
__author__ = 'Jan'
uni = {"latitude": 53.107, "longtitude": 8.853, "city": "Bremen"}


rc = RESTClient(uni, None)posts = rc.get_posts()rc.close()
for post in posts: if 'children' in post: print "[Comments : %s] [Votes : %s]" % (len(post['children']), post['vote_count']) #for comment in  post['children']: #    print "Kommentar : %s" % comment else: print "[Comments : 0] [Votes : %s]" % post['vote_count']
 print '%s' % (post['message'].encode('UTF-8'))    var = str(raw_input("[ up / down / comment / view / exit ] : "))
    commands = {'up', 'down', 'comment', 'view','exit'}
 if var == 'exit': break
 id = post['post_id']
 if var not in commands: '\n\n----------------------------\n' continue elif var =='exit': break elif var == 'comment':        comment = str(raw_input('# Comment ? '))        rc.post_comment(id, comment) print '\n\n----------------------------\n' elif var == 'view': if 'children' not in post: print "No comments ! \n\n----------------------------\n" continue for comment in  post['children']: print "[%s] %s\n" % (comment['vote_count'],comment['message'].encode('UTF-8')) else:        amount = int(raw_input('# Wie viel ? ')) for i in tqdm(range(amount)):            rc = RESTClient(uni, None) try: if var == "up":                    rc.upvote(id) elif var == "down":                    rc.downvote(id) except ValueError: print "! Vote Fehler !"                rc.close()
 continue            rc.close() print '\n\n----------------------------\n'