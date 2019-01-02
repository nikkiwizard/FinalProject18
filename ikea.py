#import modules
import time
import pygame

#initialize pygame
pygame.init()

#color variables
blue = (20,0,249)

#window variables
display_width = 800
display_height = 500

#window display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ikea Adventure")

#clock and frames
clock = pygame.time.Clock()
clock.tick(30)

#image loading
'''avatars'''
user_img = pygame.image.load("Sprites/Main_Sprite_v2.png")
girl = pygame.image.load("Sprites/Girl_v2.png")
boy = pygame.image.load("Sprites/Boy_v2.png")
'''backgrounds and text boxes'''
op_background = pygame.image.load("Backgrounds/Opening_Background.png")
storefront = pygame.image.load("Backgrounds/Ikea_Storefront.png")
narrator_box = pygame.image.load("Backgrounds/Narrator_Box.png")
dialogue_box = pygame.image.load("Backgrounds/Dialogue_Box.png")
'''map pictures'''
entrance = pygame.image.load("Maps/Entrance.png")
living_room = pygame.image.load("Maps/Living_Room.png")
dining = pygame.image.load("Maps/Dining.png")
bedroom = pygame.image.load("Maps/Bedrooms.png")
bedroom_storage = pygame.image.load("Maps/Bedroom_Storage.png")
bathroom = pygame.image.load("Maps/Bathrooms.png")
workspaces = pygame.image.load("Maps/Workspaces.png")
kitchen = pygame.image.load("Maps/Kitchens.png")
childrens = pygame.image.load("Maps/Children_Section.png")
final_stage = pygame.image.load("Maps/Exit.png")

class User(pygame.sprite.Sprite):
  def __init__(self, name):
    pygame.sprite.Sprite.__init__(self)
    self.image = user_img
    self.name = name
    self.atk = 1
    self.defense = 10
    self.health = 50

  #def describe(self):
    #'''print out the player's stats'''
    #print(f"{self.name} has:")
    #print(f"-HP: {self.health}")
    #print(f"-Attack: {self.atk}")
    #print(f"-Defense: {self.defense}")
    #return

  def attack(self, opponent):
    '''single attack opponent'''
    damage = self.atk - (opponent.defense*0.5)
    opponent.health -= damage


class Child(pygame.sprite.Sprite):
  def __init__(self, image):
    pygame.sprite.Sprite.__init__(self)
    self.image = image
    self.atk = 1
    self.defense = 0
    self.health = 3



def text_messages(text,font):
  '''Render the text in color and return the rectangle'''
  text_surface = font.render(text, True, blue)
  return text_surface, text_surface.get_rect()

def message_display(text):
  '''Set up the text with font and rectangle center'''
  '''This one blits the actual text'''
  words = pygame.font.Font("courier.ttf", 22)
  text_surf, text_rectangle = text_messages(text, words)
  text_rectangle.center = (70,390)
  display.blit(text_surf, text_rectangle.center)

escaped = False

#game loop
while not escaped:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      escaped = True

  display.blit(op_background,(0,0))
  display.blit(narrator_box, (0,300))
  message_display("It was a bright and sunny day")
  pygame.display.update()

pygame.quit()
quit()



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

#print("You decided to buy some miscellaneous furniture to decorate your new apartment")
#time.sleep(2)
#print("You arrive at Ikea, the most magical place ever")
#time.sleep(3)
#print("\n")

#print("Maybe too magical...")
#time.sleep(2)
#print("You end up wandering around too much")
#time.sleep(.5)
#print("Several annoying ankle biters decide to bother you")
#time.sleep(3)
