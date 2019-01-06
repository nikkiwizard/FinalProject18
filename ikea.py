#import modules
import pygame
import time
import random

#initialize pygame
pygame.init()

#color variables
blue = (20,0,249)
black = (0,0,0)

#window variables
display_width = 800
display_height = 500

#window display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ikea Adventure")

#clock
clock = pygame.time.Clock()

#image loading
'''avatars'''
user_img = pygame.image.load("Sprites/Main_Sprite_v2.png")
girl_img = pygame.image.load("Sprites/Girl_v2.png")
boy_img = pygame.image.load("Sprites/Boy_v2.png")
'''backgrounds and text boxes'''
narrator_box = pygame.image.load("Backgrounds/Narrator_Box.png")
you_talk = pygame.image.load("Backgrounds/You_Dialogue.png")
child_talk = pygame.image.load("Backgrounds/Child_Dialogue.png")
op_back = pygame.image.load("Backgrounds/Opening_Background.png")
storefront = pygame.image.load("Backgrounds/Ikea_Storefront.png")
entrance_back = pygame.image.load("Backgrounds/Entrance_Back.png")
living_back = pygame.image.load("Backgrounds/Living_Back.png")
dining_back = pygame.image.load("Backgrounds/Dining_Back.png")
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
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = user_img
    self.atk = 1
    self.defense = 15
    self.health = 50

  def draw(self):
    '''blit the avatar on the screen'''
    display.blit(self.image, (20,200))

  def attack(self, opponent):
    '''single attack opponent'''
    damage = self.atk - (opponent.defense*0.5)
    opponent.health -= damage
    if opponent.health <= 0:
      opponent.visible = False
      display.blit(narrator_box, (0,300))
      message_display("You Win!", 70,400)
    else:
      opponent.visible = True
      display.blit(narrator_box,(0,300))
      message_display("You attack!", 70, 400)
      message_display("Opponent takes {damage} damage", 70, 425)

  def defend(self,opponent):
    '''Take no damage for a turn'''
    self.health -= opponent.atk * 0
    display.blit(narrator_box, (0,300))
    message_display("You take no damage", 70, 400)

  def flee(self):
    luck = [0,1]
    chance = random.choice(luck)
    if chance == 0:
      display.blit(narrator_box, (0,300))
      message_display("You trip and fail to flee")
    else:
      display.blit(narrator_box,(0,300))
      message_display("You knock down some furniture and successfully escape")

class Child(pygame.sprite.Sprite):
  '''introduction to fighting an enemy: a child'''
  def __init__(self, image):
    pygame.sprite.Sprite.__init__(self)
    self.image = image
    self.atk = 1
    self.defense = 0
    self.health = 3
    self.visible = True

  def draw(self):
    if self.visible:
      display.blit(self.image, (350,200))

  def attack(self):
    '''single attack user'''
    damage = self.atk - (you.defense*0.5)
    you.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("Opponent attacks!", 70, 400)
    message_display("You take {damage} damage", 70, 425)

  def defend(self):
    '''Take no damage for a turn'''
    self.health -= opponent.atk * 0
    display.blit(narrator_box, (0,300))
    message_display("Opponent takes no damage", 70, 400)

