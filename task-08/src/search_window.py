from PySide6.QtWidgets import QWidget,QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap, QPalette
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog


import os
import requests

class DisplayCapturedDialog(QDialog):
    def __init__(self, captured_pokemon):
        super().__init__()
        self.setWindowTitle("Captured Pokemon")
        self.setFixedSize(600, 800)
        self.captured_pokemon = captured_pokemon
        self.current_index = 0

        self.name_label = QLabel(self)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name_label)

        button_layout = QHBoxLayout() 
        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.previous_pokemon)
        self.prev_button.setStyleSheet(   # for styling
            """
            QPushButton {
                background-color: black;
                color: white;
                border: 1px solid red;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: red;
                color: black;
            }
            """
        )
        button_layout.addWidget(self.prev_button)  # for adding previous button to button layout

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_pokemon)
        self.next_button.setStyleSheet(
            """
            QPushButton {
                background-color: black;
                color: white;
                border: 1px solid red;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: red;
                color: black;
            }
            """
        )
        button_layout.addWidget(self.next_button)  # for adding next button to button layout

        layout.addLayout(button_layout)  # for adding button layout to main layout

        self.name_label.setAlignment(Qt.AlignLeft)
        font = self.name_label.font()
        font.setPointSize(40)
        self.name_label.setFont(font)
        layout.addWidget(self.name_label)

        self.setLayout(layout)

        self.update_display()


    def update_display(self):
        if self.current_index < len(self.captured_pokemon):
            pokemon_name = self.captured_pokemon[self.current_index]
            pixmap = QPixmap(f"{pokemon_name.lower()}_official_artwork.png")
            new_width = 650  # adjusting size of pikachu in display window
            new_height = 650  # For adjusting size of pikachu inside the display window
            pixmap = pixmap.scaled(new_width, new_height, Qt.AspectRatioMode.KeepAspectRatio)
            
            self.label.setPixmap(pixmap)
            self.name_label.setText(pokemon_name.capitalize())
        else:
            self.label.clear()
            self.name_label.clear()


    def next_pokemon(self):
        self.current_index += 1
        if self.current_index >= len(self.captured_pokemon):
            self.current_index = 0
        self.update_display()

    def previous_pokemon(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.captured_pokemon) - 1
        self.update_display()

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setFixedSize(1250, 750)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(450, -50, 500, 500)  # Adjustments for displaying pokemon position


        background_label = QLabel(self)
        pixmap = QPixmap("/home/mrblack/Poke-Search/assets/landing.jpg")
        pixmap = pixmap.scaled(1250, 750)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, 1250, 750)
        background_label.lower()

        self.details_label = QLabel("", self)
        self.details_label.setGeometry(550, 350, 600, 400)
        self.details_label.setStyleSheet("font-weight: bold; color: white;font-size: 20px") #adjustments for position of stats

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)
        label1.setStyleSheet("font-weight: bold;font-size: 20px")

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 400, 160, 43)
        enter_button.clicked.connect(self.fetch_pokemon_data)
        enter_button.setStyleSheet(
        """
        QPushButton {
        background-color: black;
        color: white;
        border: 1px solid red;
        font-weight: bold;
        border-radius: 10px;
        }
        QPushButton:hover {
        background-color: red;
        color: black;
        }
        """
        )

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 450, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)
        capture_button.setStyleSheet(
        """
        QPushButton {
            background-color: black;
            color: white;
            border: 2px solid red;
            font-weight: bold;
            font-size: 16px;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: red;
            color: black;
        }
        """
        )

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 500, 160, 43)
        display_button.clicked.connect(self.display_captured_pokemon)
        display_button.setStyleSheet(
        """
        QPushButton {
            background-color: black;
            color: white;
            border: 2px solid red;
            font-weight: bold;
            font-size: 16px;
            border-radius: 10px;
        }
        QPushButton:hover {
            background-color: red;
            color: black;
        }
        """
        )

        self.captured_pokemon = []

    def fetch_pokemon_data(self):
        pokemon_name = self.textbox.text()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

        if response.status_code == 200:
            pokemon_data = response.json()

            name = pokemon_data['name']
            abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
            types = [type['type']['name'] for type in pokemon_data['types']]
            stats = [f"{stat['stat']['name']}: {stat['base_stat']}" for stat in pokemon_data['stats']]

            # for getting the official artwork URL
            official_artwork_url = pokemon_data['sprites']['other']['official-artwork']['front_default']

    
            official_artwork_response = requests.get(official_artwork_url)

            if official_artwork_response.status_code == 200:
                with open(f"{pokemon_name.lower()}_official_artwork.png", 'wb') as img_file:
                    img_file.write(official_artwork_response.content)

                # for modifying stats
                stats = [f"{stat['stat']['name']}: {stat['base_stat']}" for stat in pokemon_data['stats']]
                stats_details = '\n'.join(stats)  # Join stats with newlines

                details = f"Name: {name}\nAbilities: {', '.join(abilities)}\nTypes: {', '.join(types)}\nStats:\n{stats_details}"
                self.details_label.setText(details)

            
                pixmap = QPixmap(f"{pokemon_name.lower()}_official_artwork.png")
                self.image_label.setPixmap(pixmap)

                # Delete the image file after displaying
                os.remove(f"{pokemon_name.lower()}_official_artwork.png")
            else:
                QMessageBox.critical(self, "Error", "Failed to download official artwork!")

        else:
            QMessageBox.critical(self, "Error", "Pokemon not found!")

    def capture_pokemon(self):
        pokemon_name = self.textbox.text()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")

        if response.status_code == 200:
            pokemon_data = response.json()
            official_artwork_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
            official_artwork_response = requests.get(official_artwork_url)

            if official_artwork_response.status_code == 200:
                with open(f"{pokemon_name.lower()}_official_artwork.png", 'wb') as img_file:
                    img_file.write(official_artwork_response.content)

                self.captured_pokemon.append(pokemon_name)
                QMessageBox.information(self, "Capture", f"You've captured {pokemon_name}!")
            else:
                QMessageBox.critical(self, "Error", "Failed to download official artwork!")
        else:
            QMessageBox.critical(self, "Error", "Pokemon not found!")
    



    def display_captured_pokemon(self):
        if not self.captured_pokemon:
            QMessageBox.information(self, "No Captured Pokemon", "You haven't captured any Pokemon yet!")
        else:
            dialog = DisplayCapturedDialog(self.captured_pokemon)
            dialog.exec_()      
    
      

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())
