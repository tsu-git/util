#!/usr/bin/python

class dice:
    def __init__(self,
                 s1: int = 1, s2: int = 2, s3: int = 3, s4: int = 4,
                 s5: int = 5, s6: int = 6):

        self.set_sides(s1, s2, s3, s4, s5, s6)


    def set_sides(self,
                 s1: int = 1, s2: int = 2, s3: int = 3, s4: int = 4,
                 s5: int = 5, s6: int = 6):
        self.top    = s1
        self.front  = s2
        self.right  = s3
        self.left   = s4
        self.back   = s5
        self.bottom = s6

    def show_top(self):
        print(self.top)

    def north(self):
        top    = self.front
        front  = self.bottom
        right  = self.right    # same as before
        left   = self.left     # same as before
        back   = self.top
        bottom = self.back
        self.set_sides(top, front, right, left, back, bottom)
        

    def south(self):
        top    = self.back
        front  = self.top
        right  = self.right    # same as before
        left   = self.left     # same as before
        back   = self.bottom
        bottom = self.front
        self.set_sides(top, front, right, left, back, bottom)


    def east(self):
        top    = self.left
        front  = self.front    # same as before
        right  = self.top
        left   = self.bottom
        back   = self.back     # same as before
        bottom = self.right
        self.set_sides(top, front, right, left, back, bottom)

        
    def west(self):
        top    = self.right
        front  = self.front    # same as before
        right  = self.bottom
        left   = self.top
        back   = self.back     # same as before
        bottom = self.left
        self.set_sides(top, front, right, left, back, bottom)

        
if __name__ == "__main__":
    import sys

    prompt_1 = "input 6 integers as 6 dice sides: "
    prompt_2 = "input directions: "
    NORTH = "N"
    SOUTH = "S"
    EAST  = "E"
    WEST  = "W"

    s1, s2, s3, s4, s5, s6 = map(int, input(prompt_1).strip().split())
    d = dice(s1, s2, s3, s4, s5, s6)
    
    directions = input(prompt_2).strip()

    for direction in directions:
        if direction == NORTH:
            d.north()
        elif direction == SOUTH:
            d.south()
        elif direction == EAST:
            d.east()
        elif direction == WEST:
            d.west()
        else:
            print(f"wrong direction [{direction}]")
            break

    d.show_top()

    sys.exit()
