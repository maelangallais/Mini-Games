#Créé le 15 Mai 2023
from kandinsky import fill_rect,get_pixel,draw_string
from ion import *
from time import sleep

co=[0,32,64,96,128,160,192]
interface,selection=(255,181,59),(48,246,49)
switch,restart,delay,boucle=1,True,0.1,True
rouge,jaune,blanc,noir,bleu=(255,0,0),(255,231,41),(255,255,255),(0,0,0),(0,0,255)
partie,egal,vijaune,virouge=1,0,0,0
t,dx,dy=3,253,130

def choix(a,b):
  global coup
  global switch
  coup+=1
  if switch==1:
    fill_rect(co[a],co[b],30,30,rouge)
    switch=2
  elif switch==2:
    fill_rect(co[a],co[b],30,30,jaune)
    switch=1

def rougegagne(xa,ya,xb,yb):
  global virouge,partie
  if xa!=xb and ya==yb:
    fill_rect(co[xa],co[ya]+12,126,6,bleu)
  elif xa==xb and ya!=yb:
    fill_rect(co[xa]+12,co[ya],6,126,bleu)
  elif xa<xb and ya<yb:
    for i in range(126):
      fill_rect(co[xa]-3+i,co[ya]+i,6,1,bleu)
  elif xa>xb and ya>yb:
    for i in range(126):
      fill_rect(co[6-xa]+27-i,co[ya]+i,6,1,bleu)
  sleep(2)
  fill_rect(0,93,222,40,noir)
  draw_string("Les rouges gagnent !",10,103,rouge)
  sleep(2)
  virouge+=1
  partie+=1

def jaunegagne(xa,ya,xb,yb):
  global vijaune,partie
  if xa!=xb and ya==yb:
    fill_rect(co[xa],co[ya]+12,126,6,bleu)
  elif xa==xb and ya!=yb:
    fill_rect(co[xa]+12,co[ya],6,126,bleu)
  elif xa<xb and ya<yb:
    for i in range(126):
      fill_rect(co[xa]-3+i,co[ya]+i,6,1,bleu)
  elif xa>xb and ya>yb:
    for i in range(126):
      fill_rect(co[6-xa]+27-i,co[ya]+i,6,1,bleu)
  sleep(2)
  fill_rect(0,93,222,40,noir)
  draw_string("Les jaunes gagnent !",10,103,jaune)
  sleep(2)
  vijaune+=1
  partie+=1

def egalite():
  global egal,partie
  fill_rect(61,98,100,30,noir)
  draw_string("Egalité !",66,103)
  sleep(2)
  egal+=1
  partie+=1

def abandon():
  global partie
  fill_rect(61,98,100,30,noir)
  draw_string("Abandon !",66,103)
  sleep(2)
  partie+=1

image=[[0,0,0,0,1,1,1,1,0,0,0,0],
       [0,0,1,1,1,3,3,1,1,1,0,0],
       [0,1,1,1,3,3,3,3,1,1,1,0],
       [0,1,1,1,3,3,3,3,1,1,1,0],
       [3,1,1,1,3,3,3,3,1,1,1,3],
       [3,3,1,1,1,3,3,1,1,1,3,3],
       [3,3,1,1,1,1,1,1,1,1,3,3],
       [3,1,1,6,6,6,6,6,6,1,1,3],
       [1,1,6,4,4,4,4,4,4,6,1,1],
       [0,0,4,4,2,4,4,2,4,4,0,0],
       [0,0,4,4,2,4,4,2,4,4,0,0],
       [0,0,4,4,4,4,4,4,4,4,0,0],
       [0,0,0,4,4,4,4,4,4,0,0,0],
       [0,0,6,5,5,6,6,5,5,6,0,0],
       [0,4,6,5,5,4,4,5,5,6,4,0],
       [0,6,5,5,5,4,4,5,5,5,6,0],
       [4,6,5,5,5,4,4,5,5,5,6,4],
       [4,6,5,5,5,4,4,5,5,5,6,4],
       [4,6,5,5,1,1,1,1,5,5,6,4],
       [4,6,5,5,1,1,1,1,5,5,6,4],
       [0,0,0,1,1,1,1,1,1,0,0,0],
       [0,0,0,1,1,0,0,1,1,0,0,0],
       [0,0,0,1,1,0,0,1,1,0,0,0],
       [0,0,0,7,7,0,0,7,7,0,0,0],
       [0,0,7,7,7,0,0,7,7,7,0,0]]

