from gamelib import *
game = Game(612,459,"game2")
#Graphics
Lbosswalk = Animation("Lbosswalk.png",6,game,894/6,115)
Rbosswalk = Animation("Rbosswalk.png",6,game,894/6,115)
horse = Animation("horse.png",19,game,1904/19,51)
horse.moveTo(0,345)
horse.resizeBy(50)
downboss = Image("downboss.png",game)
bk = Image("desert.jpg",game)
bk2 = Image("desert2.jpg",game)
bk3 = Image("outcome.png",game)
htp = Image("htp.png",game)
wasted = Image("wasted.jpg",game)
instructions = Image("instructions.png",game)
left = Animation("left.png",12,game,1143/12,157)
right = Animation("right.png",12,game,1143/12,167)
intro = Image("intro.png",game)
text = Image("text.png",game)
texter = Image("texter.png",game)
play = Image("play.png",game)
Lbull = Image("Lbullet.png",game)
Lbull.visible = False
Rbull = Image("Rbullet.png",game)
Rbull.visible = False

gun = Sound("gun.wav",1)
game.setMusic("song.wav")
death = Sound("death.wav",2)
applause = Sound("applause.wav",3)
ufosound = Sound("aliensound.wav",4)
zombiesound = Sound("zombiesound.wav",5)

F = Font(black,30,white,"Cooper Black")
F2 = Font(black,20,red,"Bookman Old Style")
F3 = Font(white,20,red,"Cooper Black")
F4 = Font(red,20,black,"Franklin Gothic Heavy")
F5 = Font(green,25,black,"Titillium Web")

heart = Image("heart1.png",game)
heart2 = Image("heart2.png",game)
heart3 = Image("heart3.png",game)
heart4 = Image("heart4.png",game)
ufo = []
for index in range(40):
 ufo.append(Image("ufo.png",game))
 x = randint(50,600)
 y = randint (-800,-100)
 ufo[index].moveTo(x,y)
 ufo[index].setSpeed(2,180)
 ufo[index].resizeBy(30)
#Walkers from the Left
Lwalker = []
for index in range(30):
    Lwalker.append(Animation("Lwalker.png",6,game,928/6,102))
    x = randint (-1200,-200)
    s = randint(2,4)
    Lwalker[index].moveTo(x,350)
    Lwalker[index].setSpeed(s,270)
    Lwalker[index].resizeBy(-25)
#Walkers from the Right
Rwalker = []
for index in range(30):
    Rwalker.append(Animation("Rwalker.png",6,game,928/6,102))
    x = randint (800,1800)
    s = randint(2,4)
    Rwalker[index].moveTo(x,350)
    Rwalker[index].setSpeed(s,90)
    Rwalker[index].resizeBy(-25)
