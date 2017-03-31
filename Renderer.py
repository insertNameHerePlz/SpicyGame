import pygame
from PIL import Image
canvas = None

def setSurface(screen):
    global canvas
    canvas = screen
def blit(img, x, y, area):
    global canvas
    dab = pygame.image.load(img).convert()
    dab = pygame.transform.scale(dab, (8, 8))
    canvas.blit(dab, (x,y), area)

    

class Camera():
    zoom = 2
    # camera location is from top right corner
    x = 0
    y = 0
    size = [1280, 768]
    mapSizeX = 1024
    mapSizeY = 1024
    tileSize = 32
    mapImg = "map.png"
    area = pygame.Rect(0, 0, 16, 16)
    def __init__(self):
        biomeMap = Image.open("map.png")
        self.tiles = biomeMap.load()
        self.snow = pygame.image.load("snow.png").convert()
        self.snow = pygame.transform.scale(self.snow, (self.tileSize * self.zoom, self.tileSize * self.zoom))
        self.grass = pygame.image.load("grass.png").convert()
        self.grass = pygame.transform.scale(self.grass, (self.tileSize * self.zoom, self.tileSize * self.zoom))
        self.sand = pygame.image.load("sand.png").convert()
        self.sand = pygame.transform.scale(self.sand, (self.tileSize * self.zoom, self.tileSize * self.zoom))

    def draw(self):
        global canvas
        xTile = int(self.x/16)
        yTile = int(self.y/16)
        for x in range(int(self.size[0]/8+1)):
            for y in range(int(self.size[1]/8+1)):
                currentX = xTile + x
                currentY = yTile + y
                #print(x)
                currentTile = self.tiles[currentX, currentY]
                if (currentTile == (0, 255, 0)):
                    canvas.blit(self.snow, (x * 32, y * 32))
                if (currentTile == (255, 0, 255)):
                    canvas.blit(self.snow, (x * 32, y * 32))
                if (currentTile == (255, 0, 0)):
                    canvas.blit(self.sand, (x * 8, y * 8))
                if (currentTile == (0, 0, 255)):
                    canvas.blit(self.grass, (x * self.tileSize * self.zoom, y * self.tileSize * self.zoom))
        pygame.display.flip()
        

    def moveTo(self, x, y):
        # top right x
        TRX = x
        # top right y
        TRY = y
        # bottom left x
        BLX = x + self.size[0]
        #bottom left y
        BLY = y + self.size[1]
        # check if viewframe is inside the map
        TRCornerCheck = TRX < self.mapSizeX and TRX > 0 and TRY <self.mapSizeY and TRY > 0
        BLCornerCheck = BLX < self.mapSizeX and BLX > 0 and BLY <self.mapSizeY and BLY > 0
        if (TRCornerCheck and BLCornerCheck):
            # change the position
            self.area.x = x
            self.area.y = y
        else:
            print("nope")

    # move relative to the current position
    def moveRel(self, x, y):
        self.moveTo( x + self.x, y + self.y)
camera = None
def drawAll():
    if (camera == None):
        camera = Camera()
    global camera
    camera.x += 32
    camera.draw()
