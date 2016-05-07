# _*_ coding:utf-8 _*_

import json
import traceback
from bs4 import BeautifulSoup
import requests

def get_files(full_name):
	try:
		links = []
		html_page = requests.get('https://github.com/'+full_name)
		
		soup = soup_wrap(html_page)

		file_wrap = soup.findAll("div", { "class" : "file-wrap" })

		for row in file_wrap:
			links = links + row.findAll('a', href = True)
		
		for link in links:
			if ".py" in link['href']:
				print(link['title'])
			if 'tree' in link['href']:
				print(link)
				if 'title' in link:
					print(link['title'])

	except UnicodeEncodeError:
		traceback.print_exc()
		pass

def get_code(url):
	print('bela')


def soup_wrap(url):
	git_content = str(url.content, "ascii", errors="ignore")

	soup = BeautifulSoup(git_content, 'html.parser')
	return soup


def main():
    try:
    	for index in range(1,129):
    		__file__ = '../data/repos/page'+ str(index)
	    	with open(__file__, 'r') as jsonfile:
	    		items_list = json.load(jsonfile)['items']
	    		for item in items_list:
	    			get_files(item['full_name'])
	    			break  
	    	break		
    except:
    	traceback.print_exc()
    	pass	

if __name__ == "__main__":
    main()
