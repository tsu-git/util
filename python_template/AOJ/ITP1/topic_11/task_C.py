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

    def get_top(self):
        return(self.top)

    def get_bottom(self):
        return(self.bottom)

    def get_front(self):
        return(self.front)

    def get_left(self):
        return(self.left)

    def get_right(self):
        return(self.right)

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
    prompt_2 = "input 6 integers as another 6 dice sides: "

    NUM_EW_SIDES = 4
    NUM_NS_SIDES = 4

    s1, s2, s3, s4, s5, s6 = map(int, input(prompt_1).strip().split())
    d1 = dice(s1, s2, s3, s4, s5, s6)
    s1, s2, s3, s4, s5, s6 = map(int, input(prompt_2).strip().split())
    d2 = dice(s1, s2, s3, s4, s5, s6)
    
    if d1.get_left() == d2.get_front():
        d1.east()
        d1.south()
    elif d1.get_right() == d2.get_front():
        d1.west()
        d1.south()
    else:
        for j in range(NUM_NS_SIDES):
            if d1.get_front() == d2.get_front():
                break
            d1.south()

    for j in range(NUM_EW_SIDES):
        if d1.get_top() == d2.get_top():
            break
        d1.west()
    
    if d1.get_top() != d2.get_top():
        print("No")
    elif d1.get_bottom() != d2.get_bottom():
        print("No")
    elif d1.get_left() != d2.get_left():
        print("No")
    elif d1.get_right() != d2.get_right():
        print("No")
    else:
        print("Yes")


    sys.exit()

