import requests
import json
import random
import webbrowser

api_key = ##API KEY##
headers = {'Authorization': 'Bearer %s' % api_key}


""" Can take in 2 args; Term which is type of establishment and location
    RETURNS JSON text of the search results"""
def do_search(location, price_desired, term = 'restaurant', open_now = 'True'):
  url='https://api.yelp.com/v3/businesses/search'
  params={'term': term, 'location': location, 'radius':'8000', 'open_now':open_now, 'price': price_desired}
  req = requests.get(url, params=params, headers=headers)
  parsed = json.loads(req.text)
  return parsed

""" Takes in a json string and returns a list of restuarant dictionary objects """
def extract_bus(json_text):
  return json_text["businesses"]

""" takes in json_text as arg, returns nothing prints out list of businesses in a pretty form """
def prettify_list(list_of_bus):
  count = 1
  for business in list_of_bus:
      print("{}_________________".format(count))
      print("Name:", business["name"])
      print("Rating:", business["rating"])
      print("Address:", " ".join(business["location"]["display_address"]))
      print("Phone:", business["phone"])
      print("URL: ", business["url"])
      print("\n")
      count += 1

""" Takes json_text as argument
returns dictionary of a randomly selected restaurant """
def randomly_select(list_of_bus):
  return(random.choice(list_of_bus))

""" Takes a restuarant dict object and prints a prettify string version of it"""
def prettify_one(rest_dict):
    print("Name:", rest_dict["name"])
    print("Rating:", rest_dict["rating"])
    print("Address:", " ".join(rest_dict["location"]["display_address"]))
    print("Phone:", rest_dict["phone"])
    print("URL: ", rest_dict["url"])

""" Overarching function that allows user to type in their location and randomly select a restaurant and prints out that restaurant's info"""
def get_random_restaurant(location , price_d , type_of_restaurant = 'restaurant', open_now = 'True' ):
  json_ug = do_search(location, price_d, type_of_restaurant, open_now, )
  buses = extract_bus(json_ug)
  rest = randomly_select(buses)
  return(rest)

"""Given restaurant dict object, open webpage to restaurant"""
def open_webpage(rest):
  webbrowser.open(rest['url'], new = 1)

  

def get_list_of_restaurants(location ,price_d ,  type_of_restaurant = 'restaurant', open_now = 'True'):
  json_ug = do_search(location, price_d, type_of_restaurant, open_now )
  buses = extract_bus(json_ug)
  prettify_list(buses)  

""""""
def open_bool(open_now):
    if open_now.lower().startswith("y") == True:
        return 'True'
    else:
        return 'False'
        

if __name__ == "__main__":
    
    print("RANDOM RESTAURANT SEARCHER")
    print()
    type_of_food = input('PLEASE ENTER TYPE OF BUSINESS: ')
    location = input("PLEASE ENTER LOCATION OF YOUR SEARCH: ")
    price_range = input("PLEASE ENTER PRICE RANGE(1 = $, 2 = $$, 3 = $$$): ")
    open_now = open_bool(input("OPEN NOW? (Y/N): "))
    print()
    print("YOUR RESULTS")
    print()
    get_random_restaurant(location, price_range, type_of_food, open_now)
    get_list_of_restaurants(location, price_range, type_of_food, open_now)
    
