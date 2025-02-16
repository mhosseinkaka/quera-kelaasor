class Robot_move:
    '''
    This class takes the robot's initial position and range of motion.
    It can update the robot's position based on the method it has.
    If the new position is outside the range of motion, it returns an error message.
    '''
    def __init__(self, length: int, width:int, i_move: int, j_move: int) -> None:

        assert type(length) == int, "enetr yor correct length"
        assert type(width) == int, "enter your correct width"
        assert type(i_move) == int, "enter your correct i"
        assert type(j_move) == int, "enter your correct j"
        self.length = length
        self.width = width
        self.i_move = i_move
        self.j_move = j_move

    def update_position(self, di:int, dj: int) -> None:
        '''
        This class determines the new position of the robot based on the input it is given.
        If it was within the initial range, it updates the position.
        
        '''
        assert type(di) == int, "enter your correct di"
        assert type(dj) == int, "enter your correct dj"
        new_i = self.i_move + di
        new_j = self.j_move + dj

        if 0 <= new_i < self.length and 0 <= new_j < self.width:
            self.i_move = new_i
            self.j_move = new_j
        else:
            print("forbidden move!")

    def move_up(self) -> None:
        '''
        Update robot movement to the right
        '''
        self.update_position(-1, 0)

    def move_down(self) -> None:
        '''
        Update robot movement to the down
        '''
        self.update_position(1, 0)

    def move_left(self) -> None:
        '''
        Update robot movement to the left
        '''
        self.update_position(0, -1)

    def move_right(self) -> None:
        ''''
        Update robot movement to the right
        '''
        self.update_position(0, 1)

    

# test_case_1:
# r = Robot_move(5, 5, 2, 2)  
# r.move_up()  
# r.move_left()  
# r.move_down()  
# r.move_right()  
# r.move_up() 

# test_case_2:
# r = Robot_move(5, 5, 2, 5)  
# r.move_up()  
# r.move_left()  
# r.move_down()  
# r.move_right()  
# r.move_up() 