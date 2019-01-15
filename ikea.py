#import modules
import pygame
import time
import random

#initialize pygame
pygame.init()

#color variables
blue = (20,0,249)
black = (0,0,0)
white = (255,255,255)

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
emma_img = pygame.image.load("Sprites/Emma_v2.png")
mason_img = pygame.image.load("Sprites/Mason_v2.png")
'''dialogue boxes'''
narrator_box = pygame.image.load("Backgrounds/Narrator_Box.png")
you_talk = pygame.image.load("Backgrounds/You_Dialogue.png")
child_talk = pygame.image.load("Backgrounds/Child_Dialogue.png")
emma_talk = pygame.image.load("Backgrounds/Emma_Dialogue.png")
mason_talk = pygame.image.load("Backgrounds/Mason_Dialogue.png")
'''backgrounds'''
op_back = pygame.image.load("Backgrounds/Opening_Background.png")
storefront = pygame.image.load("Backgrounds/Ikea_Storefront.png")
entrance_back = pygame.image.load("Backgrounds/Entrance_Back.png")
living_back = pygame.image.load("Backgrounds/Living_Back.png")
dining_back = pygame.image.load("Backgrounds/Dining_Back.png")
bed_back = pygame.image.load("Backgrounds/Bedroom_Back.png")
bstorage_back = pygame.image.load("Backgrounds/bedroomstorage_back.png")
bath_back1 = pygame.image.load("Backgrounds/bathroom1_back.png")
bath_back2 = pygame.image.load("Backgrounds/bathroom2_back.png")
work_back = pygame.image.load("Backgrounds/workspace_back.png")
kitchen_back = pygame.image.load("Backgrounds/Kitchen_Back.png")
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
    message_display("You attack!", 60, 400)
    message_display(f"Opponent takes {damage} damage", 60, 425)
    message_display(f"Opponent health is now {opponent.health}", 60, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("You take no damage", 60, 400)
    pygame.display.update()
    time.sleep(2)

  def flee(self):
    '''50% chance of escaping a fight'''
    global count
    luck = [0,1]
    chance = random.choice(luck)
    if chance == 0:
      display.blit(narrator_box, (0,300))
      message_display("You trip and fail to flee", 60, 400)
      pygame.display.update()
      time.sleep(2)
    else:
      display.blit(narrator_box,(0,300))
      message_display("You knock down some furniture and successfully escape", 60, 400)
      pygame.display.update()
      time.sleep(2)
      count += 1
  
  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 60, 400)
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
    message_display("Opponent attacks!", 60, 400)
    message_display(f"You take {damage} damage", 60, 425)
    message_display(f"Your health is now {you.health}", 60, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 60, 400)
    pygame.display.update()
    time.sleep(2)

class Employee1(pygame.sprite.Sprite):
  def __init__(self, img, hp):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 5
    self.defense = 3
    self.health = hp

  def draw(self):
    '''blit the avatar on screen'''
    display.blit(self.image, (300,200))

  def attack(self):
    '''single attack the user'''
    damage = self.atk
    you.health -= damage
    display.blit(narrator_box,(0,300))
    message_display("Opponent attacks!", 60, 400)
    message_display(f"You take {damage} damage", 60, 425)
    message_display(f"Your health is now {you.health}", 60, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 60, 400)
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
    message_display("Opponent attacks!", 60, 400)
    message_display(f"You take {damage} damage", 60, 425)
    message_display(f"Your health is now {you.health}", 60, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 60, 400)
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
    message_display("Opponent attacks!", 60, 400)
    message_display(f"You take {damage} damage", 60, 425)
    message_display(f"Your health is now {you.health}", 60, 450)
    pygame.display.update()
    time.sleep(2)

  def defend(self):
    '''Take no damage for a turn'''
    display.blit(narrator_box, (0,300))
    message_display("Opponent defends", 60, 400)
    pygame.display.update()
    time.sleep(2)

#class assignments
you = User()
boy = Child(boy_img, 3)
girl = Child(girl_img, 3)
emma = Employee1(emma_img, 12)
mason = Employee1(mason_img, 12)

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
  message_display("You Win!", 60,400)
  pygame.display.update()
  time.sleep(2)

def no_health():
  display.fill(black)
  message_display("You Lose", 350, 250)
  message_display("Hit the Spacebar to play again", 350, 300)
  message_display("If Not, Hit the X in the corner to exit", 350, 320)
  pygame.display.update()
  count = 0

def scene1():
  '''opening introduction'''
  display.blit(op_back,(0,0))
  display.blit(narrator_box, (0,300))
  message_display("It was a bright and sunny day.", 60, 400)

def scene2():
  '''opening introduction'''
  display.blit(op_back, (0,0))
  display.blit(narrator_box, (0,300))
  message_display("A perfect day for furniture shopping.", 60, 400)

