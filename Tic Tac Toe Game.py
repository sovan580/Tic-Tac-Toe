import pygame
pygame.init()
gamedisplay=pygame.display.set_mode((550,550))
pygame.display.set_caption("TIC TAC TOE")
_00=pygame.draw.rect(gamedisplay,(255,255,255),(25,25,150,150))
_01=pygame.draw.rect(gamedisplay,(255,255,255),(200,25,150,150))
_02=pygame.draw.rect(gamedisplay,(255,255,255),(375,25,150,150))
_10=pygame.draw.rect(gamedisplay,(255,255,255),(25,200,150,150))
_11=pygame.draw.rect(gamedisplay,(255,255,255),(200,200,150,150))
_12=pygame.draw.rect(gamedisplay,(255,255,255),(375,200,150,150))
_20=pygame.draw.rect(gamedisplay,(255,255,255),(25,375,150,150))
_21=pygame.draw.rect(gamedisplay,(255,255,255),(200,375,150,150))
_22=pygame.draw.rect(gamedisplay,(255,255,255),(375,375,150,150))
run=True
draw_obj="rect"
_00_open=True
_01_open=True
_02_open=True
_10_open=True
_11_open=True
_12_open=True
_20_open=True
_21_open=True
_22_open=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                _00_open=True
                _01_open=True
                _02_open=True
                _10_open=True
                _11_open=True
                _12_open=True
                _20_open=True
                _21_open=True
                _22_open=True
                _00=pygame.draw.rect(gamedisplay,(255,255,255),(25,25,150,150))
                _01=pygame.draw.rect(gamedisplay,(255,255,255),(200,25,150,150))
                _02=pygame.draw.rect(gamedisplay,(255,255,255),(375,25,150,150))
                _10=pygame.draw.rect(gamedisplay,(255,255,255),(25,200,150,150))
                _11=pygame.draw.rect(gamedisplay,(255,255,255),(200,200,150,150))
                _12=pygame.draw.rect(gamedisplay,(255,255,255),(375,200,150,150))
                _20=pygame.draw.rect(gamedisplay,(255,255,255),(25,375,150,150))
                _21=pygame.draw.rect(gamedisplay,(255,255,255),(200,375,150,150))
                _22=pygame.draw.rect(gamedisplay,(255,255,255),(375,375,150,150))
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            if _00.collidepoint(pos) and _00_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(50,50,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(100,100),50)
                    draw_obj="rect"
                _00_open=False
            if _01.collidepoint(pos) and _01_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(225,50,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(275,100),50)
                    draw_obj="rect"
                _01_open=False
            if _02.collidepoint(pos) and _02_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(400,50,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(450,100),50)
                    draw_obj="rect"
                _02_open=False
            if _10.collidepoint(pos) and _10_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(50,225,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(100,275),50)
                    draw_obj="rect"
                _10_open=False
            if _11.collidepoint(pos) and _11_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(225,225,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(275,275),50)
                    draw_obj="rect"
                _11_open=False
            if _12.collidepoint(pos) and _12_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(400,225,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(450,275),50)
                    draw_obj="rect"
                _12_open=False
            if _20.collidepoint(pos) and _20_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(50,400,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(100,450),50)
                    draw_obj="rect"
                _20_open=False
            if _21.collidepoint(pos) and _21_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(225,400,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(275,450),50)
                    draw_obj="rect"
                _21_open=False
            if _22.collidepoint(pos) and _22_open:
                if draw_obj=="rect":
                    pygame.draw.rect(gamedisplay,(255,0,0),(400,400,100,100))
                    draw_obj="circle"
                else:
                    pygame.draw.circle(gamedisplay,(0,255,0),(450,450),50)
                    draw_obj="rect"
                _22_open=False
    pygame.display.update()
pygame.quit()



