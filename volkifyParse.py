from bs4 import BeautifulSoup
import requests

def openHTML(url):
	return requests.get(url).content
	
def getPhrase(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='UTF-8')

	return soup.select('blockquote p')[0].string

def getAuthor(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='UTF-8')	

	return soup.select('blockquote footer a')[0].string
