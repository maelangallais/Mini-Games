#Créé le 8 Mars 2023
from math import cos,sin
from kandinsky import set_pixel,fill_rect,draw_string
from random import randint
from time import sleep

def fill_ellipsis(centerI, centerJ, a, b, theta, R, color):
  a2 = a*a
  b2 = b*b
  for i in range(centerI-3*R,centerI+3*R):
    for j in range(centerJ-3*R,centerJ+3*R):
      deltaI = i-centerI
      deltaJ = j-centerJ
      x = cos(theta)*deltaI + sin(theta)*deltaJ
      y = sin(theta)*deltaI - cos(theta)*deltaJ
      if (x*x/a2+y*y/b2 <= R):
        set_pixel(i, j, color)
    #Exemple : 
      #fill_ellipsis(160,111,10,10,4,10,(255,0,0))

def drapeau():
  while True:
    fill_rect(0,0,107,222,(randint(0,255),randint(0,255),randint(0,255))),fill_rect(107,0,107,222,(randint(0,255),randint(0,255),randint(0,255))),fill_rect(214,0,107,222,(randint(0,255),randint(0,255),randint(0,255))),sleep(1)
    if keydown(KEY_BACK):break

def france():fill_rect(0,0,107,222,(0,34,144)),fill_rect(107,0,107,222,(255,255,255)),fill_rect(214,0,107,222,(230,40,55))
def belgique():fill_rect(0,0,107,222,(0,0,0)),fill_rect(107,0,107,222,(245,211,36)),fill_rect(214,0,107,222,(232,49,62))
def allemagne():fill_rect(0,0,320,74,(0,0,0)),fill_rect(0,74,320,74,(214,0,0)),fill_rect(0,148,320,74,(247,200,0))
def italie():fill_rect(0,0,107,222,(0,131,96)),fill_rect(107,0,107,222,(255,255,255)),fill_rect(214,0,107,222,(200,40,55))
def ukraine():fill_rect(0,0,320,111,(0,88,181)),fill_rect(0,111,320,111,(247,206,0))
def irlande():fill_rect(0,0,107,222,(0,148,88)),fill_rect(107,0,107,222,(255,255,255)),fill_rect(214,0,107,222,(233,122,1))
def suede():fill_rect(0,0,320,222,(0,103,162)),fill_rect(90,0,30,222,(246,198,0)),fill_rect(0,95,320,30,(246,198,0))
def grece():fill_rect(0,0,320,222,(13,91,170)),fill_rect(50,0,25,125,(247,247,247)),fill_rect(125,25,213,25,(247,247,247)),fill_rect(0,50,125,25,(247,247,247)),fill_rect(125,75,213,25,(247,247,247)),fill_rect(0,125,320,25,(247,247,247)),fill_rect(0,175,320,25,(247,247,247))
def russie():fill_rect(0,0,320,74,(247,247,247)),fill_rect(0,74,320,74,(0,55,161)),fill_rect(0,148,320,74,(206,42,29))
def norvege():fill_rect(0,0,320,222,(180,12,46)),fill_rect(90,0,60,222,(247,247,247)),fill_rect(0,84,320,56,(247,247,247)),fill_rect(105,0,30,222,(0,31,88)),fill_rect(0,98,320,28,(0,31,88))
def suisse():fill_rect(0,0,320,222,(206,42,29)),fill_rect(80,91,160,40,(247,247,247)),fill_rect(140,31,40,160,(247,247,247))
def coree():fill_rect(0,0,320,222,(255,255,255)),fill_ellipsis(160,111,10,10,4,12,(255,0,0))

def jeu():
  a=12
  t=int(input("Serie de combien de drapeaux ? "))
  print("Combien de secondes avant que la réponse")
  b=int(input("n'apparaisse ? "))
  for i in range(t):
    choix=randint(1,a)
    if choix==1:france(),sleep(b),draw_string("France",0,0)
    if choix==2:belgique(),sleep(b),draw_string("Belgique",0,0)
    if choix==3:allemagne(),sleep(b),draw_string("Allemagne",0,0)
    if choix==4:italie(),sleep(b),draw_string("Italie",0,0)
    if choix==5:irlande(),sleep(b),draw_string("Irlande",0,0)
    if choix==6:ukraine(),sleep(b),draw_string("Ukraine",0,0)
    if choix==7:suede(),sleep(b),draw_string("Suède",0,0)
    if choix==8:grece(),sleep(b),draw_string("Grèce",0,0)
    if choix==9:russie(),sleep(b),draw_string("Russie",0,0)
    if choix==10:norvege(),sleep(b),draw_string("Norvège",0,0)
    if choix==11:suisse(),sleep(b),draw_string("Suisse",0,0)
    if choix==12:coree(),sleep(b),draw_string("Corée",0,0)
    sleep(1),fill_rect(0,0,320,222,(150,150,150)),sleep(0.05)

def rapide():
  print("Combien de secondes avant que la réponse")
  n=float(input("n'apparaisse ? "))
  for z in range(12):
    if z==0:france(),sleep(n),draw_string("France",0,0)
    if z==1:belgique(),sleep(n),draw_string("Belgique",0,0)
    if z==2:allemagne(),sleep(n),draw_string("Allemagne",0,0)
    if z==3:italie(),sleep(n),draw_string("Italie",0,0)
    if z==4:irlande(),sleep(n),draw_string("Irlande",0,0)
    if z==5:ukraine(),sleep(n),draw_string("Ukraine",0,0)
    if z==6:suede(),sleep(n),draw_string("Suede",0,0)
    if z==7:grece(),sleep(n),draw_string("Grece",0,0)
    if z==8:russie(),sleep(n),draw_string("Russie",0,0)
    if z==9:norvege(),sleep(n),draw_string("Norvege",0,0)
    if z==10:suisse(),sleep(n),draw_string("Suisse",0,0)
    if z==11:coree(),sleep(n),draw_string("Corée",0,0)
    sleep(1),fill_rect(0,0,320,222,(150,150,150)),sleep(0.05)

def instructions():
  print(" "),print(" "),print("Il y a 2 jeux."),print("Soit le jeu où tous les drapeaux défileront"),print("les uns a la suite des autre."),print("Soit le mode aléatoire où les drapeaux"),print("pourront revenir plusieurs fois.")
  dilemne=int(input("Alors tu choisis le jeu 1 ou le jeu 2 ? "))
  if dilemne==1:rapide()
  if dilemne==2:jeu()


instructions()
