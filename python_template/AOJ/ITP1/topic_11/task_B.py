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

    def get_front(self):
        return(self.front)

    def show_top(self):
        print(self.top)

    def get_left(self):
        return(self.left)

    def get_right(self):
        return(self.right)

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
    prompt_2 = "input number of questions: "
    prompt_3 = "input questions (top, fromt): "

    NUM_EW_SIDES = 4
    NUM_NS_SIDES = 4

    s1, s2, s3, s4, s5, s6 = map(int, input(prompt_1).strip().split())
    d = dice(s1, s2, s3, s4, s5, s6)
    
    n = int(input(prompt_2).strip())

    i = 0
    while True:
        if i >= n:
            break

        try:
            num_t, num_f = map(int, input(prompt_3).strip().split())
        except ValueError:
            print("received invalid data")
            continue
        
        if d.get_left() == num_f:
            d.east()
            d.south()
        elif d.get_right() == num_f:
            d.west()
            d.south()
        else:
            for j in range(NUM_NS_SIDES):
                if d.get_front() == num_f:
                    break
                d.south()

        for j in range(NUM_EW_SIDES):
            if d.get_top() == num_t:
                break
            d.west()
        

        print(d.get_right())
        i += 1

    sys.exit()
