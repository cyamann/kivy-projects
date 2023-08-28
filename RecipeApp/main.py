import requests
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import xml.etree.ElementTree as ET

Window.size = (350,600)
kv = '''
MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "assets/recipe.png"
        size_hint: .1, .1
        pos_hint: {"center_x": 0.18, "center_y": 0.95}
    MDLabel:
        id: header
        text: "Welcome to Recipe App"
        pos_hint: {"center_x": 0.55, "center_y": 0.95}
        halign: "center"
        font_size: "20sp"
    Image:
        id: recipe_image
        source: ""
        size_hint: .3, .3
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
    MDLabel:
        id: ingredients_label
        text: ""
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        halign: "left"
        font_size: "20sp"

    MDLabel:
        id: instructions_label
        text: ""
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        halign: "left"
        font_size: "20sp"
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
                orientation: 'vertical'
                size_hint: .9, None
                pos_hint: {"center_x": .5, "center_y": .7}  
                height: self.minimum_height + dp(30)  # Adjust the height

                TextInput:
                    id: recipe_name
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
        recipe_name = self.root.ids.recipe_name.text
        self.show_searched_recipe(recipe_name)

    def show_searched_recipe(self, recipe_name):
        # Logic to fetch and display searched recipe
        # Example: Replace this with your recipe fetching logic
        recipes = self.read_recipes_from_xml("recipes.xml")  # Update the XML filename
        searched_recipe = None

        for recipe in recipes:
            if recipe['name'].lower() == recipe_name.lower():
                searched_recipe = recipe
                break

        if searched_recipe:
            self.update_recipe_ui(searched_recipe)
        else:
            self.clear_recipe_ui()

    def read_recipes_from_xml(self, xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        recipes = []
        for recipe_element in root.findall('recipe'):
            name = recipe_element.get('name')
            ingredients = [ingredient.text for ingredient in recipe_element.find('ingredients')]
            instructions = [step.text for step in recipe_element.find('instructions')]
            image = recipe_element.find('image').text

            recipe = {
                'name': name,
                'ingredients': ingredients,
                'instructions': instructions,
                'image': image
            }
            recipes.append(recipe)

        return recipes

    def update_recipe_ui(self, recipe_data):
        self.root.ids.header.text = f"Recipe: {recipe_data['name']}"
        self.root.ids.recipe_image.source = recipe_data['image']

        ingredients_text = "\n".join(["- " + ingredient for ingredient in recipe_data['ingredients']])
        instructions_text = "\n".join(["- " + instruction for instruction in recipe_data['instructions']])

        self.root.ids.ingredients_label.text = ingredients_text
        self.root.ids.instructions_label.text = instructions_text

    def clear_recipe_ui(self):
        self.root.ids.header.text = "Recipe Not Found"
        self.root.ids.recipe_image.source = ""
        self.root.ids.ingredients_label.text = ""
        self.root.ids.instructions_label.text = ""

if __name__ == "__main__":
    RecipeApp().run()
