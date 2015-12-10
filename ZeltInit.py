class Character:
   """Class containing all character related variables."""
   def __init__(self):
       self.name=""
       self.initiative=0
       self.inert_initiative=False
       self.crash_state=False
       self.crash_counter=0
       self.shift_target=""
   def SetName(self):
       self.name=input("Name: ")

   def set_init(self):
       self.initiative=input("Join Battle Roll: ")


def clear_screen():
   """Prints a bunch of new lines to clear the screen."""
   for i in range(24):
       print("")

character_list = []
def add_new_character():
   """

   :rtype: object
   """
   new_character=Character()
   new_character.SetName()
   new_character.set_init()
   return new_character


print("Hello World")
clear_screen()
character_list.append(add_new_character())
print(character_list[0].name + " " +character_list[0].initiative)

