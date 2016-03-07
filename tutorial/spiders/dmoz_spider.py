import scrapy
import re

from tutorial.items import Website
from tutorial.items import MPInfo

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["publications.parliament.uk"]
    start_urls = [
        "http://www.publications.parliament.uk/pa/cm/cmregmem/160208/contents.htm"
    ]

    def parse(self, response):
        for site in response.xpath("//div[@id='mainTextBlock']/p[not(@class='atozLinks')]//a"):
            url = 'http://www.publications.parliament.uk/pa/cm/cmregmem/160208/' + site.xpath('@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse_dir_contents)
    
    def parse_dir_contents(self, response):
        for sel in response.xpath("//div[@id='mainTextBlock']"):
            item = MPInfo()
            item['name'] = sel.xpath('//h2/text()').extract_first()
            content = sel.xpath('//div[@id="mainTextBlock"]//p/strong/text() | //div[@id="mainTextBlock"]//p/text()').extract()
            
            currentCase = -1
            collector = []
            items = []
            
            for chunk in content:
                matchObj = re.match("^([0-9])\. .*", chunk)
                if matchObj is not None:
                # Heading line
                    number = matchObj.group(1)
                    if (number != currentCase):
                    # Reached a new heading
                        items.append(collector)
                    currentCase = number
                    # Reset collector
                    collector = [number]
                else:
                    # Not a heading line, don't match any preamble
                    if (currentCase != -1):
                        collector.append(chunk)
            
            item['Family'] = items   
            # import re
            # if re.match("^[0-9]\. .*", line):
            #    Do Something
            
            # for idx in range(0, len(content)):
            #     chunk = content[idx]
            #     if chunk.startswith('1. ') :
            #         if not content[idx+1].startswith('2. '):
            #             item['EmploymentAndEarnings'] = content[idx+1]
            #     if chunk.startswith('2. ') :
            #         if not content[idx+1].startswith('3. '):
            #             item['Support'] = content[idx+1]
            #     if chunk.startswith('3. ') :
            #         if not content[idx+1].startswith('4. '):
            #             item['OtherSupport'] = content[idx+1]
            #     if chunk.startswith('4. ') :
            #         if not content[idx+1].startswith('5. '):
            #             item['VisitsOutsideUK'] = content[idx+1]
            #     if chunk.startswith('5. ') :
            #         if not content[idx+1].startswith('6. '):
            #             item['GiftsOutsideUK'] = content[idx+1]
            #     if chunk.startswith('6. ') :
            #         if not content[idx+1].startswith('7. '):
            #             item['LandAndProperty'] = content[idx+1]
            #     if chunk.startswith('7. ') :
            #         if not content[idx+1].startswith('8. '):
            #             item['Shareholdings'] = content[idx+1]
            #     if chunk.startswith('8. ') :
            #         if not content[idx+1].startswith('9. '):
            #             item['Miscellaneous'] = content[idx+1]
            #     if chunk.startswith('9. ') :
            #         # if content[idx+1].startswith('3. '):
            #         item['Family'] = content[idx+1]
            
            yield item
            
            
#
# import re
# if re.match("^[a-zA-Z]+.*", line):