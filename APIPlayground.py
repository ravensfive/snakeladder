import urllib.request, requests, json

# google HTML
def googlecall():
      # make call and load url details into a python object
      webUrl = urllib.request.urlopen("http://www.google.com")
      # print result code
      print(webUrl.getcode)
      # 200 status code == successful call i.e. if the website is down, don't knock over the code
      if webUrl.getcode() == 200:
          # read date into python object
          data = webUrl.read()
          # print data
          print(data)

# tested and works - will return the google html code
#googlecall()

# now lets make a REST API call and retrieve some meaningful data
# open weather map API key = d47b0cd338da497609d15108a305e3ca
# this free account permits 60 api calls a day and then will start throwing a different status code
# API documentation here : https://openweathermap.org/current#current_JSON
def callAPI():
    # eventually I will make the city dynamic, at the moment it is hardcoded to London 
    City = input("Which UK city would you like the weather for?")
    # specific call on a city ID
    # r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=2172797&APPID=d47b0cd338da497609d15108a305e3ca')
    # specific call on a city by name
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=london,uk&APPID=d47b0cd338da497609d15108a305e3ca')
    # specific call by longitude and latitude
    # r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&APPID=d47b0cd338da497609d15108a305e3ca')
    
    # test if API call was successful, if not unsuccessful message thrown
    if r.status_code == 200:    
        # load data in json format
        weatherdata = r.json()
        print(weatherdata)

        # intepret the json file    
        cityname = weatherdata["name"]
        country = weatherdata["sys"]["country"]
        weathersummary = weatherdata["weather"][0]["main"]
        weatherdescription = weatherdata["weather"][0]["description"]

        # print results
        print("The weather in " + cityname + ", " + country, " is " + weathersummary + " and " + weatherdescription)

    else :
        # print error message
        print("Could not retrieve weather for that location")

callAPI()
