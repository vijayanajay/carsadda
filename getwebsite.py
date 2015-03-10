from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import logging

logging.basicConfig()

log_handler = FileHandler('application.log')

def make_soup(url):
	html = urlopen(url)
	log_handler.info('Hello World!')
	log_handler.warn('Hello World!')
	html_contents = html.read()
	return BeautifulSoup(html_contents, "lxml")

if __name__ == '__main__':
	url = "http://www.team-bhp.com/forum/test-drives-initial-ownership-reports/148583-2014-fiat-linea-facelift-test-drive-review.html"

	soup = make_soup(url)
	f = open('workfile.tmp', 'w')

 	regex = re.compile('post_message_.*')
  	post = soup.find_all(id=re.compile('post_message_'))
 

 	print >> f, post
