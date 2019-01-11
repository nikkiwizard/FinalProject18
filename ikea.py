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

#scene count
count = 0

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
bed_back = pygame.image.load("Backgrounds/Bedroom_Back.png")
bstorage_back = pygame.image.load("Backgrounds/bedroomstorage_back.png")
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
    damage = self.atk
    opponent.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("You attack!", 70, 400)
    message_display(f"Opponent takes {damage} damage", 70, 425)
    message_display(f"Opponent health is now {opponent.health}", 70, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("You take no damage", 70, 400)
    pygame.display.update()
    time.sleep(2)

  def flee(self):
    '''50% chance of escaping a fight'''
    global count
    luck = [0,1]
    chance = random.choice(luck)
    if chance == 0:
      display.blit(narrator_box, (0,300))
      message_display("You trip and fail to flee", 70, 400)
      pygame.display.update()
      time.sleep(2)
    else:
      display.blit(narrator_box,(0,300))
      message_display("You knock down some furniture and successfully escape", 70, 400)
      pygame.display.update()
      time.sleep(2)
      count += 1
  
  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 70, 400)
    pygame.display.update()
    time.sleep(2)

class Child(pygame.sprite.Sprite):
  '''introduction to fighting an enemy: a child'''
  def __init__(self, image, hp):
    pygame.sprite.Sprite.__init__(self)
    self.image = image
    self.atk = 1
    self.defense = 0
    self.health = hp

  def draw(self):
    '''blit the avatar on screen'''
    display.blit(self.image, (350,200))

  def attack(self):
    '''single attack the user'''
    damage = self.atk
    you.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("Opponent attacks!", 70, 400)
    message_display(f"You take {damage} damage", 70, 425)
    message_display(f"Your health is now {you.health}", 70, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 70, 400)
    pygame.display.update()
    time.sleep(2)

class Employee1(pygame.sprite.Sprite):
  def __init__(self, img):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 5
    self.defense = 3
    self.health = 12

  def draw(self):
    '''blit the avatar on screen'''
    display.blit(self.image, (300,200))

  def attack(self):
    '''single attack the user'''
    damage = self.atk
    you.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("Opponent attacks!", 70, 400)
    message_display(f"You take {damage} damage", 70, 425)
    message_display(f"Your health is now {you.health}", 70, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 70, 400)
    pygame.display.update()
    time.sleep(2)

class Employee2(pygame.sprite.Sprite):
  def __init__(self, img):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 10
    self.defense = 7
    self.health = 25

  def draw(self):
    '''blit the avatar on screen'''
    display.blit(self.image, (250,200))

  def attack(self):
    '''single attack the user'''
    damage = self.atk
    you.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("Opponent attacks!", 70, 400)
    message_display(f"You take {damage} damage", 70, 425)
    message_display(f"Your health is now {you.health}", 70, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 70, 400)
    pygame.display.update()
    time.sleep(2)

class Employee3(pygame.sprite.Sprite):
  def __init__(self, img):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 17
    self.defense = 15
    self.health = 60

  def draw(self):
    '''blit the avatar on screen'''
    display.blit(self.image, (200,200))

  def attack(self):
    '''single attack the user'''
    damage = self.atk
    you.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("Opponent attacks!", 70, 400)
    message_display(f"You take {damage} damage", 70, 425)
    message_display(f"Your health is now {you.health}", 70, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 70, 400)
    pygame.display.update()
    time.sleep(2)

#class assignments
you = User()
boy = Child(boy_img, 3)
girl = Child(girl_img, 3)

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

def choice(k, opponent):
  if k[pygame.K_UP]:
    you.attack(opponent)
    return

  elif k[pygame.K_DOWN]:
    you.defend()
    return

  elif k[pygame.K_RIGHT]:
    you.flee()
    return

def opponent_choice(character):
  options = ["fight", "defend"]
  choice = random.choice(options)
  if choice == "fight":
    character.attack()
  elif choice == "defend":
    character.defend()

def win_fight():
  display.fill(black)
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("You Win!", 70,400)
  pygame.display.update()
  time.sleep(2)

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
  '''choice input'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box,(0,300))
  message_display("Make your choice:", 70, 400)

def scene19():
  '''After Fight'''
  global count
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Phew, that was easy", 70, 400)
  message_display("Sure hope I don't have to do that again", 70, 420)
  count += 1

def scene20():
  '''Next map'''
  display.fill(black)
  display.blit(dining, (0,0))

def scene21():
  '''Dining Room'''
  display.blit(dining_back, (0,0))

def scene22():
  '''Dining Room narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I definitely need another table", 70, 400)

def scene23():
  '''More narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  girl.draw()
  display.blit(child_talk, (0,300))
  message_display("What a loser! You're looking at tables.", 70, 400)

def scene24():
  '''yet more narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  girl.draw()
  display.blit(you_talk, (0,300))
  message_display("Are you kidding me??", 70, 400)
  message_display("Where are all these kids coming from???", 70, 400)

def scene25():
  '''second fight scene'''
  display.fill(black)
  you.draw()
  girl.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 70, 400)

def scene27():
  '''After fight scene'''
  global count
  display.blit(dining_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("This time I really hope I don't have to do that again", 70, 400)
  count += 1

def scene28():
  '''next map'''
  display.fill(black)
  display.blit(bedroom, (0,0))

def scene29():
  '''bedrooms'''
  display.blit(bed_back, (0,0))

def scene30():
  '''gift from the author'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Congratulations on winning your first two fights!", 70, 400)

def scene31():
  '''gift from the author'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Since you did so well, here's a gift! :)", 70, 400)
  you.health = 60
  you.atk = 3

def scene32():
  '''gift from the author! atk and health increase!'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display(f"Health is now {you.health}", 70, 390)
  message_display(f"Attack Power is now {you.atk}", 70, 420)

def scene33():
  '''good luck'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("To be able to go back home, you must fight", 70, 390)
  message_display("your way out", 70, 420)
  message_display("Good Luck, grasshopper", 70, 450)

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
    print(f"advanced one count {count}")
    count += 1
    pygame.display.update()
  
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
    pygame.display.update()
  elif count == 17:
    scene17()
    pygame.display.update()
    time.sleep(1)
    count += 1
  elif count == 18:
    opponent_choice(boy)
    choice(key, boy)
    if boy.health == 0:
      win_fight()
      count += 1
  elif count == 19:
    scene19()
    pygame.display.update()
  elif count == 20:
    scene20()
  elif count == 21:
    scene21()
  elif count == 22:
    scene22()
  elif count == 23:
    scene23()
  elif count == 24:
    scene24()
  elif count == 25:
    scene25()
    pygame.display.update()
    time.sleep(2)
    count += 1
  elif count == 26:
    opponent_choice(girl)
    choice(key, girl)
    if girl.health == 0:
      win_fight()
      count += 1
  elif count == 27:
    scene27()
    pygame.display.update()
  elif count == 28:
    scene28()
  elif count == 29:
    scene29()
  elif count == 30:
    scene30()
  elif count == 31:
    scene31()
  elif count == 32:
    scene32()
  elif count == 33:
    scene33()

pygame.quit()
quit()