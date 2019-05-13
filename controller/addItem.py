__author__ = 'mojtaba.banaie'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from EbaySDK import *


class AddItemHandler(tornado.web.RequestHandler):
    def post(self):
        Title = self.get_argument('inputTitle')
        Condition = self.get_argument('inputCondition')
        Description = self.get_argument('inputDescription')
        ListingType = self.get_argument('inputListingType')
        PayPalEmailAddress = self.get_argument('inputPayPalEmailAddress')
        PrimaryCategory = self.get_argument('inputPrimaryCategory')
        Quantity = self.get_argument('inputQuantity')
        Manufacturer = self.get_argument('inputManufacturer')
        Brand = self.get_argument('inputBtrand')
        Price = self.get_argument('inputPrice')
        Currency = self.get_argument('inputCurrency')
        try :
            FreeShipping = self.get_argument('freeShipping')
        except:
            FreeShipping  = "False"
        ShippingCost = self.get_argument('shippingCost')
        ShippingAdditionalCost = self.get_argument('shippingAdditionalCost')

        request["Item"]["Title"] = Title
        request["Item"]["ConditionID"] = Condition
        request["Item"]["ListingType"] = ListingType
        request["Item"]["Description"] = Description
        request["Item"]["ItemSpecifics"]["NameValueList"][0]["Value"] = Manufacturer
        request["Item"]["ItemSpecifics"]["NameValueList"][1]["Value"] = Brand
        request["Item"]["ProductListingDetails"]["BrandMPN"]["Brand"] = Brand
        request["Item"]["Quantity"] = Quantity
        request["Item"]["PrimaryCategory"]["CategoryID"] = PrimaryCategory
        request["Item"]["PayPalEmailAddress"] = PayPalEmailAddress
        request["Item"]["StartPrice"] = Price
        request["Item"]["Currency"] = Currency
        if FreeShipping=="True":
            request["Item"]["ShippingDetails"]["ShippingServiceOptions"]["FreeShipping"] = "True"
            del request["Item"]["ShippingDetails"]["ShippingServiceOptions"]["ShippingServiceCost"]

        else :
            request["Item"]["ShippingDetails"]["ShippingServiceOptions"]["ShippingServiceCost"] = ShippingCost
            request["Item"]["ShippingDetails"]["ShippingServiceOptions"]["ShippingServiceAdditionalCost"]\
                = ShippingAdditionalCost
        response = api.execute('AddItem', request)
        dictstr = response.dict()
        if dictstr["Ack"] == "Error" :
            self.write(dictstr)
            self.finish()
        else :
            itemDetails=getItemDetails(dictstr["ItemID"])
            # itemDetails=getItemDetails("110403338122")
            # self.write(dictstr)
            self.render('addItemResult.html', itemDetails=itemDetails)
    def get(self):
        self.render('addItem.html')

