# coding:utf-8
import reimport osimport urllibimport socketimport timeimport sysimport tempfile

class TumblrSpider: RETRY_LIMIT = 5
 def __init__(self, blog, fileTypes): self.blog = blog self.baseUrl = 'http://%s.tumblr.com/page/' % self.blog self.dir = sys.path[0] + os.sep + blog self.fileTypes = fileTypes
 self.goHunting = True
 def run(self): """ """ if not os.path.isdir(self.dir):            os.mkdir(self.dir) self.__crawl()
 def __crawl(self): """ """ print u' %s \n' % self.blog        page = 1 while self.goHunting: self.__crawlPage(page)            page += 1 print
 def __crawlPage(self, page): """ """ print u' %d ' % page        url = self.__assemblePageUrl(page)        pageSrc = self.__readPage(url)        links = self.__findAllLinks(pageSrc) print u' %d ' % len(links) self.__retrieveAll(links)
 def __assemblePageUrl(self, page): """ URL """ return '%s%d' % (self.baseUrl, page)
 def __readPage(self, url): """ """        page = None
 for i in range(5): try:                response = urllib.urlopen(url)                page = response.read()                response.close() except: print u''                time.sleep(5) else: break
 if not page:            abort(u'') else: return page
 def __findAllLinks(self, page): """ """ # regex written by xiyoulaoyuanjia@Github        regex = r'(http://[0-9]{0,5}\.media\.tumblr\.com/([a-z]|[A-Z]|[0-9]){32}.*\.(%s))' % '|'.join(self.fileTypes)        result = re.findall(regex, page)
        links = []
 for match in result:            links.append(match[0])
 return links
 def __retrieveAll(self, links): """ """ for i in range(len(links)): if not self.goHunting: return
 for j in range(TumblrSpider.RETRY_LIMIT): try: print u' %d/%d' % (i + 1, len(links)) self.__retrieve(links[i]) except: print u''                    time.sleep(5) else: break
 def __retrieve(self, link): """ """        filename = self.__splitResourceName(link)
 if os.path.isfile(filename): print u'' self.goHunting = False return else:            path = self.dir + os.sep + filename self.__download(link, path)
 def __splitResourceName(self, url): """ """ return url.split('/')[-1]
 def __download(self, url, saveTo): """ """        tmp = tempfile.mktemp(".tmp")        urllib.urlretrieve(url, tmp)        os.rename(tmp, saveTo)

class Config: """ """ CONFIG_FILE = sys.path[0] + os.sep + 'config.txt'
 def initConfigFile(self): """ """        f = file(Config.CONFIG_FILE, 'w')
        blogs = ['bokuwachikuwa', 'wnderlst']        fileTypes = ['jpg', 'png', 'gif']
        blogsStr = '|'.join(blogs)        fileTypesStr = '|'.join(fileTypes)
        f.write('Blog=%s\n' % blogsStr)        f.write('FileType=%s\n' % fileTypesStr)
        f.close()
 def readConfig(self): """ """ if not os.path.isfile(Config.CONFIG_FILE): self.initConfigFile()
        f = file(Config.CONFIG_FILE, 'r')
        configFileContent = ''.join(f.readlines())
        blogsStr = re.search('Blog=(.*)\n', configFileContent).group(1)        fileTypesStr = re.search('FileType=(.*)\n', configFileContent).group(1)
        blogs = blogsStr.split('|')        fileTypes = fileTypesStr.split('|')
        dic = {'blogs': blogs, 'fileTypes': fileTypes}
        f.close()
 return dic

def abort(prompt): """ """ print prompt raw_input(u'') exit()

if __name__ == '__main__':    socket.setdefaulttimeout(30)
    config = Config()    dic = config.readConfig()
 for blog in dic['blogs']:        spider = TumblrSpider(blog, dic['fileTypes'])        spider.run() print
    abort(u'')