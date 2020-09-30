import scrapy
from bs4 import BeautifulSoup

#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector import HtmlXPathSelector
#from craigslist_sample.items import CraigslistSampleItem

class QuotesSpider(scrapy.Spider):
#class QuotesSpider(CrawlSpider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for data in soup.find_all('div', attrs={'class':'quote'}):
            print(data.find('span', attrs={'class':'text'}).get_text())
            yield {'quote':data.find('span', attrs={'class':'text'}).get_text()}
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''