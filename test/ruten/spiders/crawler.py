# import logging
import scrapy
from bs4 import BeautifulSoup as bs
from ruten.items import RutenItem
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class RutenCrawler(CrawlSpider):
	name = 'ruten'
	start_urls = ['http://class.ruten.com.tw/category/sub00.php?c=00110013&p=1',
	'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=2',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=3',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=4',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=5',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=6',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=7',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=8',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=9',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=10',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=11',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=12',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=13',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=14',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=15',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=16',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=17',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=18',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=19',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=20',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=21',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=22',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=23',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=24',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=25',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=26',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=27',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=28',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=29',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=30',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=31',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=32',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=33',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=34',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=35',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=36',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=37',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=38',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=39',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=40',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=41',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=42',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=43',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=44',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=45',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=46',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=47',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=48',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=49',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=50',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=51',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=52',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=53',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=54',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=55',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=56',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=57',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=58',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=59',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=60',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=61',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=62',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=63',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=64',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=65',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=66',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=67',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=68',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=69',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=70',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=71',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=72',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=73',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=74',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=75',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=76',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=77',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=78',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=79',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=80',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=81',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=82',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=83',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=84',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=85',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=86',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=87',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=88',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=89',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=90',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=91',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=92',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=93',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=94',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=95',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=96',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=97',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=98',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=99',
'http://class.ruten.com.tw/category/sub00.php?c=00110013&p=100']

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