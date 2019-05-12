from ebaysdk.trading import Connection as Trading


MySandBoxToken = "AgAAAA**AQAAAA**aAAAAA**cGDXXA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4aiCZKEpA+dj6x9nY+seQ**rv4EAA**AAMAAA**erqvfmnMX5xWev0CDqWCf3Fb/0O+Qbx1u5QDrzbTaEupoqQKV11uZJe+GHet7K4luuF7jVFAiNREvXa77loj+ajjj5nfZmW0oLhZL0RLSLIdo6FQbHBcAsMciBnMIZNhmAsRAHdQ0DkELOhKPT5ShFh3+wq280TwNJVyx1VpNWRt4SFjtQY06A0x03IBL02zwSpR+Q2v5vWLVMLRNW++SLmFxjv67L/avUqPs/GS2i7eyiH+Zodpgp2Mge7qvSehLB0HHa3+JLF8RgwOZTZAY3aPgu2ET7j4/NifnJAELyN1ce1LWSrDKtF5BNEEq76hqed+RD3u1C7Sc8aZUd7cxYdsiI/c3P4QdFZ/OHM38hpkQg7E0K08m3wFhM5Mn/vV+6IxFw24vbqGpRWTGP7EmOS9CMRwYEfhQAL8ii3fmNRZQfqgPYA/Rajl7XYy7KrI+9txrmKgz/1tG5U0vSoY9PwyfkMn+F0Dv0l/NNYbq1/IVFwTWv6nS0D6/1rOkZH/ajkalzT+oyeA/CJmr5Mfi6Yi6HEL/rBppgLSUikxgbcqzUKB7a0XfN7KpI7gXZOryZ7wBbQK5CVkNhtvmwvnvksfbYN8OueI2Cocn2hrovj/f5rpNaI/burqQ3Op3YRBNQgZiDPyLhQnAIWnBYiPNkKPY5RT47ciFwDx2O8un2pKrUPDrelKA+usrQZNg8YjyOHuxtwa4Ccpth4ggLhXWAALC3aMHDusy1kSVLZxkh14M0jxObXetoXE82DufmC6"
MySandBoxCertID='SBX-eaa3d7e6295a-a29e-4fa2-99eb-ae8e'
MyDevID='da60db7a-fb35-4b1d-af99-e1d74f695fd7'
MySandBoxAppID='SMojtaba-Analyzin-SBX-2eaa3d7e6-326aafc9'


api = Trading(certid=MySandBoxCertID,devid=MyDevID,token=MySandBoxToken, appid=MySandBoxAppID, config_file=None,domain="api.sandbox.ebay.com")

request = {
        "Item": {
            "Title": "Dell Inspiron 5239 LT USA ",
            "Country": "AU",
            "Location": "AU",
            "Site": "Australia",
            "ConditionID": "1000",
            "PaymentMethods": "PayPal",
            "ListingType": "Chinese" ,
            # "ListingType": "FixedPriceItem" ,
            "PayPalEmailAddress": "nobody@gmail.com",
            "PrimaryCategory": {"CategoryID": "20713"},
            "Description": "A really nice mechanical keyboard!",
            "ListingDuration": "Days_10",
            "ItemSpecifics": {
                "NameValueList": [
                    {"Name": "Manufacturer",
                     "Value": "LG"},
                    {"Name": "Brand",
                     "Value": "LG"}
                ]},
            "StartPrice": "150",
            "Currency": "USD",
            'ProductListingDetails': {
                'BrandMPN': {
                    'Brand': 'TEST BRAND',
                    'MPN': 'U4162G04311_BLACKC9997'
                },
                'EAN': '8054241786423',
                'UPC': 885909298594,
                'IncludeStockPhotoURL': 'true',
                'IncludeeBayProductDetails': 'true',

            },
            'Quantity': 1,

            "ShippingDetails": {
                "ShippingServiceOptions": {
                    # "FreeShipping": "True",
                     "ShippingServiceCost": 12.50 ,
                    "ShippingService": "USPSMedia"
                }
            },
            "DispatchTimeMax": "3"
        }
    }

if __name__ =="__main__" :
    response = api.execute('AddItem', request)
    dictstr = response.dict()
    print(dictstr)