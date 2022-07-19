import pygame as pg
import sys
import random


def main():
    clock  = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん")
    screen_sfc = pg.display.set_mode((1000,600))#Sruface
    screen_rct = screen_sfc.get_rect()  #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")  #Surface
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    #練習5:爆弾一個目
    bmimg_sfc = pg.Surface((20,20)) # Surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10) #爆弾１の色、座標、大きさの指定
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0,screen_rct.width) #玉の跳ね返り方
    bmimg_rct.centery = random.randint(0,screen_rct.height) #玉の跳ね返り方
    vx, vy = +1,+1

    # 爆弾二個目
    bmimg_sfc2 = pg.Surface((20,20)) # Surface2
    bmimg_sfc2.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc2,(0,0,255),(10,10),10) #爆弾２の色、座標、大きさの指定。
    bmimg_rct2 = bmimg_sfc2.get_rect()
    bmimg_rct2.centerx = random.randint(400,screen_rct.width) #玉の跳ね返り方
    bmimg_rct2.centery = random.randint(200,screen_rct.height) # 玉の跳ね返り方
    vx2, vy2 = +1,+1
    

    #pg.display.update()
    clock.tick(0.5)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #練習４
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True:  kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True:  kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True:  kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:  kkimg_rct.centerx += 1
        #練習7
        if check_bound(kkimg_rct, screen_rct) != (1,1): #領域外だったら
            if key_states[pg.K_UP]    == True:  kkimg_rct.centery += 1
            if key_states[pg.K_DOWN]  == True:  kkimg_rct.centery -= 1
            if key_states[pg.K_LEFT]  == True:  kkimg_rct.centerx += 1
            if key_states[pg.K_RIGHT] == True:  kkimg_rct.centerx -= 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        #練習６ 
        bmimg_rct.move_ip(vx, vy) #爆弾１の動き方
        bmimg_rct2.move_ip(vx2, vy2)#爆弾２の動き方
        #練習５
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        screen_sfc.blit(bmimg_sfc2, bmimg_rct2)
        #練習７
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        yoko, tate = check_bound2(bmimg_rct2, screen_rct)
        vx2 *= yoko
        vy2 *= tate

        if kkimg_rct.colliderect(bmimg_rct) == True: # こうかとんが爆弾にぶつかったら
            print("Game Over!") # ターミナルに表示される。
            return
        if kkimg_rct.colliderect(bmimg_rct2) == True: # こうかとんが爆弾にぶつかったら
            print("Game Over!") #ターミナルに表示される。
            return

        pg.display.update()
        clock.tick(400)

def check_bound(rct,scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''

    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1 #領域外
    if rct.top < scr_rct.top or scr_rct.bottom  < rct.bottom: tate = -1 #領域外
    return yoko,tate

def check_bound2(rct2,scr_rct2):

    yoko, tate = +1, +1 # 領域内
    if rct2.left < scr_rct2.left or scr_rct2.right < rct2.right: yoko = -1 #領域外
    if rct2.top < scr_rct2.top or scr_rct2.bottom  < rct2.bottom: tate = -1 #領域外
    return yoko,tate


if __name__ == "__main__":
    pg.init()
    main() #これから実装するゲームのメイン部分
    pg.quit()
    sys.exit()