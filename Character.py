# This will contain the actions, modifiers, and other need to knows for a character
# The class specifics wll be imported based on the selected class which will be stored in some other file
from Class_Mage import Mage


class Character:
    def __init__(self, char_class,hp):
        self.char_class = char_class
        self.char_loadout = self.set_char(char_class, hp)

    def set_char(self,char_class,hp):
        loadout = Mage(hp) # Default
        if char_class == "MAGE":
            loadout = Mage(hp)

        return loadout




