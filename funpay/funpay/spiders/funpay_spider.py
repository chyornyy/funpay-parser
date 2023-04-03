import scrapy
from tqdm import tqdm


class FunpaySpider(scrapy.Spider):
    name = "funpay"

    def start_requests(self):
        print('Give me the URL of the lot you need information about: ')
        urls = [
            input()
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lots = response.css('a.tc-item')
        with tqdm(total=len(lots)) as pbar:
            for lot in lots:
                pbar.update(1)
                yield {
                    'username': lot.css('div.media-user-name::text').get().replace(' ', '').replace('\n', ''),
                    'price': lot.css('div.tc-price::int').get().replace(' ', '').replace('\n', ''),
                    'unit': lot.css('div.tc-price span.unit::text').get().replace('\u20bd', 'RUB'),
                    'amount-items-to-sell': lot.css('div.tc-amount::text').get(),
                    'description': lot.css('div.tc-desc-text::text').get().encode('ascii', 'ignore').decode(),
                    '5stars-count': lot.css('span.rating-mini-count::text').get(),
                    'on-site:': lot.css('div.media-user-info::text').get(),
                }
