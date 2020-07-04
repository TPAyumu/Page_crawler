import scrapy


class spider(scrapy.Spider):
    name = "spiderman"
    base_url = "https://learnjapanesedaily.com/most-common-japanese-words.html/"
    current_page = "1"
    for i in range(1, 19):
        start_urls = [base_url + current_page]

        if current_page == "1":
            def parse(self, response):
                for x in range(6, 66):
                    for p in response.xpath("//p/text()")[x].getall():
                        yield {"list: ": p}

        elif current_page == "17":
            def parse(self, response):
                for x in range(4, 44):
                    for p in response.xpath("//p/text()")[x].getall():
                        yield {"list: ": p}

        else:
            def parse(self, response):
                for x in range(4, 64):
                    for p in response.xpath("//p/text()")[x].getall():
                        yield {"list: ": p}

        current_page = str(i)
