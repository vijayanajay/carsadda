from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import logging
from goose import Goose
logger = logging.getLogger(__name__)

def extract(url):
	logger.info ("inside extract function")
	goose = Goose()
	article = goose.extract(url=url)
	logger.debug (article.cleaned_text)
	return (article)

def clean_post(post):
	return ("nothing")

#Redundant - no more applicable since we are using the "goose" library now
'''def make_soup(url):
	logger.info ("Entering make_soup")

	#create the soup from the url that is the input
	html_contents = urlopen(url).read().decode('latin-1')

	# Replace all doubled-up <BR> tags with <P> tags
	replaceBrs = re.compile("<br */? *>[ \r\n]*<br */? *>")
   	html_contents = re.sub(replaceBrs, "</p><p>", html_contents)

   	#Repalce all <a...> with <p>
   	replaceAhRefs_begin = re.compile("<a.*?>")
   	replaceAhRefs_end = re.compile("</a>")
   	html_contents = re.sub(replaceAhRefs_begin, "<p>", html_contents)
   	html_contents = re.sub(replaceAhRefs_end, "</p>", html_contents)
	
   	#Replace all <img> tags with blank
   	replaceImg = re.compile("<img.*?>")
   	html_contents = re.sub(replaceImg, "", html_contents)

	#Remove all <p></p> tags with less than 15 chars in them
	replaceIrrelevantPara = re.compile("<p>.{2,25}?</p>")
	html_contents = re.sub(replaceIrrelevantPara, "", html_contents)

	logger.debug(html_contents)

	return BeautifulSoup(html_contents, "lxml") '''

#Redundant - no more applicable since we are using the "goose" library now
''' def get_soup(url):
	#find all the individual posts and dump it into a soup
	logger.info ("Entering get_soup")
	soup = make_soup(url)

	# remove all the scripts in the html
	for s in soup.find_all("script"):
		s.extract()

 	post = soup.find_all("p")

 	#logger.debug (post)
 	return (post)   '''

if __name__ == '__main__':
	url = "http://www.team-bhp.com/forum/test-drives-initial-ownership-reports/148583-2014-fiat-linea-facelift-test-drive-review.html"

	soup = make_soup(url)
	f = open('workfile.tmp', 'a')

 	post = get_soup(url)
