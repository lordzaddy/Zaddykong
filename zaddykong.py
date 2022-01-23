import   pygame 

pygame.init()

size = width, height = 1200, 800 
speed = [0,0]
black = 0 ,0 ,0
x = 1
y = 1
vel = 0.5
jumpyjump=False
jump=1 

window=pygame.display.set_mode(size)
pygame.display.set_caption("ZaddyKong")
hero=pygame.image.load("minnymaymay.xcf")


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit ()
    if event.type ==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            x-= vel
        if event.key ==pygame.K_RIGHT:
            x+= vel 
        if event.key==pygame.K_UP:
            jumpyjump= True
            if jumpyjump == True: 
              y-= jump 
        if event.key ==pygame.K_DOWN:
            y+= vel 

        




    window.fill(black)
    window.blit(hero, (x,y))
    pygame.display.flip() 