def scene3():
  '''Cue Ikea'''
  display.blit(storefront, (0,0))

def scene4():
  '''More Introduction'''
  display.blit(storefront, (0,0)) 
  display.blit(narrator_box, (0,300))
  message_display("Ikea: The best place for interior decorating", 60, 400)

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
  message_display("Wow, I sure hope I don't get lost in here", 60, 400)

def scene8():
  '''Scene 6 Continued'''
  display.blit(entrance_back, (0,0))
  you.draw()
  display.blit(you_talk,(0,300))
  message_display("It's not like I'm going to have to fight anyone...", 60, 400)

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
  message_display("Hmm, This couch is nice..", 60, 400)

def scene12():
  '''Still more narration'''
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Must..resist..impulsive buying...", 60, 400)

def scene13():
  '''Right before fight scene'''
  display.blit(living_back, (0,0))
  you.draw()
  boy.draw()
  display.blit(you_talk, (0,300))
  message_display("Hey Kid, I was looking at that", 60, 400)

def scene14():
  '''Again, right before fight'''
  display.blit(living_back, (0,0))
  you.draw()
  boy.draw()
  display.blit(child_talk, (0,300))
  message_display("Mine now. Fight me, you anime wannabe.", 60, 400)

def scene15():
  '''introduction to fighting'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box, (0,300))
  message_display("Welcome to your first fight", 60, 390)
  message_display("You must be quick!(Keep hitting the arrow keys)", 60, 420)
  message_display("Or the opponent will keep attacking!!!", 60, 450)

def scene16():
  '''intro continued'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box, (0,300))
  message_display("Hit the Up-Arrow Key to Attack.", 60, 375)
  message_display("Hit the Down-Arrow Key to Defend", 60, 420)
  message_display("Hit the Right-Arrow Key to Flee", 60, 465)
  message_display("Hit the space bar to continue")

def scene17():
  '''choice input'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box,(0,300))
  message_display("Make your choice:", 60, 400)

def scene19():
  '''After Fight'''
  global count
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Phew, that was easy", 60, 400)
  message_display("Sure hope I don't have to do that again", 60, 420)
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
  message_display("I definitely need another table", 60, 400)

def scene23():
  '''More narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  girl.draw()
  display.blit(child_talk, (0,300))
  message_display("What a loser! You're looking at tables.", 60, 400)

def scene24():
  '''yet more narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  girl.draw()
  display.blit(you_talk, (0,300))
  message_display("Are you kidding me??", 60, 400)
  message_display("Where are all these kids coming from???", 60, 400)

def scene25():
  '''second fight scene'''
  display.fill(black)
  you.draw()
  girl.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)

def scene27():
  '''After fight scene'''
  global count
  display.blit(dining_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("This time I really hope I don't have to do that again", 60, 400)
  count += 1

def scene28():
  '''next map'''
  display.fill(black)
  display.blit(bedroom, (0,0))

def scene29():
  '''bedrooms'''
  display.blit(bed_back, (0,0))

def scene30():
  '''gift from the developer'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Congratulations on winning your first two fights!", 60, 400)

def scene31():
  '''gift from the developer'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Since you did so well, here's a gift! :)", 60, 400)
  you.health = 60
  you.atk = 3

def scene32():
  '''gift from the developer! atk and health increase!'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display(f"Health is now {you.health}", 60, 390)
  message_display(f"Attack Power is now {you.atk}", 60, 420)

def scene33():
  '''good luck'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("To be able to go back home, you must fight", 60, 390)
  message_display("your way out", 60, 420)
  message_display("Good Luck, grasshopper", 60, 450)

def scene34():
  '''nap and replenish energy'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("For now, you nap on the super comfy bed", 60, 390)
  message_display("to replenish your energy", 60, 420)

def scene35():
  '''bedroom storage map'''
  display.fill(black)
  display.blit(bedroom_storage, (0,0))

def scene36():
  '''bedroom storage background'''
  display.blit(bstorage_back, (0,0))

def scene37():
  '''bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("owo what's this", 60, 400)

def scene38():
  '''more bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I could fit so many things in these...", 60, 400)

def scene39():
  '''yet more bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("My anime figurine collection...", 60, 390)
  message_display("My Fall Out Boy posters...", 60, 420)
  message_display("My CNCO merch...", 60, 450)

def scene40():
  '''even more yet more bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  emma.draw()
  display.blit(emma_talk, (0,300))
  message_display("You look like you would be a good employee here", 60, 400)

def scene41():
  '''still more even more yet more narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  emma.draw()
  display.blit(you_talk, (0,300))
  message_display("Um No, I don't think so", 60, 400)

def scene42():
  scene40()

def scene43():
  '''right before fight scene'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  emma.draw()
  display.blit(you_talk, (0,300))
  message_display("Why can't people leave me alone today??", 60, 400)

