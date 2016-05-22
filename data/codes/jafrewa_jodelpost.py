from jodelrest import RESTClientimport Tkinterimport tkFileDialogfrom tqdm import *import sysimport time__author__ = 'Jan'

class JodelPost(object): def __init__(self, location, auth=None):
 if auth is None: self.client = RESTClient(location, None) else: self.client = RESTClient(location, auth) self.last_post = None self.location = location
 def change_location(self, location): self.client.set_pos(location['longtitude'], location['latitude'], location['city']) self.location = location
 def post_image(self, image): self.client.post_image(image) self.set_last_post(self.client.get_posts())
 def post_text(self, text): self.client.post(text) self.set_last_post(self.client.get_posts())
 def set_last_post(self, posts): for post in posts: if post['post_own'] == 'own': self.last_post = post['post_id'] break
 def get_posts(self): return self.client.get_posts()
 def boost_post(self, votes): for i in tqdm(range(votes)):            tmpClient = RESTClient(self.location, None)            tmpClient.upvote(self.last_post)            tmpClient.close()


uni = {"latitude": 53.107, "longtitude": 8.853, "city": "Bremen"}post = JodelPost(uni)
menuInput = 0
while menuInput <= 0 or menuInput > 3: print '1) Bild posten\n2) Text posten\n\n3) Beenden\n' try:        menuInput = int(raw_input('Auswahl ? : ')) except ValueError: continue
if menuInput == 3: exit()elif menuInput == 2:    text = str(raw_input('Text ? :\n')).decode(sys.stdin.encoding)    post.post_text(text)elif menuInput == 1:    root = Tkinter.Tk()    root.withdraw()
 # Make it almost invisible - no decorations, 0 size, top left corner.    root.overrideredirect(True)    root.geometry('0x0+0+0')
 # Show window again and lift it to top so it can get focus, # otherwise dialogs will end up behind the terminal.    root.deiconify()    root.lift()    root.focus_force()    myFormats = [        ('Portable Network Graphics','*.png'),        ('JPEG / JFIF','*.jpg'),    ] file = tkFileDialog.askopenfilename(parent=root, title='Choose a file', filetypes=myFormats)    root.destroy() if file is not None:        post.post_image(str(file)) else: print 'Beendet'
boost = str(raw_input('Post boosten ? [J/N]\n'))
if boost == 'J': print 'Bitte warten!'
 for i in tqdm(range(10)):        time.sleep(1)    post.set_last_post(post.get_posts()) print '\n' while True:        amount = raw_input('Wie viel ? \n') try:            amount = int(amount) except ValueError: continue break    post.boost_post(amount)