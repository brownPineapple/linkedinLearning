import requests
from geopy.geocoders import Nominatim

def printMyStuff():
    print("-"*25)

class City:
    def __init__(self, name):
        self.name = name
        self.find_city()
        self.actions()
    
    def find_city(self):
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(self.name)
        self.latitude = location.raw['lat']
        self.longitude = location.raw['lon']
        self.dbName = location.raw['display_name']
        self.shortName = location.raw['name']
        
    def get_units(self):
        temp =  input("Please choose the metrics ?\t1.Celsius OR\t2.Farenheit\nDefault: Celsius\nInput:")

        if temp == "1":
            self.units = "metric"
        elif temp == '2':
            self.units = "imperial"
        else:
            self.units = "metric"

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid=42d2d06beb65d20130647f8c5e9082af&units={self.units}")
  
        except Exception as error:
            print("Error occured: ", error)
        
        self.weather_data = response.json()
    
    def print_temperature(self):
        self.get_units()
        self.get_data()
        temp_symbol = 'C'
        if self.units == "imperial":
            temp_symbol = 'F'
        printMyStuff()
        print(f'City Name Entered - {self.name}\nAddress match - {self.dbName}\nWeather location - {self.weather_data['name']}')
        printMyStuff()
        print(f'\nThe current temperature of {self.shortName} is : {self.weather_data["main"]["temp"]}{chr(176)}{temp_symbol}\n')
        printMyStuff()
        print(f'with highs of: {self.weather_data["main"]["temp_max"]}{chr(176)}{temp_symbol} and lows of {self.weather_data["main"]["temp_min"]}{chr(176)}{temp_symbol}') 
    
    def actions(self):
        printMyStuff()
        print(f"What do you want to know about {self.name} ?")
        printMyStuff()
        res = input("1.Print full address\n2.Weather info(Summary)\n3.Weather info(Detailed)?")
        match res:
            case "1":
                pass
            case "2":
                pass
            case "3":
                self.print_temperature()
            case _:
                print("Not a valid input")
                
cityName = input("Enter a place: ")
printMyStuff()
my_city = City(cityName)
