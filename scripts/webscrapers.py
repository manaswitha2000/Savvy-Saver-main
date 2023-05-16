# import requests as req
from bs4 import BeautifulSoup
from requests_html import HTMLSession

req = HTMLSession()
headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows 95; BCD2000)'}

def sort_name(name):
    """ removes whitespace from product name"""
    name_list = name.split()
    sorted_name = " ".join(name_list)
    return sorted_name


def create_soup_page(url):
    webpage = req.get(url)
    # webpage_text = webpage.text
    soup = BeautifulSoup(webpage.content, "html.parser")
    return soup


# def flipkart_scrape(url):
#     """returns the item price for a flipkart product"""
#     soup = create_soup_page(url)
#     try:
#         price_units = soup.find("p", class_="pricePerUnit").getText().strip()
#         product_price = price_units.partition("/")[0]
#         if "p" in product_price:
#             product_price_pence = product_price.replace("p", "")
#             product_price_final = float(product_price_pence)/100
#         else:
#             product_price_final = price_units.partition("/")[0][1:]
#
#         return product_price_final
#
#     except AttributeError:
#         print("Failed- investigate: {}".format(url))

def flipkart_scrape(url):
    soup = create_soup_page(url)
    # title = soup.find("span", {"id":"productTitle"}).text.strip()
    #print("Amazon url {}".format(url))
    price_element = soup.find("div", attrs = {"class":"_30jeq3 _16Jk6d"}).text
    # print(title)
    # price_element = soup.find('span', {'class': 'a-price-whole'})
    print("FPRICE...............", price_element)
    #print("Amazon url {}".format(url))
    if price_element:
        return price_element

    return 0

# def amazon_scrape(url):
#     """returns the item price for a amazon product"""
#     soup = create_soup_page(url)
#     try:
#         product_description = soup.find("div", class_="related-search-ribbon-enabled")

#         try:
#             product_price_raw = product_description.find(class_="nowPrice").getText()
#             product_price = product_price_raw.strip()[1:]
#         except AttributeError:
#             # If the nowPrice isn't available it means the product is on offer.
#             product_price_raw = product_description.find(class_="typicalPrice").getText()
#             product_price = product_price_raw.strip()[1:]

#         return product_price
#     except AttributeError:
#         print("Failed- investigate: {}".format(url))
    # price_element = soup.find('span', {'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})

    # if price_element:
    #     # Extract the price value
    #     price = price_element.get_text().strip()
    #     return price

    # return 'Price not found'
def amazon_scrape(url):
    soup = create_soup_page(url)
    # title = soup.find("span", {"id":"productTitle"}).text.strip()
    #print("Amazon url {}".format(url))
    price_element = soup.find('span', {"class":"a-price-whole"}).text
    # print(title)
    # price_element = soup.find('span', {'class': 'a-price-whole'})
    print("APRICE...............", price_element)
    #print("Amazon url {}".format(url))
    if price_element:
        return price_element

    return 0

def jiomart_scrape(url):
    soup = create_soup_page(url)
    # title = soup.find("span", {"id":"productTitle"}).text.strip()
    #print("Amazon url {}".format(url))
    price_element = soup.find("li", attrs = {"class":"pdp__priceSection__priceListText"}).text
    # print(title)
    # price_element = soup.find('span', {'class': 'a-price-whole'})
    print("JPRICE...............", price_element)
    #print("Amazon url {}".format(url))
    if price_element:
        return price_element

    return 0
