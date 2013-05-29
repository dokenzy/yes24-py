# -*- coding: utf-8 -*-

'''This is a book infomation API of Yes24.com for python 2.7.
You can get informations like title, author, price, date, pages, weight, size.
'''

from __future__ import print_function, unicode_literals
import sys
import urllib2
import re
from bs4 import BeautifulSoup as BS
from util import textstrip, value_or_msg, ERR_MESSAGES, BOOK_MESSAGES


class Yes24(object):
	'''	Yes24 API class:
	>>> yes24 = Yes24(783045)
	>>> yes24.title
	u'Corvette Fifty Years'
	>>> yes24.author
	u'Randy Leffingwell | Motorbooks International'
	>>> yes24.weight
	u'2980g'
	>>> yes24.size
	u'310*40mm'
	'''
	
	def __init__(self, bookId=None):
		if bookId:
			url = 'http://www.yes24.com/24/goods/{}'.format(bookId)
			self.book = urllib2.urlopen(url)
			if 'ExceptionNotice' in self.book.url:
				raise ValueError
			self.soup = BS(self.book)
			self.TitleDiv = self.soup.find('div', {'id': 'title'})
			self.PriceDiv = self.soup.find('div', {'class': 'priceBox'})
			self.Paper = self.soup.find('p', {'class': 'pdSize'})
		else:
			raise TypeError

	@property
	@textstrip
	def title(self):
		return self.TitleDiv.h1.text

	@property
	@textstrip
	def author(self):
		return self.TitleDiv.p.text
		
	@property
	@textstrip
	def price(self):
		return self.PriceDiv.dl.dd.text
	
	@property
	@textstrip
	def date(self):
		return self.soup.find('dd', {'class': 'pdDate'}).p.text
		
	@property
	@textstrip
	def pages(self):
		re_p = re.compile(r'(\d+)쪽')
		pages = re_p.search(self.Paper.text)
		return value_or_msg(pages)

	@property
	@textstrip
	def weight(self):
		re_p = re.compile(r'(\d+)g')
		weight = re_p.search(self.Paper.text)
		return value_or_msg(weight)
		
	@property
	@textstrip
	def size(self):
		re_p = re.compile(r'(\d+\*\d+)mm')
		size = re_p.search(self.Paper.text)
		return value_or_msg(size)
		
	@property
	@textstrip
	def url(self):
		return self.book.url


if __name__ == '__main__':
	import doctest
	doctest.testmod()
	try:
		yes24 = Yes24(6694057)
	except TypeError:
		print(ERR_MESSAGES['require_bookId'])
		sys.exit(1)
	except ValueError:
		print(ERR_MESSAGES['invalid_value'])
		sys.exit(1)
	except:
		print(ERR_MESSAGES['unknown_error'])
		sys.exit(1)
	else:
		'''
		print('title: ', yes24.title)
		print('author: ', yes24.author)
		print('price: ', yes24.price)
		print('date: ', yes24.date)
		print('pages: ', yes24.pages)
		print('weight: ', yes24.weight)
		print('size: ', yes24.size)
		print('url: ', yes24.url)
		'''