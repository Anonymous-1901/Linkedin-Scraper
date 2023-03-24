import scrapy 
import json

class ScraperSpider(scrapy.Spider):
    name = 'jobs_scraper'
    start_urls = []
    #Read Sub-Categories from the 2 files we created i.e sub1 and sub2 
    with open("sub1.json","r") as f:
        data = json.load(f)
        sub_urls = data[0]["subcategory1"]
    with open("sub2.json","r") as f:
        data = json.load(f)
        #Merging all subcategories into 1 list to make it easier to append
        sub_urls += (data[0]["subcategory2"])
    for i in range(0,len(sub_urls)):
        #Replace spaces with '-' as it is a URL 
        var = sub_urls[i].replace(' ','-')
        #Adding the Subcategory into search url
        start_urls.append(f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={var}&location=Maharashtra"
                          "&trk=public_jobs_jobs-search-bar_search-submit&start=0")    

    def parse(self,response):
        # data = response.css('section.two-pane-serp-page__results-list').css('a').css('span::text').getall()
        # yield {"data":data}
        job_item = {}
        jobs = response.css("li")

        num_jobs_returned = len(jobs)
        print("******* Num Jobs Returned *******")
        print(num_jobs_returned)
        print('*****')
        #Format and extract all the information from the css 
        for job in jobs:
            job_item['job_position'] = job.css("h3::text").get(default='not-found').strip()
            job_item['job_detail_url'] = job.css(".base-card__full-link::attr(href)").get(default='not-found').strip()
            job_item['company_name'] = job.css('h4 a::text').get(default='not-found').strip()
            #Gathering company link here which we'll use later to exract company info
            job_item['company_link'] = job.css('h4 a::attr(href)').get(default='not-found')
            job_item['company_location'] = job.css('.job-search-card__location::text').get(default='not-found').strip()
            #Find if the job is remote or WFH , by checking if Work from home is mentioned in the description
            if "home" in job_item["job_position"].lower():
                job_item['job_location'] = "Remote"
            else:
                job_item['job_location'] = job.css('.job-search-card__location::text').get(default='not-found').strip()
            yield job_item