def scene44():
  '''third fight scene'''
  display.fill(black)
  you.draw()
  emma.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)

def scene46():
  '''after third fight'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Maybe it's time I dye my hair a normal color...", 60, 400)
  message_display("People will finally leave me alone.", 60, 430)

def scene47():
  '''bathroom map'''
  display.fill(black)
  display.blit(bathroom, (0,0))

def scene48():
  '''bathroom background'''
  display.blit(bath_back1, (0,0))

def scene49():
  '''bathroom narration'''
  display.blit(bath_back1, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("OMG This curtain is totes cute.", 60, 400)

def scene50():
  '''more bathroom narration'''
  display.blit(bath_back1, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Hmm but my bathroom walls are green..", 60, 400)
  message_display("It'd look like too much Christmas.", 60, 430)

def scene51():
  '''even more bathroom narration'''
  display.blit(bath_back1, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Maybe I need some professional help.",  60, 400)

def scene52():
  '''mason appears for even more narration'''
  display.blit(bath_back2, (0,0))
  you.draw()
  mason.draw()
  display.blit(mason_talk, (0,300))
  message_display("Did you say professional help? XD!", 60, 400)

def scene53():
  '''right before fight scene'''
  display.blit(bath_back2, (0,0))
  you.draw()
  mason.draw()
  display.blit(you_talk, (0,300))
  message_display("AAAAAAAAAAAAAAAAAAAAAA", 60, 390)
  message_display("It's time to stop!", 60, 420)

def scene54():
  '''fourth fight scene'''
  display.fill(black)
  you.draw()
  mason.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)

def scene56():
  '''after fourth fight'''
  display.blit(bath_back2, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I'm starting to think I'm being attacked", 60, 390)
  message_display("I'd better get out of here ASAP", 60, 420)

def scene57():
  '''workspace map'''
  display.fill(black)
  display.blit(workspaces, (0,0))

def scene58():
  '''workspace background'''
  display.blit(work_back, (0,0))

def scene59():
  '''developer's gift!'''
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Congratulations on getting halfway through!", 60, 400)

def scene60():
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Have this gift as a token!", 60, 400)
  you.health = 70
  you.atk = 7

def scene61():
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display(f"Health is now {you.health}", 60, 390)
  message_display(f"Attack Power is now {you.atk}", 60, 420)

def scene62():
  '''developer's gift!!'''
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Being in the workspaces fills you with productivity", 60, 400)

def scene63():
  '''kitchen map'''
  display.fill(black)
  display.blit(kitchen, (0,0))

def scene64():
  '''kitchen background'''
  display.blit(kitchen_back, (0,0))

def scene65():
  '''kitchen narration'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,0))
  message_display("If only I had a significant other that cooked...", 60, 400)

def scene66():
  '''more kitchen narration'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,0))
  message_display("I'd decorate my own kitchen better", 60, 400)

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
    message_display("Hit SPACE to continue", 60, 400)
    pygame.display.update()
    count += 1
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
    if you.health <= 0:
      no_health()
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
    if you.health <= 0:
      no_health()
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
  elif count == 34:
    scene34()
  elif count == 35:
    scene35()
  elif count == 36:
    scene36()
  elif count == 37:
    scene37()
  elif count == 38:
    scene38()
  elif count == 39:
    scene39()
  elif count == 40:
    scene40()
  elif count == 41:
    scene41()
  elif count == 42:
    scene42()
  elif count == 43:
    scene43()
  elif count == 44:
    scene44()
    pygame.display.update()
    time.sleep(2)
    count += 1
  elif count == 45:
    opponent_choice(emma)
    choice(key, emma)
    if emma.health == 0:
      win_fight()
      count += 1
    if you.health <= 0:
      no_health()
  elif count == 46:
    scene46()
  elif count == 47:
    scene47()
  elif count == 48:
    scene48()
  elif count == 49:
    scene49()
  elif count == 50:
    scene50()
  elif count == 51:
    scene51()
  elif count == 52:
    scene52()
  elif count == 53:
    scene53()
  elif count == 54:
    scene54()
    pygame.display.update()
    time.sleep(2)
    count += 1
  elif count == 55:
    opponent_choice(mason)
    choice(key, mason)
    if mason.health == 0:
      win_fight()
      count += 1
    if you.health <= 0:
      no_health()
  elif count == 56:
    scene56()
  elif count == 57:
    scene57()
  elif count == 58:
    scene58()
  elif count == 59:
    scene59()
  elif count == 60:
    scene60()
  elif count == 61:
    scene61()
  elif count == 62:
    scene62()
  elif count == 63:
    scene63()
  elif count == 64:
    scene64()
  elif count == 65:
    scene65()
  elif count == 66:
    scene66()

pygame.quit()
quit()