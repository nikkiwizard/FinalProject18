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
peter_img = pygame.image.load("Sprites/Peter_v2.png")
lilia_img = pygame.image.load("Sprites/Lilia_v2.png")
nikki_img = pygame.image.load("Sprites/Nikki_v2.png")
'''dialogue boxes'''
narrator_box = pygame.image.load("Dialogue_Boxes/Narrator_Box.png")
you_talk = pygame.image.load("Dialogue_Boxes/You_Dialogue.png")
child_talk = pygame.image.load("Dialogue_Boxes/Child_Dialogue.png")
emma_talk = pygame.image.load("Dialogue_Boxes/Emma_Dialogue.png")
mason_talk = pygame.image.load("Dialogue_Boxes/Mason_Dialogue.png")
peter_talk = pygame.image.load("Dialogue_Boxes/Peter_Dialogue.png")
lilia_talk = pygame.image.load("Dialogue_Boxes/Lilia_Dialogue.png")
nikki_talk = pygame.image.load("Dialogue_Boxes/Nikki_Dialogue.png")
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
childrens_back = pygame.image.load("Backgrounds/Childrens_Back.png")
exit_back = pygame.image.load("Backgrounds/Exit_Back.png")
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

class User(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = user_img
    self.atk = 1
    self.defense = 15
    self.health = 50

  def draw(self,x=20,y=200):
    '''blit the avatar on the screen'''
    display.blit(self.image, (x,y))

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
  def __init__(self, img, hp):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 10
    self.defense = 7
    self.health = hp

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
  def __init__(self, img, hp):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 17
    self.defense = 15
    self.health = hp

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

class Manager(pygame.sprite.Sprite):
  def __init__(self, img):
    pygame.sprite.Sprite.__init__(self)
    self.image = img
    self.atk = 20
    self.defense = 15
    self.health = 65

  def draw(self):
    '''blit the avatar on screen'''
    display.blit(self.image, (20,200))

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

  def heal(self):
    self.health += 5
    display.blit(narrator_box, (0,300))
    message_display("Nikki Heals!", 60, 400)
    message_display(f"Nikki's health is now {self.health}!", 60, 425)

#class assignments
you = User()
boy = Child(boy_img, 3)
girl = Child(girl_img, 3)
emma = Employee1(emma_img, 12)
mason = Employee1(mason_img, 12)
peter = Employee2(peter_img, 25)
lilia = Employee3(lilia_img, 30)
nikki = Manager(nikki_img)

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

def nikki_choice():
  options = ["fight", "defend","heal"]
  choice = random.choice(options)
  if choice == "fight":
    nikki.attack()
  elif choice == "defend":
    nikki.defend()
  elif choice == "heal":
    nikki.heal()

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
  message_display("Hit the X in the corner to exit", 125, 320)
  pygame.display.update()

def scene1():
  '''opening introduction'''
  display.blit(op_back,(0,0))
  display.blit(narrator_box, (0,300))
  message_display("It was a bright and sunny day.", 60, 400)
  message_display("(Hit SPACE to continue)", 60, 470)
  pygame.display.update()

def scene2():
  '''opening introduction'''
  display.blit(op_back, (0,0))
  display.blit(narrator_box, (0,300))
  message_display("A perfect day for furniture shopping.", 60, 400)
  message_display("(Hit SPACE to continue)", 60, 470)
  pygame.display.update()

def scene3():
  '''Cue Ikea'''
  display.blit(storefront, (0,0))
  message_display("(Hit SPACE to continue)", 60, 470)
  pygame.display.update()

def scene4():
  '''More Introduction'''
  display.blit(storefront, (0,0)) 
  display.blit(narrator_box, (0,300))
  message_display("Ikea: The best place for interior decorating", 60, 400)
  pygame.display.update()

def scene5():
  '''First Map'''
  display.fill(black)
  display.blit(entrance, (0,0))
  pygame.display.update()

def scene6():
  '''Introduction to Plot Scene'''
  display.blit(entrance_back, (0,0))
  pygame.display.update()

def scene7():
  '''Scene 6 continued'''
  display.blit(entrance_back, (0,0))
  you.draw()
  display.blit(you_talk,(0,300))
  message_display("Wow, I sure hope I don't get lost in here", 60, 400)
  pygame.display.update()

def scene8():
  '''Scene 6 Continued'''
  display.blit(entrance_back, (0,0))
  you.draw()
  display.blit(you_talk,(0,300))
  message_display("It's not like I'm going to have to fight anyone...", 60, 400)
  pygame.display.update()

def scene9():
  '''Living Room Map'''
  display.fill(black)
  display.blit(living_room,(0,0))
  pygame.display.update()

def scene10():
  '''First fight/plot point background'''
  display.blit(living_back, (0,0))
  pygame.display.update()

def scene11():
  '''More narration for fight'''
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Hmm, This couch is nice..", 60, 400)
  pygame.display.update()

def scene12():
  '''Still more narration'''
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Must..resist..impulsive buying...", 60, 400)
  pygame.display.update()

def scene13():
  '''Right before fight scene'''
  display.blit(living_back, (0,0))
  you.draw()
  boy.draw()
  display.blit(you_talk, (0,300))
  message_display("Hey Kid, I was looking at that", 60, 400)
  pygame.display.update()

def scene14():
  '''Again, right before fight'''
  display.blit(living_back, (0,0))
  you.draw()
  boy.draw()
  display.blit(child_talk, (0,300))
  message_display("Mine now. Fight me, you anime wannabe.", 60, 400)
  pygame.display.update()

def scene15():
  '''introduction to fighting'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box, (0,300))
  message_display("Welcome to your first fight", 60, 390)
  message_display("You must be quick!(Keep spamming the arrow keys)", 60, 420)
  message_display("Or the opponent will keep attacking!!!", 60, 450)
  pygame.display.update()

def scene16():
  '''intro continued'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box, (0,300))
  message_display("Hit the Up-Arrow Key to Attack.", 60, 370)
  message_display("Hit the Down-Arrow Key to Defend.", 60, 400)
  message_display("Hit the Right-Arrow Key to Flee.", 60, 430)
  message_display("(Hit the space bar to continue and start the fight)", 55, 460)
  pygame.display.update()

def scene17():
  '''choice input'''
  display.fill(black)
  you.draw()
  boy.draw()
  display.blit(narrator_box,(0,300))
  message_display("Make your choice:", 60, 400)
  pygame.display.update()

def scene19():
  '''After Fight'''
  display.blit(living_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Phew, that was easy", 60, 400)
  message_display("Sure hope I don't have to do that again", 60, 420)
  pygame.display.update()

def scene20():
  '''Next map'''
  display.fill(black)
  display.blit(dining, (0,0))
  pygame.display.update()

def scene21():
  '''Dining Room'''
  display.blit(dining_back, (0,0))
  pygame.display.update()

def scene22():
  '''Dining Room narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I definitely need another table", 60, 400)
  pygame.display.update()

def scene23():
  '''More narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  girl.draw()
  display.blit(child_talk, (0,300))
  message_display("What a loser! You're looking at tables.", 60, 400)
  pygame.display.update()

def scene24():
  '''yet more narration'''
  display.blit(dining_back, (0,0))
  you.draw()
  girl.draw()
  display.blit(you_talk, (0,300))
  message_display("Are you kidding me??", 60, 400)
  message_display("Where are all these kids coming from???", 60, 425)
  pygame.display.update()

def scene25():
  '''second fight scene'''
  display.fill(black)
  you.draw()
  girl.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)
  pygame.display.update()

def scene27():
  '''After fight scene'''
  display.blit(dining_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("This time I really hope I don't have to do that again", 60, 400)
  pygame.display.update()

def scene28():
  '''next map'''
  display.fill(black)
  display.blit(bedroom, (0,0))
  pygame.display.update()

def scene29():
  '''bedrooms'''
  display.blit(bed_back, (0,0))
  pygame.display.update()

def scene30():
  '''gift from the developer'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Congratulations on winning your first two fights!", 60, 400)
  pygame.display.update()

def scene31():
  '''gift from the developer'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Since you did so well, here's a gift! :)", 60, 400)
  pygame.display.update()
  you.health = 60
  you.atk = 3

def scene32():
  '''gift from the developer! atk and health increase!'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display(f"Health is now {you.health}", 60, 390)
  message_display(f"Attack Power is now {you.atk}", 60, 420)
  pygame.display.update()

def scene33():
  '''good luck'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("To be able to go back home, you must fight", 60, 390)
  message_display("your way out", 60, 420)
  message_display("Good Luck, grasshopper", 60, 450)
  pygame.display.update()

def scene34():
  '''nap and replenish energy'''
  display.blit(bed_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("For now, you nap on the super comfy bed", 60, 390)
  message_display("to replenish your energy", 60, 420)
  pygame.display.update()

def scene35():
  '''bedroom storage map'''
  display.fill(black)
  display.blit(bedroom_storage, (0,0))
  pygame.display.update()

def scene36():
  '''bedroom storage background'''
  display.blit(bstorage_back, (0,0))
  pygame.display.update()

def scene37():
  '''bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("owo what's this", 60, 400)
  pygame.display.update()

def scene38():
  '''more bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I could fit so many things in these...", 60, 400)
  pygame.display.update()

def scene39():
  '''yet more bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("My anime figurine collection...", 60, 390)
  message_display("My Fall Out Boy posters...", 60, 420)
  message_display("My Doctor Who merch...", 60, 450)
  pygame.display.update()

def scene40():
  '''even more yet more bstorage narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  emma.draw()
  display.blit(emma_talk, (0,300))
  message_display("You look like you would be a good employee here", 60, 400)
  pygame.display.update()

def scene41():
  '''still more even more yet more narration'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  emma.draw()
  display.blit(you_talk, (0,300))
  message_display("Um No, I don't think so", 60, 400)
  pygame.display.update()

def scene42():
  scene40()
  pygame.display.update()

def scene43():
  '''right before fight scene'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  emma.draw()
  display.blit(you_talk, (0,300))
  message_display("Why can't people leave me alone today??", 60, 400)
  pygame.display.update()

def scene44():
  '''third fight scene'''
  display.fill(black)
  you.draw()
  emma.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)
  pygame.display.update()

def scene46():
  '''after third fight'''
  display.blit(bstorage_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Maybe it's time I dye my hair a normal color...", 60, 400)
  message_display("People will finally leave me alone.", 60, 430)
  pygame.display.update()

def scene47():
  '''bathroom map'''
  display.fill(black)
  display.blit(bathroom, (0,0))
  pygame.display.update()

def scene48():
  '''bathroom background'''
  display.blit(bath_back1, (0,0))
  pygame.display.update()

def scene49():
  '''bathroom narration'''
  display.blit(bath_back1, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("OMG This curtain is totes cute.", 60, 400)
  pygame.display.update()

def scene50():
  '''more bathroom narration'''
  display.blit(bath_back1, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Hmm but my bathroom walls are green..", 60, 400)
  message_display("It'd look like too much Christmas.", 60, 430)
  pygame.display.update()

def scene51():
  '''even more bathroom narration'''
  display.blit(bath_back1, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Maybe I need some professional help.",  60, 400)
  pygame.display.update()

def scene52():
  '''mason appears for even more narration'''
  display.blit(bath_back2, (0,0))
  you.draw()
  mason.draw()
  display.blit(mason_talk, (0,300))
  message_display("Did you say professional help? XD!", 60, 400)
  pygame.display.update()

def scene53():
  '''right before fight scene'''
  display.blit(bath_back2, (0,0))
  you.draw()
  mason.draw()
  display.blit(you_talk, (0,300))
  message_display("AAAAAAAAAAAAAAAAAAAAAA", 60, 400)
  message_display("It's time to stop!", 60, 425)
  pygame.display.update()

def scene54():
  '''fourth fight scene'''
  display.fill(black)
  you.draw()
  mason.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)
  pygame.display.update()

def scene56():
  '''after fourth fight'''
  display.blit(bath_back2, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I'm starting to think I'm being attacked", 60, 390)
  message_display("I'd better get out of here ASAP", 60, 420)
  pygame.display.update()

def scene57():
  '''workspace map'''
  display.fill(black)
  display.blit(workspaces, (0,0))
  pygame.display.update()

def scene58():
  '''workspace background'''
  display.blit(work_back, (0,0))
  pygame.display.update()

def scene59():
  '''developer's gift!'''
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Congratulations on getting halfway through!", 60, 400)
  pygame.display.update()

def scene60():
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Have this gift as a token!", 60, 400)
  pygame.display.update()
  you.health = 70
  you.atk = 7

def scene61():
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display(f"Health is now {you.health}", 60, 390)
  message_display(f"Attack Power is now {you.atk}", 60, 420)
  pygame.display.update()

def scene62():
  '''developer's gift!!'''
  display.blit(work_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Being in the workspaces fills you with productivity", 60, 400)
  pygame.display.update()

def scene63():
  '''kitchen map'''
  display.fill(black)
  display.blit(kitchen, (0,0))
  pygame.display.update()

def scene64():
  '''kitchen background'''
  display.blit(kitchen_back, (0,0))
  pygame.display.update()

def scene65():
  '''kitchen narration'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("If only I had a significant other that cooked...", 60, 400)
  pygame.display.update()

def scene66():
  '''more kitchen narration'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I'd decorate my own kitchen better", 60, 400)
  pygame.display.update()

def scene67():
  '''even more narration'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  peter.draw()
  display.blit(peter_talk, (0,300))
  message_display("Oh, I'll help you decorate! ;)", 60, 400)
  pygame.display.update()

def scene68():
  '''yet some more narration'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  peter.draw()
  display.blit(you_talk, (0,300))
  message_display("No thank you! Gotta blast!", 60, 400)
  pygame.display.update()

def scene69():
  '''right before fight scene 5'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  peter.draw()
  display.blit(peter_talk, (0,300))
  message_display("Awww, but I promise you'll have a good time *pouts*", 60, 400)
  pygame.display.update()

def scene70():
  '''fifth fight scene commence!!!'''
  display.fill(black)
  you.draw()
  peter.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)
  pygame.display.update()

def scene72():
  '''after fifth fight scene'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Where's an exit when you need one?!", 60, 400)
  pygame.display.update()

def scene73():
  '''after fifth fight scene part deux'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("*I'm in danger*", 60, 400)
  message_display("I've never seen my life flash before my eyes like today", 60, 425)
  pygame.display.update()

def scene74():
  '''after fifth fight scene part tre'''
  display.blit(kitchen_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Except maybe that one time before a history test XD", 60, 400)
  pygame.display.update()

def scene75():
  '''children's ikea map'''
  display.fill(black)
  display.blit(childrens, (0,0))
  pygame.display.update()

def scene76():
  '''children's section background'''
  display.blit(childrens_back, (0,0))
  pygame.display.update()

def scene77():
  ''''children section narration'''
  display.blit(childrens_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I wish I was still a kid...", 60, 400)
  pygame.display.update()
  you.atk = 8 

def scene78():
  ''''more narration'''
  display.blit(childrens_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("Imagine having a bunk bed that looks like a house", 60, 400)
  pygame.display.update()

def scene79():
  '''more narration'''
  display.blit(childrens_back, (0,0))
  you.draw()
  lilia.draw()
  display.blit(lilia_talk, (0,300))
  message_display("If you stay here forever, you can have one!", 60, 400)
  pygame.display.update()

def scene80():
  '''more narration'''
  display.blit(childrens_back, (0,0))
  you.draw()
  lilia.draw()
  display.blit(lilia_talk, (0,300))
  message_display("Please stay. Stay with us. Forever", 60, 400)
  pygame.display.update()

def scene81():
  '''more narration'''
  display.blit(childrens_back, (0,0))
  you.draw()
  lilia.draw()
  display.blit(you_talk, (0,300))
  message_display("Yikes, clingy much?", 60, 400)
  pygame.display.update()

def scene81():
  '''right before sixth fight scene'''
  display.blit(childrens_back,(0,0))
  you.draw()
  lilia.draw()
  display.blit(you_talk, (0,300))
  message_display("That's a no from me, fam", 60, 400)
  pygame.display.update()

def scene82():
  '''fight numero seis'''
  display.fill(black)
  you.draw()
  lilia.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)
  pygame.display.update()
  time.sleep(2)

def scene84():
  '''yay exit signs !!'''
  display.blit(exit_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("FINALLY!", 60, 400)
  pygame.display.update()

def scene85():
  display.blit(exit_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I can finally leave!!", 60, 400)
  pygame.display.update()

def scene86():
  display.blit(exit_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("F R E E D O M", 60, 400)
  pygame.display.update()

def scene87():
  display.blit(exit_back, (0,0))
  you.draw(40,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  message_display("(Don't hit SPACE until...)", 60, 425)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(80,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(100,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(150,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit",60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(200,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)

def scene88():
  display.blit(exit_back, (0,0))
  you.draw(200,200)
  display.blit(nikki_talk, (0,300))
  message_display("HOLD IT",60, 400)
  pygame.display.update()
  you.atk = 10

def scene89():
  display.blit(exit_back, (0,0))
  you.draw(200,200)
  display.blit(nikki_talk, (0,300))
  message_display("Where do you think you're going?!", 60, 400)
  pygame.display.update()

def scene90():
  display.blit(exit_back, (0,0))
  you.draw(200,200)
  nikki.draw()
  display.blit(nikki_talk, (0,300))
  message_display("Nobody is ever allowed to leave", 60, 400)
  pygame.display.update()

def scene91():
  display.blit(exit_back, (0,0))
  you.draw(200,200)
  nikki.draw()
  display.blit(you_talk, (0,300))
  message_display("We'll see about that", 60, 400)
  pygame.display.update()

def scene92():
  '''final boss fight: the developer~'''
  display.fill(black)
  you.draw(200,200)
  nikki.draw()
  display.blit(narrator_box, (0,300))
  message_display("Make your choice: ", 60, 400)
  pygame.display.update()
  time.sleep(2)

def scene94():
  display.blit(exit_back, (0,0))
  you.draw(200,200)
  display.blit(you_talk(0,300))
  message_display("I can finally leave", 60, 400)
  pygame.display.update()

def scene95():
  display.blit(exit_back, (0,0))
  you.draw(250,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(300,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(350,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(400,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(450,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(500,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(550,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(600,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(650,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(700,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(750,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(770,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(790,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)
  display.blit(exit_back, (0,0))
  you.draw(800,200)
  display.blit(narrator_box, (0,300))
  message_display("You make your way towards to exit", 60, 400)
  pygame.display.update()
  time.sleep(1)

def scene96():
  display.blit(op_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("The sunlight on my face and the refreshing wind...", 60, 400)
  pygame.display.update()


def scene97():
  display.blit(op_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("I thought I would never see the light again", 60, 400)
  pygame.display.update

def scene98():
  display.blit(op_back, (0,0))
  you.draw()
  display.blit(you_talk, (0,300))
  message_display("10/10, would do again", 60, 400)
  pygame.display.update()

def scene99():
  display.blit(op_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Congrats on winnning the game!",60, 400)
  pygame.display.update()

def scene100():
  display.blit(op_back, (0,0))
  you.draw()
  display.blit(narrator_box, (0,300))
  message_display("Thanks for playing!", 60, 400)
  pygame.display.update()

#game loop escape
escaped = False

#game loop
while not escaped:
  clock.tick(4)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      escaped = True

  key = pygame.key.get_pressed()

  if key[pygame.K_SPACE]:
    print(f"advanced one count {count}")
    count += 1

  if count == 0:
    message_display("Hit SPACE to continue", 60, 400)
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
    time.sleep(2)
    count += 1
  elif count == 18:
    opponent_choice(boy)
    choice(key, boy)
    if boy.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
  elif count == 19:
    scene19()
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
    time.sleep(2)
    count += 1
  elif count == 26:
    opponent_choice(girl)
    choice(key, girl)
    if girl.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
  elif count == 27:
    scene27()
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
    time.sleep(2)
    count += 1
  elif count == 45:
    opponent_choice(emma)
    choice(key, emma)
    if emma.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
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
    time.sleep(2)
    count += 1
  elif count == 55:
    opponent_choice(mason)
    choice(key, mason)
    if mason.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
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
  elif count == 67:
    scene67()
  elif count == 68:
    scene68()
  elif count == 69:
    scene69()
  elif count == 70:
    scene70()
    time.sleep(2)
    count += 1
  elif count == 71:
    opponent_choice(peter)
    choice(key, peter)
    if peter.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
  elif count == 72:
    scene72()
  elif count == 73:
    scene73()
  elif count == 74:
    scene74()
  elif count == 75:
    scene75()
  elif count == 76:
    scene76()
  elif count == 77:
    scene77()
  elif count == 78:
    scene78()
  elif count == 79:
    scene79()
  elif count == 80:
    scene80()
  elif count == 81:
    scene81()
  elif count == 82:
    scene82()
    count += 1
  elif count == 83:
    opponent_choice(lilia)
    choice(key, lilia)
    if lilia.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
  elif count == 84:
    scene84()
  elif count == 85:
    scene85()
  elif count == 86:
    scene86()
  elif count == 87:
    scene87()
    count  += 1
  elif count == 88:
    scene88()
  elif count == 89:
    scene89()
  elif count == 90:
    scene90()
  elif count == 91:
    scene91()
  elif count == 92:
    scene92()
    count += 1
  elif count == 93:
    nikki_choice()
    choice(key, nikki)
    if nikki.health <= 0:
      win_fight()
      count += 1
    if you.health <= 0:
      count = 500
  elif count == 94:
    scene94()
  elif count == 95:
    scene95()
  elif count == 96:
    scene96()
  elif count == 97:
    scene97()
  elif count == 98:
    scene98()
  elif count == 99:
    scene99()
  elif count == 100:
    scene100()
    time.sleep(15)
    escaped = True
  elif count == 500:
    no_health()

pygame.quit()
quit()