horse.setSpeed(5,270)
downboss.setSpeed(12,180)
downboss.moveTo(300,-2500)
Lbosswalk.setSpeed(3,270)
Rbosswalk.setSpeed(3,90)
Rbosswalk.moveTo(650,340)
Lbosswalk.moveTo(-1000,340)
Lbosswalk.resizeBy(-25)
Rbosswalk.resizeBy(-25)
heart.resizeBy(-95)
heart.moveTo(50,50)
heart2.resizeBy(-95)
heart2.moveTo(75,50)
heart3.resizeBy(-95)
heart3.moveTo(100,50)
heart4.resizeBy(-95)
heart4.moveTo(125,50)
right.health == left.health
right.health = 4
intro.resizeTo(612,459)
text.moveTo(300,150)
texter.moveTo(300,100)
texter.resizeBy(-55)
play.moveTo(300,250)
htp.moveTo(300,400)
htp.resizeBy(-20)
play.resizeBy(-20)
instructions.resizeBy(-35)
left.visible= False
right.visible= True
left.resizeBy(-30)
right.resizeBy(-30)
left.moveTo(-40,340)
right.moveTo(-40,340)
Lbull.resizeBy(-98)
Rbull.resizeBy(-98)
game.setBackground(bk)
bk2.resizeTo(612,459)
bk3.resizeTo(612,459)
xy =0
#Start Screen
startgame = True
while startgame:
    while not game.over:
     game.processInput()
     game.clearBackground()
     game.playMusic()
     intro.draw()
     htp.draw()
     text.draw()
     play.draw()
     if play.collidedWith(mouse) and mouse.LeftButton:
         game.over = True
     if htp.collidedWith(mouse):
        instructions.draw()
     game.update(30)
    game.over = False

    #Introduction
    if xy ==0:
     game.drawBackground()
    loop = 0
    #Introduction 2 Skipping
    while not game.over and xy==0:
        game.clearBackground()
        game.drawBackground()
        texter.draw()
        right.draw()
        right.x+=2
        game.drawText("Press ENTER to Start",right.x-30,right.y-100,F)
        if game.over == False:
            loop +=1
        if loop >50:
         game.wait(K_RETURN)
         game.over = True
        game.update(30)
    game.over = False

    #Wave 1 UFOS
    ufosgone = 0
    walkers = 0
    m = 40
    left.stop()
    right.stop()
    right.visible = True
    #m = ufos leftover before game is over
    while not game.over and right.health >0:
        game.processInput()
        game.scrollBackground("left",4)
        left.x = right.x
        left.y = right.y
        heart.draw()
        heart2.draw()
        heart3.draw()
        heart4.draw()
        left.draw()
        right.draw()
        #Health
        if right.health==3 or left.health ==3:
            heart4.visible = False
        if right.health ==2 or left.health ==2:
            heart3.visible = False
        if right.health ==1 or left.health ==1:
            heart2.visible = False
        if right.health ==0 or left.health ==0:
            heart.visible = False
        #UFOS
        for index in range(40):
            ufo[index].move()
            if ufo[index].visible == True and ufo[index].y>380:
             ufosgone +=1
             walkers +=1
             m -=1
             ufo[index].visible = False
            if ufo[index].collidedWith(left) or ufo[index].collidedWith(right):
                ufosound.play()
                left.health -=1
                right.health -= 1
                ufosgone+=1
                m -=1
                ufo[index].visible = False
        if ufosgone >39:
            game.over = True
        game.drawText("Health= " + str(right.health),35,70,F2)
        game.drawText("Level 1",500,70,F2)
        #Double Jump Prevention
        if left.y <340 or right.y<340:
            left.y +=5
            right.y +=5
        if right.y <280 and keys.Pressed[K_UP]:
            right.y +=20
            left.y +=20
        #Player Controls
        if keys.Pressed[K_UP]:
            right.y -=20
            left.y -=20
        if keys.Pressed[K_RIGHT]:
            right.visible = True
            left.visible = False
            right.nextFrame()
            right.x += 6
        if keys.Pressed[K_LEFT] :
            left.visible = True
            right.visible = False
            left.nextFrame()
            right.x -= 6
        #Prevent player from hiding in the edges
        if left.x <10 or right.x <10:
            left.x += 6
            right.x +=6
        if left.x >600 or right.x >600:
            left.x -=6
            right.x -=6
        game.update(30)
        
    game.over = False
    wave2done = 0
    game.clearBackground()
    left.stop()
    right.stop()
    #Wave 2 Walking Aliens
    while not game.over and right.health >0:
        game.processInput()
        bk2.draw()
        left.x = right.x
        left.y = right.y
        #Health
        if right.health==3 or left.health ==3:
            heart4.visible = False
        if right.health ==2 or left.health ==2:
            heart3.visible = False
        if right.health ==1 or left.health ==1:
            heart2.visible = False
        if right.health ==0 or left.health ==0:
            heart.visible = False
        if wave2done >59:
            game.over = True
        #Walkers
        for index in range(30):
            Lwalker[index].move()
            Rwalker[index].move()
            #Finishing Level 2
            if Lwalker[index].isOffScreen("right") and Lwalker[index].visible == True:
                wave2done +=1
                Lwalker[index].visible = False
            if Rwalker[index].isOffScreen("left") and Rwalker[index].visible == True:
                wave2done +=1
                Rwalker[index].visible = False
            if Lbull.collidedWith(Lwalker[index],"rectangle"):
                wave2done +=1
                Lwalker[index].visible = False
                Lbull.visible = False
            if Rbull.collidedWith(Rwalker[index],"rectangle"):
                wave2done +=1
                Rwalker[index].visible = False
                Rbull.visible = False
            if Lwalker[index].collidedWith(left) or Lwalker[index].collidedWith(right):
                zombiesound.play()
                wave2done +=1
                left.health -=1
                right.health -=1
                Lwalker[index].visible = False
            if Rwalker[index].collidedWith(left) or Rwalker[index].collidedWith(right):
                zombiesound.play()
                wave2done +=1
                left.health -=1
                right.health -=1
                Rwalker[index].visible = False
        heart.draw()
        heart2.draw()
        heart3.draw()
        heart4.draw()
        left.draw()
        right.draw()
        Lbull.move()
        Rbull.move()
        game.drawText("Level 2",500,70,F2)
        game.drawText("Health= " + str(right.health),35,70,F2)
        #Floating prevention all together
        if left.y <340 or right.y<340:
            left.y +=5
            right.y +=5
           #Player Controls
        if keys.Pressed[K_SPACE] and left.visible:
            Lbull.moveTo(left.x-20, left.y)
            Lbull.setSpeed(50,90)
            Lbull.visible = True
            gun.play()
        if keys.Pressed[K_SPACE] and right.visible:
            Rbull.moveTo(right.x+20, right.y)
            Rbull.setSpeed(50,270)
            Rbull.visible = True
            gun.play()
        if keys.Pressed[K_RIGHT]:
            right.visible = True
            left.visible = False
            right.nextFrame()
            right.x += 6
        if keys.Pressed[K_LEFT] :
            left.visible = True
            right.visible = False
            left.nextFrame()
            right.x -= 6
        #Prevent player from hiding in the edges
        if left.x <10 or right.x <10:
            left.x += 6
            right.x +=6
        if left.x >600 or right.x >600:
            left.x -=6
            right.x -=6
        game.update(30)

    #Level 3 Boss
    game.over = False
    Rbosswalk.health = 400
    u = 0
    #u helps determine the location where the boss slug will appear
    left.stop()
    right.stop()
    while not game.over and right.health >0:
        game.processInput()
        game.scrollBackground("left",4)
        left.x = right.x
        left.y = right.y
        heart.draw()
        heart2.draw()
        heart3.draw()
        heart4.draw()
        left.draw()
        right.draw()
        Lbull.move()
        Rbull.move()
        Lbosswalk.move()
        Rbosswalk.move()
        downboss.move()
        game.drawText("Final Level",450,70,F2)
        game.drawText("Health= " + str(right.health),35,70,F2)
        #Health
        if right.health==3 or left.health ==3:
            heart4.visible = False
        if right.health ==2 or left.health ==2:
            heart3.visible = False
        if right.health ==1 or left.health ==1:
            heart2.visible = False
        if right.health ==0 or left.health ==0:
            heart.visible = False
        #Double Jump Prevention
        if left.y <340 or right.y<340:
            left.y +=5
            right.y +=5
        if right.y <250 and keys.Pressed[K_UP]:
            right.y +=20
            left.y +=20
           #Player Controls
        if keys.Pressed[K_UP]:
            right.y -=20
            left.y -=20
        if keys.Pressed[K_SPACE] and left.visible:
            Lbull.moveTo(left.x-20, left.y)
            Lbull.setSpeed(50,90)
            Lbull.visible = True
            gun.play()
        if keys.Pressed[K_SPACE] and right.visible:
            Rbull.moveTo(right.x+20, right.y)
            Rbull.setSpeed(50,270)
            Rbull.visible = True
            gun.play()
        if keys.Pressed[K_RIGHT]:
            right.visible = True
            left.visible = False
            right.nextFrame()
            right.x += 6
        if keys.Pressed[K_LEFT] :
            left.visible = True
            right.visible = False
            left.nextFrame()
            right.x -= 6
        #Boss Logic
        if Lbull.collidedWith(Lbosswalk) or Lbull.collidedWith(Rbosswalk):
            Rbosswalk.health -=10
            Lbull.visible = False
        if Rbull.collidedWith(Lbosswalk) or Rbull.collidedWith(Rbosswalk):
            Rbosswalk.health -=10
            Rbull.visible = False
        if Rbosswalk.isOffScreen("left"):
            Rbosswalk.visible = False
            u +=1
        if Lbosswalk.isOffScreen("right"): 
            Lbosswalk.visible = False
            u +=1
        if downboss.y >380:
            downboss.visible = False
        if downboss.y >=-30 and downboss.y <-10:
            a = downboss.angleTo(right)
            downboss.rotateTo(a)
        if downboss.collidedWith(left) or downboss.collidedWith(right):
            downboss.visible = False
            right.health -=1
        #Repeat with same logic
        if u ==2:
            Lbosswalk.visible = True
            downboss.visible = True
            downboss.moveTo(300,-400)
        if u ==3:
            Rbosswalk.visible = True
            Rbosswalk.moveTo(700,300)
        if u ==300:
            game.over = True
        if Lbosswalk.collidedWith(left) or Lbosswalk.collidedWith(right):
            right.health -=1
        if Rbosswalk.collidedWith(left) or Rbosswalk.collidedWith(right):
            right.health -=1
        if Rbosswalk.health <1:
            game.over = True
        #Prevent player from hiding in the edges
        if left.x <10 or right.x <10:
            left.x += 6
            right.x +=6
        if left.x >600 or right.x >600:
            left.x -=6
            right.x -=6
        game.update(30)

    #Stalling for Time, Ends the Game (Secondary Ending)
    game.over = False
    right.moveTo(300,340)
    for index in range(20):
        k = randint(0,500)
        o = randint(-500,-100)
        ufo[index].moveTo(k,o)
    while not game.over and right.health >0 and Rbosswalk.health >0:
        game.scrollBackground("left",4)
        left.move()
        right.move()
        game.drawText("Alien Boss Has Ordered Reinforcements",100,170,F4)
        game.drawText("You Took",30,250,F5)
        game.drawText("Too Long!",30,270,F5)
        Lbosswalk.visible = True
        Lbosswalk.moveTo(10,340)
        for index in range(20):
            ufo[index].visible = True
            if right.visible == True:
                ufo[index].moveTowards(right,5)
            if left.visible == True:
                ufo[index].moveTowards(left,5)
            if ufo[index].collidedWith(left):
                right.health -=1
            if ufo[index].collidedWith(right):
                    right.health -=1
        game.update(30)
        
    #Game Over Screen, GOOD Ending
    game.over = False
    game.clearBackground()
    if right.health >0:
        applause.play()
    game.stopMusic()
    game.clearBackground()
    while not game.over and right.health >0:
        game.processInput()
        bk3.draw()
        game.drawText("Congratulations!",175,100,F)
        game.drawText("You Escaped the Alien Onslaught!",50,150,F)
        game.drawText("PRESS Y to Restart",20,30,F3)
        horse.move()
        if keys.Pressed[K_y]:
            startgame = True
            right.visible = True
            for index in range(40):
             x = randint(50,600)
             y = randint (-800,-100)
             ufo[index].moveTo(x,y)
            for index in range(30):
                x = randint (-1200,-200)
                s = randint(2,4)
                Lwalker[index].moveTo(x,350)
            for index in range(30):
                x = randint (800,1800)
                s = randint(2,4)
                Rwalker[index].moveTo(x,350)
            horse.moveTo(0,345)
            downboss.moveTo(300,-2500)
            Rbosswalk.moveTo(650,340)
            Lbosswalk.moveTo(-1000,340)
            left.moveTo(-40,340)
            right.moveTo(-40,340)
            bk.moveTo(612/2,459/2)
            right.health = 4
            heart.visible = True
            heart2.visible = True
            heart3.visible = True
            heart4.visible = True
            wave2done = 0
            ufosgone = 0
            walkers = 0
            m = 0
            u = 0
            xy +=1
            game.over = True
        game.update(30)

        
    #Game Over Screen, BAD Ending
    left.visible = False
    right.visible = False
    if right.health ==0:
        wasted.draw()
        game.drawText("PRESS Y to Restart",20,30,F3)
        game.stopMusic()
        death.play()
        right.health -=1
        game.update()
         
    while not game.over:
        game.processInput()
        if keys.Pressed[K_y]:
            game.playMusic()
            startgame = True
            right.visible = True
            for index in range(40):
             ufo[index].visible = True
             x = randint(50,600)
             y = randint (-800,-100)
             ufo[index].moveTo(x,y)
            for index in range(30):
                Lwalker[index].visible = True
                x = randint (-1200,-200)
                s = randint(2,4)
                Lwalker[index].moveTo(x,350)
            for index in range(30):
                Rwalker[index].visible = True
                x = randint (800,1800)
                s = randint(2,4)
                Rwalker[index].moveTo(x,350)
            horse.moveTo(0,345)
            downboss.moveTo(300,-2500)
            Rbosswalk.moveTo(650,340)
            Lbosswalk.moveTo(-1000,340)
            left.moveTo(-40,340)
            right.moveTo(-40,340)
            bk.moveTo(612/2,459/2)
            right.health = 4
            heart.visible = True
            heart2.visible = True
            heart3.visible = True
            heart4.visible = True
            downboss.visible = True
            wave2done = 0
            ufosgone = 0
            walkers = 0
            m = 0
            u = 0
            xy +=1
            game.over = True
        game.update(30)