while restart:
  fill_rect(0,0,320,222,blanc)
  fill_rect(0,0,222,32,interface)
  fill_rect(222,0,98,222,interface)
  fill_rect(0,0,320,2,noir)
  fill_rect(8,7,2,18,blanc)
  fill_rect(128,7,2,18,blanc)
  fill_rect(228,40,2,18,blanc)
  fill_rect(228,65,2,18,blanc)
  fill_rect(228,90,2,18,blanc)
  for a in range(25):
    for b in range(12):
      if image[a][b]==1:
        fill_rect(dx+b*t,dy+a*t,t,t,(255,255,255))
      if image[a][b]==2:
        fill_rect(dx+b*t,dy+a*t,t,t,(0,0,0))
      if image[a][b]==3:
        fill_rect(dx+b*t,dy+a*t,t,t,(249,32,42))
      if image[a][b]==4:
        fill_rect(dx+b*t,dy+a*t,t,t,(253,201,142))
      if image[a][b]==5:
        fill_rect(dx+b*t,dy+a*t,t,t,(20,32,151))
      if image[a][b]==6:
        fill_rect(dx+b*t,dy+a*t,t,t,(241,106,40))
      if image[a][b]==7:
        fill_rect(dx+b*t,dy+a*t,t,t,(100,56,0))
  for i in range(6):
    fill_rect(co[i]+30,co[1],2,222,noir)
  for i in range(5):
    fill_rect(co[0],co[i+1]+30,222,2,noir)
  draw_string("Partie n°"+str(partie),10,7,(0,0,255))
  draw_string("Egalité: "+str(egal),130,7)
  draw_string("Victoire",230,40)
  draw_string("Rouge: "+str(virouge),230,65,rouge)
  draw_string("Jaune: "+str(vijaune),230,90,jaune)
  x,y=3,6
  xp,yp=x-1,y
  coup,boucle=0,True
  hauteur=[6,6,6,6,6,6,6]
  while boucle:
    sleep(delay)
    if keydown(KEY_BACK):
      restart=False
      break
    if keydown(KEY_LEFT):
      xp,yp=x,hauteur[x]
      if x<=0:x=6
      else:x-=1
      while not hauteur[x]>0:
        if x<=0:x=6
        else:x-=1
      fill_rect(co[xp],co[yp],30,30,blanc)
    elif keydown(KEY_RIGHT):
      xp,yp=x,hauteur[x]
      if x>=6:x=0
      else:x+=1
      while not hauteur[x]>0:
        if x>=6:x=0
        else:x+=1
      fill_rect(co[xp],co[yp],30,30,blanc)
    elif keydown(KEY_OK):
      choix(x,hauteur[x])
      hauteur[x]-=1
      if hauteur[x]==0:
        eg=0
        while not hauteur[x]>0:
          if x<=0:x=6
          else:x-=1
          if hauteur[x]==0:eg+=1
          if eg==7:
            egalite()
            boucle=False
            break
    elif keydown(KEY_BACKSPACE):
      abandon()
      boucle=False
    cox,coy=co[x],co[hauteur[x]]
    fill_rect(cox,coy,30,30,selection)
    for c in range(2):
      if c==0:col=rouge
      else:col=jaune
      for a in range(7):
        for b in range(4):
          if get_pixel(co[b],co[a])==col and get_pixel(co[b+1],co[a])==col and get_pixel(co[b+2],co[a])==col and get_pixel(co[b+3],co[a])==col:
            if c==0:rougegagne(b,a,b+4,a)
            else:jaunegagne(b,a,b+4,a)
            boucle=False
      for a in range(7):
        for b in range(4):
          if get_pixel(co[a],co[b])==col and get_pixel(co[a],co[b+1])==col and get_pixel(co[a],co[b+2])==col and get_pixel(co[a],co[b+3])==col:
            if c==0:rougegagne(a,b,a,b+4)
            else:jaunegagne(a,b,a,b+4)
            boucle=False
      for a in range(4):
        for b in range(4):
          if get_pixel(co[a],co[b])==col and get_pixel(co[a+1],co[b+1])==col and get_pixel(co[a+2],co[b+2])==col and get_pixel(co[a+3],co[b+3])==col:
            if c==0:rougegagne(a,b,a+4,b+4)
            else:jaunegagne(a,b,a+4,b+4)
            boucle=False
      for a in range(4):
        for b in range(4):
          if get_pixel(co[6-a],co[b])==col and get_pixel(co[6-(a+1)],co[b+1])==col and get_pixel(co[6-(a+2)],co[b+2])==col and get_pixel(co[6-(a+3)],co[b+3])==col:
            if c==0:rougegagne(a,b,a-4,b-4)
            else:jaunegagne(a,b,a-4,b-4)
            boucle=False
