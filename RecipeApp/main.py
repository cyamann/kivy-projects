import requests
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350,600)
kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1

    MDFloatLayout:
        size_hint_y: .3
        canvas:
            Color:
                rgb: rgba(148, 117, 255, 255)
            RoundedRectangle:
                size: self.size
                pos: self.pos

        MDFloatLayout:  
            pos_hint: {"center_x": .5, "center_y": .5}  
            canvas:
                RoundedRectangle:
                    size: self.size
                    pos: self.pos

            BoxLayout:
                id: input_box
                orientation: 'vertical'
                size_hint: .9, None
                pos_hint: {"center_x": .5, "center_y": .7}  
                height: self.minimum_height + dp(30)  # Adjust the height

                TextInput:
                    id: city_name
                    hint_text: "Enter Recipe Name"
                    size_hint: 1, None
                    height: self.minimum_height
                    multiline: False
                    font_size: "20sp"
                    hint_text_color: 0, 0, 0, 1
                    padding: 15
                    cursor_color: 1, 1, 1, 1
                    cursor_width: "2sp"
                    halign: "center"
                    background_color: 1, 1, 1, 1
                    canvas:
                        Color:
                            rgba: 1, 1, 1, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [15, 15, 0, 0]  # Set the radius for rounded corners

                Button:
                    text: "Get Recipe"
                    font_size: "20sp"
                    size_hint: 1, None
                    height: dp(48)
                    padding: 15
                    pos_hint: {"center_x": .5, "center_y": .5}  

                    background_color: 1, 1, 1, 0
                    color: rgba(148, 117, 255, 255)
                    on_release: app.search_recipe()
                    canvas.before:
                        Color:
                            rgb: 1, 1, 1, 1
                        RoundedRectangle:
                            size: self.size
                            pos: self.pos
                            radius: [0, 0, 15, 15]  # Set the radius for rounded corners
'''


class RecipeApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def search_recipe(self):
        # Your search_recipe logic here
        pass


if __name__ == "__main__":
    RecipeApp().run()
