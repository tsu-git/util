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

    def get_back(self):
        return(self.back)

    def get_left(self):
        return(self.left)

    def get_right(self):
        return(self.right)

    def show_top(self):
        print(self.top)

    def sort_values(self):
        values = []
        values.append(self.get_top())
        values.append(self.get_front())
        values.append(self.get_right())
        values.append(self.get_left())
        values.append(self.get_back())
        values.append(self.get_bottom())
        values.sort()
        return(values)


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

    prompt_1 = "input number of dices: "
    prompt_2 = "input 6 integers as 6 dice sides: "

    NUM_EW_SIDES = 4
    NUM_NS_SIDES = 4
    dice_list = []

    n = int(input(prompt_1).strip())
    
    i = 0
    while True:
        if i >= n:
            break

        try:
            s1, s2, s3, s4, s5, s6 = map(
                                    int, input(prompt_2).strip().split())
        except ValueError:
            print("Received invalid data. Try again.")
            continue

        dice_list.append(dice(s1, s2, s3, s4, s5, s6))
        i += 1
        

    uniq_set = {}
    for d in dice_list:
        sorted_values = d.sort_values()

        # move the minimum value to the front side
        if d.get_left() == sorted_values[0]:
            d.east()
            d.south()
        elif d.get_right() == sorted_values[0]:
            d.west()
            d.south()
        else:
            for j in range(NUM_NS_SIDES):
                if d.get_front() == sorted_values[0]:
                    break
                d.south()

        # decide which value to move
        if d.get_back() != sorted_values[1]:
            available_value_to_move = sorted_values[1]
        else:
            available_value_to_move = sorted_values[2]


        for j in range(NUM_EW_SIDES):
            if d.get_top() == available_value_to_move:
                break
            d.west()

        uniq_key = (d.get_top(), d.get_front(), d.get_right(),
                    d.get_left(), d.get_back(), d.get_bottom())
        uniq_set[uniq_key] = True


    if len(uniq_set) != n:
        print("No")
    else:
        print("Yes")

    sys.exit()

