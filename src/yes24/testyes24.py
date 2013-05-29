# -*- coding: utf-8 -*-

'''unittest for yes24 api'''


from __future__ import print_function, unicode_literals
from yes24 import Yes24
import unittest


class TestYes24(unittest.TestCase):
	def setUp(self):
		self.yes24 = Yes24(6694057)

	def tearDown(self):
		pass

	def testTitle(self):
		title = self.yes24.title
		self.assertEqual(title, '파이썬 완벽 가이드')
	
	def testAuthor(self):
		author = self.yes24.author
		self.assertEqual(author, '데이비드 M. 비즐리 저/송인철,송현제 공역 | 인사이트(insight) | 원제 : Python Essential Reference')
		
	def testPrice(self):
		price = self.yes24.price
		self.assertEqual(price, '38,000원')
		
	def testDate(self):
		date = self.yes24.date
		self.assertEqual(date, '2012년 04월 09일')
		
	def testPages(self):
		pages = self.yes24.pages
		self.assertEqual(pages, '864쪽')
		
	def testPages(self):
		weight = self.yes24.weight
		self.assertEqual(weight, '1632g')
		
	def testPages(self):
		size = self.yes24.size
		self.assertEqual(size, '188*240mm')
		
	def testUrl(self):
		size = self.yes24.url
		self.assertEqual(size, 'http://www.yes24.com/24/goods/6694057')
		
if __name__ == '__main__':
	unittest.main()