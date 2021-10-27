# Title: Weather App CIS-245 Final Project
# Author: Rhonda Rivas/Bellevue University base from CIS-245 week 9
# Date: 10-19-2021
# Description:  Your program must prompt the user for their city or zip code and request weather forecast data from
# openweathermap.org. Your program must display the weather information in an READABLE format to the user

import requests

# The method fetches the weather data and returns the result using your api key

def getLocation():
    url = "http://api.openweathermap.org/data/2.5/" # base url for fetching the weather from API 
    key = "41fbe04a4f6b918a4a2b748bd32f1a34" # your personal API key goes here

# The connection to the server and welcome or failure for connection
    try:
        response = requests.get(url)
    except:
        print("\nError: Sorry, but the connection to server failed.\n")
        exit()
    else:
        print("\nYou are now connection to server successfully!\n")
        while response.status_code != 200:
            loc = input("Ready for weather? Please enter a city or zip code: ") # Grabs the input form user
            try:
                response = requests.get(f"{url}forecast?q={loc}&appid={key}&units=imperial")
            except:
                print("\nError: Sorry, but the connection to server failed.\n") # notifies of server issue
                exit()    
            if response.status_code == 404:
                print("Error: Your city not found.") # Returns message if your city or zip wrong

        return response.json()

# This checks to see if the user gave the zip code or the city name
#  grabs from the API based on input from the user

def getForecast(location):
    url = "http://api.openweathermap.org/data/2.5/" # base url for the API
    key = "a078ddf1aaae5118ddf6a23dd2681eb0" # You API here
    zip = location["city"]["coord"]["lat"] # parameters for data
    id = location["city"]["coord"]["lon"]

    try:
        forecast = requests.get(f"{url}onecall?lat={zip}&lon={id}&appid={key}&units=imperial") #imperial for USA
    except:
        print("\nError: Sorry, but the connection to server failed.\n")
        exit()
    else:
        return forecast.json()

# displays the foecast based on the input from the user

def displayForecast(location, forecast):
    city = location["city"]["name"]
    country = location["city"]["country"]

    print(f"\nForecast for {city}, {country}:\n")
    for x in range (8):
        print(f"{'Today' if x == 0 else f'Day {x}'}:")
        print(f"\tWeather: {forecast['daily'][x]['weather'][0]['main']}")
        print(f"\tHigh: {round(forecast['daily'][x]['temp']['max'])}F")
        print(f"\tLow: {round(forecast['daily'][x]['temp']['min'])}F")
    
# Asks the user if they want to grab another forecast 
# returns additional forecasts based on user input

def main():
    response = "yes"
    print("\nWelcome! to Rhonda's Weather APP!")

    while response == "yes" or response == "y":
        location = getLocation()
        forecast = getForecast(location)
        displayForecast(location, forecast)

        response = input("\nWould you like to check the forcast for another city? (yes or no): ")
        while response != "yes" and response != "y" and response != "no" and response != "n":
            print("Error: invalid entry")
            response = input("Would you like to check the forcast for another city? (yes or no): ")
# Thanks the user for using the service and says goodbye

    print("\nGoodbye! Adios! Have a Great day!\n")

if __name__ == "__main__":
    main()
