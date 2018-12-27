import time
import pygame

pygame.init()

display_width = 800
display_height = 500

blue = (20,0,249)

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ikea Adventure")
clock = pygame.time.Clock()
background_img = pygame.image.load("Opening_Background.png")
user_img = pygame.image.load("Main_Sprite_v2.png")
narrator_img = pygame.image.load("Narrator_Box.png")

def user_pic(x,y):
  display.blit(user_img, (x,y))

def text_objects(text,font):
  text_surface = font.render(text, True, blue)
  return text_surface, text_surface.get_rect()

def message_display(text):
  words = pygame.font.Font("courier.ttf", 35)
  text_surf, text_rectangle = text_objects(text, words)
  text_rectangle.center = ((display_height*0.5),(display_width*0.5))
  display.blit(text_surf, text_rectangle)

x = display_width * 0.3
y = display_height * 0.4


escaped = False

while not escaped:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      escaped = True

  display.blit(background_img, (0,0))
  display.blit(user_img, (x,y))
  display.blit(narrator_img, (0,(display_height-200)))
  message_display("Hello World")
  pygame.display.update()


#class Player:
 # def __init__(self, name):
  #  self.name = name
   # self.atk = 1
    #self.defense = 10
    #self.health = 50

#  def describe(self):
 #   '''print out the player's stats'''
  #  print(f"{self.name} has:")
   # print(f"-HP: {self.health}")
    #print(f"-Attack: {self.atk}")
   # print(f"-Defense: {self.defense}")
    #return

#  def attack(self, opponent):
 #   '''single attack obstacles'''
  #  print("You chose to attack!")
   # original_opponent_hp = opponent.hp
    #damage = self.atk - opponent.defense

#class Child:
 # def __init__(self):
  #  self.atk = 1
   # self.defense = 0
    #self.health = 3

#class Employee1:
 # def __init__(self, nombre):
  #  self.name = nombre
   # self.atk = 5
    #self.defense = 3
  #  self.health = 10

#class Employee2:
 # def __init__(self):
  #  self.atk = 10
   # self.defense = 7
    #self.health = 25

#class Employee3:
 # def __init__(self):
  #  self.atk = 17
   # self.defense = 15
    #self.health = 60

'''
inventory = {
  "map": 1
}

nombre = input("What is your name?: ")

user = Player(nombre)
print(f"Welcome {user.name}!")
print("\n")

print("It was a bright and sunny day in the land of ____")
time.sleep(2)
print("You decided to buy some miscellaneous furniture to decorate your new apartment")
time.sleep(2)
print("You arrive at Ikea, the most magical place ever")
time.sleep(3)
print("\n")

print("Maybe too magical...")
time.sleep(2)
print("You end up wandering around too much")
time.sleep(.5)
print("Several annoying ankle biters decide to bother you")
time.sleep(3)

child_1 = Child()
child_2 = Child()
child_3 = Child()
'''