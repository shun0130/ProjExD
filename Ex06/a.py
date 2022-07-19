import pygame as pg
import sys
import random

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect


    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

        
class Bird:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)         # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1

    
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy 


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate   
        self.blit(scr)          


def main():
    clock = pg.time.Clock()
    scr = Screen("戦え！こうかとん", (1000, 600), "fig/pg_bg.jpg")  #こうかとんの画像指定、ウィンドウの大きさ指定
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd1 = Bomb((random.randint(0,255),(random.randint(0,255)),(random.randint(0,255))),10,(+1,+1), scr)  #爆弾一個目(色はランダム)
    bkd2 = Bomb((random.randint(0,255),(random.randint(0,255)),(random.randint(0,255))),10,(+1,+1), scr)  #爆弾二個目(色はランダム)
    bkd3 = Bomb((random.randint(0,255),(random.randint(0,255)),(random.randint(0,255))),10,(+1,+1), scr)  #爆弾三個目(色はランダム)
    hoge = pg.mixer.Sound("sound/mp3_BGM.mp3")  #ゲームプレイ中常にBGMが流れるようにする
    hoge.play()


    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kkt.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)

        if kkt.rct.colliderect(bkd1.rct):   # 爆弾一個目に当たったら爆発の効果音が流れるようにする
            hoge = pg.mixer.Sound("sound/爆発2.mp3")
            hoge.play()
            return

        if kkt.rct.colliderect(bkd2.rct):   # 爆弾二個目に当たったら爆発の効果音が流れるようにする
            hoge = pg.mixer.Sound("sound/爆発2.mp3")
            hoge.play()
            return

        if kkt.rct.colliderect(bkd3.rct):   # 爆弾三個目に当たったら爆発の効果音が流れるようにする
            hoge = pg.mixer.Sound("sound/爆発2.mp3")
            hoge.play()
            return

        pg.display.update()
        clock.tick(400)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()