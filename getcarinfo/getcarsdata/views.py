from django.shortcuts import render 
import getwebsite
import logging
logger = logging.getLogger(__name__)

def index (request):
	url = "http://www.topgear.com/india/our-car-reviews/linea?id=2833"
	#post_text = get the results from soup based on the url above
	post_text= getwebsite.get_soup(url)
	
	# the return from get_soup is a ResultSet (list). That needs to be converted to dictionary to send to the html
	context = {'post_text': post_text}

	#return the dictionary to the html
	return render(request,'getcarsdata/index.html', context)

# Create your views here.