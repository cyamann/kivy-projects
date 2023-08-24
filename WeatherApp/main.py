import requests
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350,600)
kv='''
MDFloatLayout:
    md_bg_color: 1,1,1,1
    Image:
        source: "assets/location.jpg"
        size_hint: .3, .3
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
    MDLabel:
        id: location
        text: ""
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        halign: "center"
        font_size: "20sp"
    Image:
        id: weather_image
        source: ""
        size_hint: .3, .3
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
    MDLabel:
        id: tempature
        text: ""
        markup: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        halign: "center"
        font_size: "20sp"
    MDLabel:
        id: weather
        text: ""
        source: ""
        markup: True
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        halign: "center"
        font_size: "20sp"
    MDFloatLayout:
        pos_hint: {"center_x": 0.2, "center_y": 0.45}
        size_hint: .22, .1
        Image:
            source: "assets/humidity.png"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            id: humidity
            text: ""
            pos_hint: {"center_x": 1.2, "center_y": 0.7}
            halign: "center"
            font_size: "14sp" 
        MDLabel:
            text: "Humidity"
            pos_hint: {"center_x": 1.2, "center_y": 0.3}
            halign: "center"
            font_size: "14sp"    
    MDFloatLayout:
        pos_hint: {"center_x": 0.7, "center_y": 0.45}
        size_hint: .22, .1
        Image:
            source: "assets/foggy.png"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
        MDLabel:
            id: wind_speed
            text: ""
            pos_hint: {"center_x": 1.2, "center_y": 0.7}
            halign: "center"
            font_size: "14sp" 
        MDLabel:
            text: "Windy"
            pos_hint: {"center_x": 1.2, "center_y": 0.3}
            halign: "center"
            font_size: "14sp"  
    MDFloatLayout:
        size_hint_y: .3
        canvas:
            Color:
                rgb: rgba(148,117,255,255)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [10,10,0,0]
        MDFloatLayout:  
            pos_hint: {"center_x": .5, "center_y": .71}  
            size_hint: .9,.32
            canvas:
                Color:
                    rgb: rgba(131,69,255,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
            TextInput:
                id: city_name
                hint_text: "Enter City Name"
                size_hint: 1,None
                pos_hint: {"center_x": .5, "center_y": .5}  
                height: self.minimum_height
                multiline: False
                font_size: "20sp"
                hint_text_color: 1,1,1,1
                foreground_color: 1,1,1,1
                background_color: 1,1,1,0
                padding: 15
                cursor_color: 1,1,1,1
                cursor_width: "2sp"
                halign: "center"
        Button:
            text: "Get Weather"
            font_size: "20sp"
            size_hint: .9,.32
            pos_hint: {"center_x": .5, "center_y": .29} 
            background_color: 1,1,1,0
            color : rgba(148,117,255,255)
            on_release: app.search_weather()
            canvas.before:
                Color:
                    rgb: 1,1,1,1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]


'''
class WeatherApp(MDApp):
    api_key= "e59ec130254ef94a193b235ab35a9704"
    def build(self):
        return Builder.load_string(kv)
    def get_weather(self,city_name):
        try:
            url= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"
            response = requests.get(url)
            x = response.json()
            print(x)
            if x["cod"] != "404":
                tempature = round(x["main"]["temp"] - 273)
                humidity = x["main"]["humidity"]
                weather = x["weather"][0]["main"]
                id = int(x["weather"][0]["id"])  # Convert to integer
                wind_speed = round(x["wind"]["speed"] * 3.6)
                location = x["name"] + ", " + x["sys"]["country"]
                self.root.ids.tempature.text = f"[b]{tempature}[/b]° [b]Celcius[/b]"
                self.root.ids.weather.text = str(weather)
                self.root.ids.humidity.text = f"{humidity}%"
                self.root.ids.wind_speed.text = f"{wind_speed} km/h"
                self.root.ids.location.text = location

                if id == 800:
                    self.root.ids.weather_image.source = "C:\\Users\\Ceren.CEREN\\PycharmProjects\\WeatherApp\\assets\\sunny.jpg"
                elif 200 <= id <= 232:
                    self.root.ids.weather_image.source = "assets/storm.png"
                elif 300 <= id <= 321 or 500 <= id <= 531:
                    self.root.ids.weather_image.source = "assets/rainy.jpg"
                elif 600 <= id <= 622:
                    self.root.ids.weather_image.source = "assets/snow.png"
                elif 700 <= id <= 781:
                    self.root.ids.weather_image.source = "assets/haze.png"
                elif 801 <= id <= 804:
                    self.root.ids.weather_image.source = "assets/cloudy.jpg"

            else:
                print("City Not Found")
        except requests.ConnectionError:
            print("No Internet Connection")

    def search_weather(self):
        city_name = self.root.ids.city_name.text
        if city_name != "":
            self.get_weather(city_name)


if __name__ == "__main__":
    WeatherApp().run()
