# import logging
import scrapy
from bs4 import BeautifulSoup as bs
from ruten.items import RutenItem
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RutenCrawler(CrawlSpider):
	name = 'ruten'
	start_urls = ['http://class.ruten.com.tw/category/sub00.php?c=00110002&p=1',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=2',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=3',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=4',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=5',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=6',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=7',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=8',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=9',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=10',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=11',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=12',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=13',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=14',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=15',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=16',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=17',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=18',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=19',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=20',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=21',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=22',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=23',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=24',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=25',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=26',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=27',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=28',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=29',\
	'http://class.ruten.com.tw/category/sub00.php?c=00110002&p=30']

	#url = 'http://class.ruten.com.tw/category/sub00.php?c=00110002&p={}'
	#for i in range(1,5):
		#url.format(i)
		#start_urls.append(url)
	#start_urls = ['http://class.ruten.com.tw/category/sub00.php?c=00110002&p=1']	
	

	# rules = [
	# 	Rule(LinkExtractor(allow=('class.ruten.com.tw/category/sub00.php?c=00110002&p=')),callback='parse',follow=True)
	# ]


	def parse(self,response):
		domainlink="http://goods.ruten.com.tw/item/show?"
		res = bs(response.body, "lxml")
		for ent in res.select('a.item-name-anchor'):
			yield scrapy.Request(ent['href'],self.parse_detail)
				
	
	def parse_detail(self, response):
		res = bs(response.body, "lxml")
		#cont = res.select('#user_generated_content iframe')[0]['src']
		#yield scrapy.Request(cont)
		#soup2 = bs(response.body, "lxml")
		#soup3=soup2.text.strip()
		#souptext =' '.join(soup3.split('\n'))
		#pattern = re.compile(r'(<!--).*(-->)') 
		#con = pattern.sub('',souptext)
      
		rutenitem = RutenItem()
		rutenitem['title'] = res.select('h2.item-title')[0].text
		rutenitem['price'] = res.select('.dollar')[0].text 
		rutenitem['nnumber'] = res.select('.text-medium.number')[0].text
		rutenitem['snumber'] = res.select('.text-medium.number')[1].text
		rutenitem['seller_name'] = res.select('.item-info-owner .seller-disc a')[0].text
		rutenitem['seller_logint'] = res.select('.item-info-owner p')[0].text
		rutenitem['seller_score'] = res.select('.item-info-owner p .text-medium')[1].text 
		rutenitem['qa_count'] = res.select('.rt-tab-pane .rt-tab-item')[1].text
		rutenitem['price_count'] = res.select('.rt-tab-pane .rt-tab-item')[2].text
		#rutenitem['content'] = con
		return rutenitem