class Employee1(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #self.image
    self.atk = 5
    self.defense = 3
    self.health = 10

class Employee2(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #self.image
    self.atk = 10
    self.defense = 7
    self.health = 25

class Employee3(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    #self.image
    self.atk = 17
    self.defense = 15
    self.health = 60

#other variables
count = 0
you = User()
boy = Child(boy_img)

def text_messages(text,font):
  '''Render the text in color and return the rectangle'''
  text_surface = font.render(text, True, blue)
  return text_surface, text_surface.get_rect()

def message_display(text, x, y):
  '''Set up the text with font and rectangle center'''
  '''This one blits the actual text'''
  words = pygame.font.Font("courier.ttf", 22)
  text_surf, text_rectangle = text_messages(text, words)
  text_rectangle.center = (x,y)
  display.blit(text_surf, text_rectangle.center)

def opponent_choice(character):
  options = ["fight", "defend"]
  choice = random.choice(options)
  if choice == "fight":
    character.attack(You)
    message_display("{character} attacks!")
  elif choice == "defend":
    character.defend()
    message_display("{character} takes no damage")

def scene1():
  '''opening introduction'''
  display.blit(op_back,(0,0))
  display.blit(narrator_box, (0,300))
  message_display("It was a bright and sunny day.", 70, 400)

def scene2():
  '''opening introduction'''
  display.blit(op_back, (0,0))
  display.blit(narrator_box, (0,300))
  message_display("A perfect day for furniture shopping.", 70, 400)

def scene3():
  '''Cue Ikea'''
  display.blit(storefront, (0,0))

def scene4():
  '''More Introduction'''
  display.blit(storefront, (0,0)) 
  display.blit(narrator_box, (0,300))
  message_display("Ikea: The best place for interior decorating", 70, 400)

def scene5():
  '''First Map'''
  display.fill(black)
  display.blit(entrance, (0,0))

def scene6():
  '''Introduction to Plot Scene'''
  display.blit(entrance_back, (0,0))

def scene7():
  '''Scene 6 continued'''
  display.blit(entrance_back, (0,0))
  you.draw()
  display.blit(you_talk,(0,300))
  message_display("Wow, I sure hope I don't get lost in here", 70, 400)

def scene8():
  '''Scene 6 Continued'''
  display.blit(entrance_back, (0,0))
  you.draw()
  display.blit(you_talk,(0,300))
  message_display("It's not like I'm going to have to fight anyone...", 70, 400)

def scene9():
  '''Living Room Map'''
  display.fill(black)
  display.blit(living_room,(0,0))

def scene10():
  '''First fight/plot point background'''
  display.blit(living_back, (0,0))

def scene11():
  '''More narration for fight'''
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Hmm, This couch is nice..", 70, 400)

def scene12():
  '''Still more narration'''
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Must..resist..impulsive buying...", 70, 400)

def scene13():
  '''Right before fight scene'''
  display.blit(living_back, (0,0))
  you.draw()
  boy.draw()
  display.blit(you_talk, (0,300))
  message_display("Hey Kid, I was looking at that", 70, 400)

def scene14():
  '''Again, right before fight'''
  display.blit(living_back, (0,0))
  you.draw()
  boy.draw()
  display.blit(child_talk, (0,300))
  message_display("Mine now. Fight me, you anime wannabe.", 70, 400)

def scene15():
  '''introduction to fighting'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box, (0,300))
  message_display("Welcome to your first fight", 70, 400)

def scene16():
  '''intro continued'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box, (0,300))
  message_display("Hit the Up-Arrow Key to Attack.", 70, 375)
  message_display("Hit the Down-Arrow Key to Defend", 70, 420)
  message_display("Hit the Right-Arrow Key to Flee", 70, 465)

def scene17():
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box,(0,300))
  message_display("Make your choice:", 70, 420)

#game loop escape
escaped = False

#game loop
while not escaped:
  clock.tick(5)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      escaped = True

  key = pygame.key.get_pressed()

  if key[pygame.K_SPACE]:
    count += 1
    pygame.display.update()

  def choice():
    if key[pygame.K_UP]:
      if count >= 17:
        you.attack(boy)
        return

    elif key[pygame.K_DOWN]:
      if count >= 17:
        you.defend(boy)
        return

    elif key[pygame.K_LEFT]:
      you.flee()
      return

  if count == 0:
    message_display("Hit SPACE to continue", 70, 400)
    pygame.display.update()
  elif count == 1:
    scene1()
  elif count == 2:
    scene2()
  elif count == 3:
    scene3()
  elif count == 4:
    scene4()
  elif count == 5:
    scene5()
  elif count == 6:
    scene6()
  elif count == 7:
    scene7()
  elif count == 8:
    scene8()
  elif count == 9:
    scene9()
  elif count == 10:
    scene10()
  elif count == 11:
    scene11()
  elif count == 12:
    scene12()
  elif count == 13:
    scene13()
  elif count == 14:
    scene14()
  elif count == 15:
    scene15()
  elif count == 16:
    scene16()
  elif count == 17:
    scene17()
    choice()
    opponent_choice(boy)

pygame.quit()
quit()