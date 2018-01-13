import scrapy
from JD_selenium.items import JingDongItem
class JD_Wheel_Spider(scrapy.Spider):
    name = "wheel"
    allowed_domains = ["www.jd.com"]
    # start_url = ["http://www.jd.com/"]
    search_url1 = "https://search.jd.com/Search?keyword={key}&enc=utf-8&page={page}"
    
    def start_requests(self):
        key = "轮毂"
        for num in range(1, 5):
            page1 = str(num*2-1)
            yield scrapy.Request(url=self.search_url1.format(key=key, page=page1), callback=self.parse_one)
            
    def parse_one(self, response):
        all_goods = response.xpath('//div[@id="J_goodsList"]/ul/li')

        for one_good in all_goods:
            item = JingDongItem()
            # try:
            item['title'] = one_good.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()').extract()
            item['comment_count'] = one_good.xpath('div/div[@class="p-commit"]/strong/a/text()').extract()
            item['shop_url'] = one_good.xpath('div/div[@class="p-shop"]/span/a/@href').extract()
            item['goods_url'] = one_good.xpath('div/div[@class="p-name p-name-type-2"]/a/@href').extract()
            item['price'] = one_good.xpath('div/div[@class="p-price"]/strong/i/text()').extract()
            yield item

        print("A\nA\nA\nA\nA\n")
        print(len(all_goods))