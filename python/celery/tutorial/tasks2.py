'''
import requests
from celery import Celery, bootsteps, Task, shared_task
from celery.bin import Option
from celery.utils.log import get_task_logger
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from tutorial.spiders.quotes_spider import QuotesSpider

logger = get_task_logger(__name__)
app = Celery("tasks2")

@app.task
def scrape_carbonite():
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(QuotesSpider)
    process.start()
'''
from billiard.context import Process
from scrapy.crawler import Crawler
from scrapy import signals
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from tutorial.spiders.quotes_spider import QuotesSpider
from celery.utils.log import get_task_logger

#from celery_app import app
from celery import Celery, bootsteps, Task, shared_task
logger = get_task_logger(__name__)
#app = Celery("tasks2")

app = Celery('tasks2', broker='amqp://localhost//', backend='db+postgresql://scrapyuser:scrapypassword@localhost/scrapy')
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    worker_max_tasks_per_child=1,
    broker_pool_limit=None
)
class CrawlerProcess(Process):
    def __init__(self, spider):
        Process.__init__(self)
        settings = get_project_settings()
        self.crawler = Crawler(spider.__class__, settings)
        self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        self.spider = spider

    def run(self):
        self.crawler.crawl(self.spider)
        reactor.run()


@app.task
#def crawl(QuotesSpider, *args, **kwargs):
def crawl(*args, **kwargs):
    spider = QuotesSpider(*args, **kwargs)
    crawler = CrawlerProcess(spider)
    crawler.start()
    crawler.join()
    