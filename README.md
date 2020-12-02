# data_extraction_03_scrapy

install scrapy
* I am using anaconda python to install scrapy

create project & spider
* scrapy startproject zillow
* scrapy genspider zillow www.zillow.com 

commands to run:
* cd PATH/TO/data_extraction_03_scrapy/zillow
* scrapy crawl zillow -O house.json