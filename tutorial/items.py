# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
    
class Website(Item):

    name = Field()
    url = Field()

# class Interests(Item):
#     EmploymentAndEarnings = Field()
#     Support = Field()
#     OtherSupport = Field()
#     VisitsOutsideUK = Field()
#     GiftsOutsideUK = Field()
#     LandAndProperty = Field()
#     Shareholdings = Field()
#     Miscellaneous = Field()
#     Family = Field()
    
class MPInfo(Item):
    name = Field()
    info = Field()
    EmploymentAndEarnings = Field()
    Support = Field()
    OtherSupport = Field()
    VisitsOutsideUK = Field()
    GiftsOutsideUK = Field()
    LandAndProperty = Field()
    Shareholdings = Field()
    Miscellaneous = Field()
    Family = Field()

