import pygame as pg
import sys
import random

def main():
    clock  = pg.time.Clock()
    pg.display.set_caption("逃げろ効果トン")
    screen_sfc = pg.display.set_mode((1000,600))#Sruface
    screen_rct = screen_sfc.get_rect()  #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")  #Surface
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900,400

    #練習5:爆弾
    bmimg_sfc = pg.Surface((20,20)) # Surface
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0,screen_rct.width)
    bmimg_rct.centery = random.randint(0,screen_rct.height)
    vx, vy = +1,+1

    #pg.display.update()
    clock.tick(0.5)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

    #練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True:  kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True:  kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True:  kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:  kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        #練習6

        bmimg_rct.move_ip(vx, vy)
        #練習５
        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main() #これから実装するゲームのメイン部分
    pg.quit()
    sys.exit()