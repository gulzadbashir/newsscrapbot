import scrapy
from tolonews.items import NewsItem


class ToloSpider(scrapy.Spider):
    name = "tolospider"
    allowed_domains = ["tolonews.com"]
    start_urls = ["https://tolonews.com"]

    def parse(self, response):
        newss = response.css('.content-article')
        for newsss in newss:
            relative_url = newsss.css('.content-article h3 a::attr(href)').get()
            if relative_url is not None:news_url = 'https://tolonews.com' + relative_url
            yield response.follow(news_url, callback= self.news_parse)
    def news_parse(self, response):
        tolonews = 'https://tolonews.com'
        news_item = NewsItem()


        
        news_item['title'] = response.xpath('.//*[@id="wrapper"]/div[1]/article/div/div/div[1]/div[2]/div[1]/div[1]/div/div/div/h2//text()').extract(),
        news_item['image'] = (tolonews+str(response.css('.img-wrap img::attr(src)').get())),
        news_item['url'] = response.url,
        news_item['text'] = response.xpath('//*[@id="wrapper"]/div[1]/article/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[1]//text()').extract()

        yield news_item