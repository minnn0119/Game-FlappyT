import random # Để tạo số ngẫu nhiên
import sys # Sẽ dùng sys.exit để thoát game
import pygame
from pygame.locals import * # Import pygame cơ bản

# Gán biến cho trò chơi và tạo cửa sổ game.
WINDOWWIDTH = 289
WINDOWHEIGHT = 511

BACKGROUND = pygame.image.load('gallery/img/background.png')

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Flappy Bird')

def main():

    t = T()
    columns = Columns()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.blit(BACKGROUND, (0, 0))

        pygame.display.update()
        fpsClock.tick(FPS)

class T(): #class của nhân vật
    
    def _init_(self): #hàm tạo nhân vật
        pass

    def draw(self): #hàm vẽ nhân vật lên màn hình
        pass

    def update(self): #hàm tạo chuyển động nhân vật
        pass

class Columns(): #class của cột

    def _init_(): #hàm tạo cột
        pass

    def draw(self): #hàm vẽ cột lên màn hình
        pass

    def update(self): #hàm tạo chuyển động cột
        pass

class Score(): #class của bảng tính điểm

    def __init__(self): #hàm tạo bảng tính điểm
       pass
    
    def draw(self): #hàm vẽ bảng tính điểm lên màn hình 
        pass
    
    def update(self, t, columns): # hàm cập nhật bảng tính điểm
        pass

def rectCollision(rect1, rect2): #hàm xử lý va chạm

    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False 


if __name__ == '__main__':

    main()