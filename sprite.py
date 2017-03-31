import pygame
from time import sleep
from pygame import Rect
import Renderer

class Sprite():
    animations = {}
    imgPath = ""
    def loadAssets(self, file):
        temp = loadAnimations(file)
        self.animations = temp[0]
        self.imgPath = temp[1]
    def play(self, animation):
        playAnimation(self.animations.get(animation), self.imgPath)
def playAnimation(animation, imgPath):
    for i in animation:
        Renderer.blit(imgPath, 0, 0, i)
        sleep(0.1666)
def loadAnimations(file):
    #define some variables for returning the talbe
    key = None
    animations={}
    currentAnimation=[]
    #open the file
    with open(file) as f:
        #get the path of the tile map from the first line
       imgPath = f.readline().split(" ")[1].rstrip()
       for line in f:
            try:
                #reset the array
                currentAnimation = []
                #get the key and remove whitespace
                key = line.split(" ")[1].rstrip()
                #skip the desc and header lines
                trash = f.readline()
                trash = f.readline()
                while(True):
                    #split the coords by - and put into a list
                    line = f.readline().split("-")
                    #if the line is end, exit the loop and move onto next animation
                    if line[0].rstrip() == "end":
                        break
                    #convert all items in the array to int
                    cycle = 0
                    for i in line:
                        line[cycle] = int(i)
                        cycle = cycle + 1
                    #create a rectangle object
                    area = Rect(0, 0, 0, 0)
                    #set the x, y, h, w from the current line being read
                    area.x = line[0]
                    area.y = line[1]
                    area.w = line[2] - line[0]
                    area.h = line[3] - line[1]
                    #add the area to the animation
                    currentAnimation.append(area)
                #add the animation the the map/dictonary of animations
                animations[key] = currentAnimation
                
            except Exception as e:
                print(e)
    #return both the imgpath and animation
    return [animations, imgPath]