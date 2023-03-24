# import scrapy 
# import json
# class ScraperSpider(scrapy.Spider):
#     name = 'get_cat'
#     start_urls = ['https://www.careerguide.com/career-options']
#     def parse(self,response):
        # For Categories : 
        # for category in response.css('h2.c-font-bold'):
        #     yield{
        #         'name' : category.css('a::text').get(),
        #         'link' : category.css('a').attrib['href']
        #     }
        # Category 1 , Aerospace and aviation
        # x= response.xpath('//*[@id="aspnetForm"]/div[6]/div[3]/div/div[2]/div/div[1]/div[1]/ul')
        # subcat1 = x.css('a::text').getall()
        # yield {"subcategory1" : subcat1}
        # Category 2 , Agriculture
        # x= response.xpath('//*[@id="aspnetForm"]/div[6]/div[3]/div/div[2]/div/div[1]/div[2]/ul')
        # subcat2 = x.css('a::text').getall()
        # yield {"subcategory2" : subcat2}
    