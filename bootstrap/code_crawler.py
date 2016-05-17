# _*_ coding:utf-8 _*_

import traceback
from bs4 import BeautifulSoup
import requests
import json

class CodeCrawler:


	def soup_wrap(self, url):
		git_content = str(url.content, "ascii", errors="ignore")

		soup = BeautifulSoup(git_content, 'html.parser')
		return soup


	def get_files(self, full_name):
		try:
			links = []
			html_page = requests.get('https://github.com/'+full_name)
			
			soup = self.soup_wrap(html_page)

			file_wrap = soup.findAll("div", { "class" : "file-wrap" })

			for row in file_wrap:
				links = links + row.findAll('a', href = True)
			
			for link in links:
				if ".py" in link['href']:
					self.get_code(link['href'])
				elif 'tree' in link['href'] and link.has_attr('title'):
					self.get_files(link['href'])
		except UnicodeEncodeError:
			traceback.print_exc()
			pass
	
	def get_code(self, url):
		filename = "data/codes/" +str(url.split('/')[1])+ "_" +str(url.split('/')[-1])
		print(filename)
		html_page = requests.get('https://github.com/'+url)		
		soup = self.soup_wrap(html_page)
		code_wrap = soup.findAll("td", { "class" : "blob-code" })

		f = open(filename, "w")
		for row in code_wrap:
			f.write(row.text)
		f.close()

	def __init__(self):
		try:
			for index in range(1,32):
				__file__ = 'data/repos/page'+ str(index)
				with open(__file__, 'r') as jsonfile:
					for item in json.load(jsonfile)['items']:
						self.get_files(item['full_name'])
		except:
			traceback.print_exc()
			pass