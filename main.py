# Name: Brian Swanson
# Github Username: briantswanson
# Date: 11/29/2023
# Class: CS 162 Fall 2023
# Assignment: Portfolio Project
"""
Description:
Write a class named ChessVar that plays an abstract game that is a variant of chess with rules outlined in the readme.
Standard starting positions, simplified piece movement, printing a board is not required. Locations on the board represented with algebraic notation.
"""

"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS FOR HALFWAY PROGRESS REPORT
1. Initializing the ChessVar class:
    a. Creating a new ChessVar object initializes an empty game board and piece inventories for both colors. White ('W') is set as the first turn.
    Players will need to use the 'start_game()' function to set up the board and begin.
2. Keeping track of turn order:
    a. A ChessVar object has a variable named _current_turn that keeps track of the current turn color.
    At the end of the 'make_move()' function the game checks for a winner using 'check_winner()' and if no winner is found then it will run 'set_current_turn()' to change the turn.
3. Keeping track of the current board position:
    a. ChessVar has an object '_game_board' which is a list of 8, each cell has another list of 8 inside. The game board keeps track of the positions.
    'start_game()' places all of the pieces in their default positions and 'make_move()' determines if a move if valid and executes the move, an update to '_game_board'.
4. Determining if a regular move is valid:
    a. 'make_move()' uses multiple conditions and functions to check if a move is valid including:
    * A check to make sure the move is within bounds of the board.
    * A check to make sure the starting_loc has a piece to move.
    * A check to make sure the piece in starting_loc is the correct color.
    * A check for obstructions between starting_loc and ending_loc
    'make_move()' then invokes the object in starting_loc to see if the move is valid based on the piece in starting_loc. If True is returned, the piece moves and the move is valid.
5. Determining if a capture is valid:
    a. Since all captures occur if a valid move is made to a location containing a piece, a valid capture only needs to check the color of the piece.
    If the color of the piece is opposite of the player and the move is valid, the capture occurs and the piece is subtracted from the captured player's inventory.
6. Determining the current state of game:
    a. After each valid move, the ChessVar 'make_move()' function will run 'check_for_winner()' which will check the inventory of each player's pieces.
    If it is found that a player has 0 of any of their pieces, the winner is chosen and the game ends. If there is no current winner, the state remains 'UNFINISHED' and the turn changes.
"""

"""
Goals:
1. Start Game init that sets up the board - COMPLETE
2. get_game_state function - COMPLETE
3. make_move function:
    a. Check if locations given are in-bounds - COMPLETE
    b. Check to see if start_loc is a valid piece color - COMPLETE
    c. Check if the move is legal based on the piece move rules in start_loc - COMPLETE
    d. Check to see if the path is obstructed - COMPLETE
    e. Ensure that once the turn is complete all valid variables are updated - COMPLETE
    f. Log any captures by subtracting 1 from the player's inventory and check for a win condition - COMPLETE
    """


class ChessVar:
    """Represents a modified chess variant containing methods and data members that allow two players to play against each other."""

    def __init__(self):
        self._game_state = "UNFINISHED"
        self._current_turn = "W"
        self._alpha = "abcdefgh"
        self._game_board = [[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[]]]
        self._game_turn = 1
        self._w_pawn_count = 8
        self._w_rook_count = 2
        self._w_knight_count = 2
        self._w_bishop_count = 2
        self._w_queen_count = 1
        self._w_king_count = 1
        self._b_pawn_count = 8
        self._b_rook_count = 2
        self._b_knight_count = 2
        self._b_bishop_count = 2
        self._b_queen_count = 1
        self._b_king_count = 1
        self._game_board[0][0].append(Rook("a8", "B"))
        self._game_board[0][1].append(Knight("b8", "B"))
        self._game_board[0][2].append(Bishop("c8", "B"))
        self._game_board[0][3].append(Queen("d8", "B"))
        self._game_board[0][4].append(King("e8", "B"))
        self._game_board[0][5].append(Bishop("f8", "B"))
        self._game_board[0][6].append(Knight("g7", "B"))
        self._game_board[0][7].append(Rook("h8", "B"))
        for i in range(len(self._game_board[1])):
            self._game_board[1][i].append(Pawn(self._alpha[i] + str(7), "B"))

        self._game_board[7][0].append(Rook("a1", "W"))
        self._game_board[7][1].append(Knight("b1", "W"))
        self._game_board[7][2].append(Bishop("c1", "W"))
        self._game_board[7][3].append(Queen("d1", "W"))
        self._game_board[7][4].append(King("e1", "W"))
        self._game_board[7][5].append(Bishop("f1", "W"))
        self._game_board[7][6].append(Knight("g1", "W"))
        self._game_board[7][7].append(Rook("h1", "W"))
        for i in range(len(self._game_board[6])):
            self._game_board[6][i].append(Pawn(self._alpha[i] + str(2), "W"))

    def get_game_board(self):
        """
        Prints the game board with algebraic notation.
        """
        numbers = "87654321"
        print("   a     b     c     d     e     f     g     h")
        for i in range(len(self._game_board)):
            print(f"{numbers[i]}{self._game_board[i]}{numbers[i]}")
        print("   a     b     c     d     e     f     g     h")


    def get_game_state(self):
        """
        Returns the current game state.
        :return: self._game_state
        """
        return self._game_state


    def get_current_turn(self):
        """
        Returns the game's current turn.
        :return: self._current_turn
        """
        return self._current_turn

    def set_current_turn(self):
        """
        Setter to change whose turn it currently is.
        :return:
        """
        if self._current_turn == "W":
            self._current_turn = "B"
        else:
            self._current_turn = "W"
            self._game_turn += 1
        print("Current Turn is now: " + self._current_turn)


    def set_game_state(self, winner):
        """
        Sets the game state for a winner.
        Options: WHITE_WON, BLACK_WON
        """
        self._game_state = winner


    def get_game_turn(self):
        """
        Returns the turn the game is on.
        :return: self._game_turn
        """
        return self._game_turn


    def alpha_to_index(self, location):
        """
        Takes in a String location (ex: c5) and returns the index number for the letter to assist with movement.
        :param location: string
        :return: alpha_int
        """
        alpha = "abcdefgh"
        alpha_int = int(alpha.index(location[0]))
        return alpha_int


    def check_for_winner(self):
        """
        Checks the board to see if either player has lost.
        Lose condition is if a player loses all of their pieces of one type.
        Sets the status of the game to 'WHITE_WON' or 'BLACK_WON' depending on the state of the game.
        """

        if self._w_pawn_count == 0 or self._w_rook_count == 0 or self._w_knight_count == 0 or self._w_bishop_count == 0 or self._w_queen_count == 0 or self._w_king_count == 0:
            self.set_game_state("BLACK_WON")
        elif self._b_pawn_count == 0 or self._b_rook_count == 0 or self._b_knight_count == 0 or self._b_bishop_count == 0 or self._b_queen_count == 0 or self._b_king_count == 0:
            self.set_game_state("WHITE_WON")
        return(self._game_state)


    def make_move(self, start_loc, end_loc):
        """
        Accepts a starting location and ending location. This function:
        1. Checks to see if the piece in starting_loc belongs to the current player.
        2. Checks to see if ending_loc is a valid location
        3. Checks if the game is won.
        If any of those are invalid, return False.
        If the move is valid, move the piece at starting_loc to ending_loc and capture any pieces if they are there.
        Then update the turn and return True.
        :param start_loc:
        :param end_loc:
        :return: True or False
        """

        alpha = "abcdefgh"

        if alpha.index(start_loc[0]) == -1 or alpha.index(end_loc[0]) == -1 or 0 > int(start_loc[1]) > 8 or 0 > int(end_loc[1]) > 8:
            # move is out of bounds
            print("A parameter was out of bounds: " + start_loc + " " + end_loc)
            return False

        def location_checker(location):
            """
            Returns the object in location, returns None if the location is empty.
            :param location: either starting_loc or ending_loc
            :return: object at location
            """

            outer_index = 8-int(location[1])
            inner_index = self.alpha_to_index(location[0])
            if len(self._game_board[outer_index][inner_index]) == 0:
                return None
            return self._game_board[outer_index][inner_index][0]

        def capture_checker(end_loc_object):
            """
            Returns True or False if an object is located at end_loc.
            :param end_loc_object:
            :return: True or False
            """
            if end_loc_object is not None:
                return True
            return False

        def capture_success(captured_piece):
            """
            Subtracts from the player's inventory if a capture is successful.
            :param end_loc_object:
            :return:
            """
            capture_color = captured_piece.get_name()[1]
            capture_type = captured_piece.get_name()[0]

            if capture_color == "W":
                if capture_type == "P":
                    self._w_pawn_count -= 1
                elif capture_type == "R":
                    self._w_rook_count -= 1
                elif capture_type == "B":
                    self._w_bishop_count -= 1
                elif capture_type == "H":
                    self._w_knight_count -= 1
                elif capture_type == "Q":
                    self._w_queen_count -= 1
                elif capture_type == "K":
                    self._w_king_count -= 1

            if capture_color == "B":
                if capture_type == "P":
                    self._b_pawn_count -= 1
                elif capture_type == "R":
                    self._b_rook_count -= 1
                elif capture_type == "B":
                    self._b_bishop_count -= 1
                elif capture_type == "H":
                    self._b_knight_count -= 1
                elif capture_type == "Q":
                    self._b_queen_count -= 1
                elif capture_type == "K":
                    self._b_king_count -= 1

        def obstruction_checker(start_loc, end_loc):
            """
            Checks the path between start_loc and end_loc and determines if the path is obstructed.
            Knights are exempt from obstructed paths.
            :param start_loc:
            :param end_loc:
            :return: True or False
            """
            alpha = "abcdefgh"

            if start_loc[0] == end_loc[0]:
                # vertical move condition
                if int(end_loc[1]) > int(start_loc[1]):
                    for i in range(int(start_loc[1])+1, int(end_loc[1])):
                        if location_checker(start_loc[0]+str(i)) is not None:
                            return False
                else:
                    for i in range(int(end_loc[1]), int(start_loc[1])-1):
                        if location_checker(start_loc[0]+str(i)) is not None:
                            return False
                return True

            elif start_loc[1] == end_loc[1]:
                # horizontal move condition
                start_alpha_index = self.alpha_to_index(start_loc[0])
                end_alpha_index = self.alpha_to_index(end_loc[0])
                if end_alpha_index > start_alpha_index:
                    for i in range(start_alpha_index+1, end_alpha_index):
                        if location_checker(str(alpha[i] + start_loc[1])) is not None:
                            return False
                else:
                    for i in range(end_alpha_index-1, start_alpha_index):
                        if location_checker(str(alpha[i],start_loc[1])) is not None:
                            return False
                return True

            else:
                start_horizontal_index = self.alpha_to_index(start_loc[0])
                end_horizontal_index = self.alpha_to_index(end_loc[0])
                start_vert_index = int(start_loc[1])
                end_vert_index = int(end_loc[1])
                next_loc = None

                if end_horizontal_index > start_horizontal_index:
                    # diagonal move right, start at d end at h
                    spaces_moved = end_horizontal_index - start_horizontal_index
                    if end_vert_index > start_vert_index:
                        # diag move right and up
                        for i in range (1, spaces_moved):
                            if next_loc is None:
                                next_loc = alpha[start_horizontal_index+i] + str(start_vert_index+i)
                            if location_checker(next_loc) is None:
                                prev_loc = next_loc
                                if prev_loc[0] != "h":
                                    next_loc = str(alpha[self.alpha_to_index(prev_loc) + 1]) + str(int(prev_loc[1]) + 1)
                            else:
                                print(next_loc + " is occupied.")
                                return False
                        return True

                    else:
                        # diag move right and down
                        for i in range(1, spaces_moved):
                            if next_loc is None:
                                next_loc = alpha[start_horizontal_index + i] + str(start_vert_index - i)
                            if location_checker(next_loc) is None:
                                prev_loc = next_loc
                                if prev_loc[0] != "h":
                                    next_loc = str(alpha[self.alpha_to_index(prev_loc) + 1]) + str(int(prev_loc[1]) - 1)
                            else:
                                print(next_loc + " is occupied.")
                                return False
                        return True

                if start_horizontal_index > end_horizontal_index:
                    # diagonal move left, start at h and at d
                    spaces_moved = start_horizontal_index - end_horizontal_index
                    if end_vert_index > start_vert_index:
                        # diag move left and up
                        for i in range(1, spaces_moved):
                            if next_loc is None:
                                next_loc = alpha[start_horizontal_index - i] + str(start_vert_index + i)
                            if location_checker(next_loc) is None:
                                prev_loc = next_loc
                                if prev_loc[0] != "a":
                                    next_loc = str(alpha[self.alpha_to_index(prev_loc) - 1]) + str(int(prev_loc[1]) + 1)
                            else:
                                print(next_loc + " is occupied.")
                                return False
                        return True
                    else:
                        # diag move left and down
                        for i in range(1, spaces_moved):
                            if next_loc is None:
                                next_loc = alpha[start_horizontal_index - i] + str(start_vert_index - i)
                            if location_checker(next_loc) is None:
                                prev_loc = next_loc
                                if prev_loc[0] != "a":
                                    next_loc = str(alpha[self.alpha_to_index(prev_loc) - 1]) + str(int(prev_loc[1]) - 1)
                            else:
                                print(next_loc + " is occupied.")
                                return False
                        return True

            return False

        start_loc_object = location_checker(start_loc)
        end_loc_object = location_checker(end_loc)
        capture_attempt = capture_checker(end_loc_object)

        if start_loc_object is None:
            # No object found at starting_loc
            print("Object at " + start_loc + "not found.")
            return False

        if start_loc_object.get_color() != self._current_turn:
            # Object at start_loc is not the correct color
            print("wrong color")
            return False

        if end_loc_object is not None and end_loc_object.get_color() == self.get_current_turn():
            # If there is an object at the end location of your same color, fail the movement
            print("piece of same color at end_loc")
            return False

        if start_loc_object.get_name()[0] != "H" and not obstruction_checker(start_loc,end_loc):
            # if path is not obstructed, knight excluded
            print("Path from " + start_loc + " to " + end_loc + " is obstructed")
            return False

        if start_loc_object.check_if_valid(capture_attempt, end_loc):
            # Check to see if start_loc_object has determined the move is valid based on what turn it is, if a capture is attempted and if end_loc is valid for the piece
            start_outer_index = 8 - int(start_loc[1])
            start_inner_index = self.alpha_to_index(start_loc[0])
            end_outer_index = 8 - int(end_loc[1])
            end_inner_index = self.alpha_to_index(end_loc[0])
            start_loc_object.set_location(end_loc)
            if capture_attempt:
                capture_success(end_loc_object)
            self._game_board[end_outer_index][end_inner_index].clear()
            self._game_board[end_outer_index][end_inner_index].append(start_loc_object)
            self._game_board[start_outer_index][start_inner_index].clear()
            if self.check_for_winner() != "UNFINISHED":
                return self.get_game_state()
            self.set_current_turn()
            return True

        return False


class Piece:
    """
    Represents a superclass that is intended to be inherited into specific chess pieces.
    Contains a move behavior that checks to ensure that a move is not out of bounds.
    Piece tracks location and if the piece was captured.
    """

    def __init__(self, location, color):
        self._location = location
        self._captured = False
        self._color = color
        self._name = color


    def __repr__(self):
        """
        Edits the function so when printed the name of the object is returned.
        """
        return self._name


    def alpha_to_index(self, location):
        """
        Takes in a String location (ex: c5) and returns the index number for the letter to assist with movement.
        Defined in Piece because all child classes need to use this function to determine valid moves.
        :param location: string
        :return: alpha_int
        """
        alpha = "abcdefgh"
        alpha_int = int(alpha.index(location[0]))
        return alpha_int


    def get_name(self):
        """
        Returns the name of the piece to help visually with the board.
        :return: self._name
        """
        return self._name


    def get_color(self):
        """
        Returns the color of the piece.
        """
        return self._color


    def get_location(self):
        """
        Returns the location of the piece.
        :return: self._location
        """
        return self._location

    def set_location(self, new_location):
        """
        Sets the location string of the Piece. Does not move the piece on the game board.
        :param new_location:
        :return: n/a
        """
        self._location = new_location


    def get_captured(self):
        """
        Returns the captured status of the piece.
        :return: self._captured
        """
        return self._captured


    def set_captured(self, status):
        """
        Sets the captured status of a piece using a boolean.
        """
        self._captured = status


class Pawn(Piece):
    """
    Represents a pawn piece which is a child class of Super Class Piece.
    Pawns can typically move 1 space forward. A Pawn's first move can be 2 spaces forward.
    Pawns capture diagonally one square forward.
    """

    def __init__(self, location, color):
        super().__init__(location, color)
        self._name = "P" + self._name
        self._first_turn = True

    def check_if_valid(self, capture, new_location):
        """
        Checks if a location is valid based on the child class.
        """

        def capture_index_checker(new_location):
            """
            Checks to see if the new location is valid when a Pawn capture is attempted.
            :param new_location:
            :return: True or False
            """
            start_index = self.alpha_to_index(self._location[0])
            end_index = self.alpha_to_index(new_location[0])
            if start_index == 0:
                # Guard in case start_index is at the left bound (a)
                if end_index == start_index + 1:
                    return True

            elif start_index == 7:
                # Guard in case start_index is at the right bound (h)
                if end_index == start_index - 1:
                    return True

            elif end_index == start_index + 1 or end_index == start_index - 1:
                # Condition for start_index 1 - 6
                return True

            return False

        if new_location == str(self._location[0]) + str(int(self._location[1]) + 1) or new_location == str(self._location[0]) + str(int(self._location[1]) - 1) and not capture:
            # Check to see if Pawn is moving 1 space forward
            if self._first_turn:
                self._first_turn = False
            return True

        elif new_location == str(self._location[0]) + str(int(self._location[1]) + 2) and self._first_turn or new_location == str(self._location[0]) + str(int(self._location[1]) - 2) and self._first_turn and not capture:
            # Check to see if Pawn is moving 2 spaces forward in turn 1
            self._first_turn = False
            return True

        elif capture is True:
            # Check to see if we are attempting a capture and the diagonal move is valid
            if capture_index_checker(new_location):
                return True

        return False


class Rook(Piece):
    """
    Represents a rook piece which is a child class of Super Class Piece.
    Rooks can move any number of uninterrupted tiles either horizontally or vertically.
    """

    def __init__(self, location, color):
        super().__init__(location, color)
        self._name = "R" + self._name

    def check_if_valid(self, capture, new_location):
        """
        Checks if a location is valid based on the child class.
        """

        if new_location[0] == self._location[0]:
            # Check to see if Rook is moving Horizontally
            return True

        elif new_location[1] == self._location[1]:
            # Check to see if Rook is moving Vertically
            return True

        return False


class Bishop(Piece):
    """
    Represents a Bishop piece which is a child class of Super Class Piece.
    Bishops can move any number of uninterrupted tiles diagonally.
    """

    def __init__(self, location, color):
        super().__init__(location, color)
        self._name = "B" + self._name

    def check_if_valid(self, capture, new_location):
        """
        Checks if a location is valid based on the child class.
        Bishops move diagonally which can be seen as a square.
        We can use the difference in the vertical movement to ensure the horizontal movement is equal.
        """

        start_horizontal_index = self.alpha_to_index(self._location[0])
        end_horizontal_index = self.alpha_to_index(new_location[0])
        start_vert_index = int(self._location[1])
        end_vert_index = int(new_location[1])
        space_moved_vert = abs(start_vert_index - end_vert_index)
        space_moved_horiz = abs(start_horizontal_index - end_horizontal_index)

        if space_moved_vert == space_moved_horiz:
            # Check to see if Queen is moving diagonally
            return True

        # if the difference is 0, Bishop is not moving and the move is invalid
        return False


class Knight(Piece):
    """
    Represents a Knight piece which is a child class of Super Class Piece.
    Knights move in an L-shape, two spaces in a straight direction and one space perpendicular to that.
    Alphabetically represented with 'H' to not confuse with King
    """

    def __init__(self, location, color):
        super().__init__(location, color)
        self._name = "H" + self._name

    def check_if_valid(self, capture, new_location):
        """
        Checks if a location is valid based on the child class.
        """

        if (int(new_location[1]) == int(self._location[1]) +2) or int(new_location[1]) == int(self._location[1]) - 2:
            if int(self.alpha_to_index(new_location[0])) == int(self.alpha_to_index(self._location[0]))+ 1 or int(self.alpha_to_index(new_location[0])) == int(self.alpha_to_index(self._location[0])) - 1:
                # Check for vertical 2 horizontal 1
                return True

        elif int(self.alpha_to_index(new_location[0])) == int(self.alpha_to_index(self._location[0]))+ 2 or int(self.alpha_to_index(new_location[0])) == int(self.alpha_to_index(self._location[0])) - 2:
            if (int(new_location[1]) == int(self._location[1]) + 1) or int(new_location[1]) == int(self._location[1]) - 1:
                # Check for horizontal 2 vertical 1
                return True

        return False


class Queen(Piece):
    """
    Represents a Queen piece which is a child class of Super Class Piece.
    Queens can move any number of uninterrupted tiles either horizontally, vertically, or diagonally.
    Queens capture another piece of it ends on their space.
    """

    def __init__(self, location, color):
        super().__init__(location, color)
        self._name = "Q" + self._name

    def check_if_valid(self, capture, new_location):
        """
        Checks if a location is valid based on the child class.
        """

        start_horizontal_index = self.alpha_to_index(self._location[0])
        end_horizontal_index = self.alpha_to_index(new_location[0])
        start_vert_index = int(self._location[1])
        end_vert_index = int(new_location[1])
        space_moved_vert = abs(start_vert_index-end_vert_index)
        space_moved_horiz = abs(start_horizontal_index - end_horizontal_index)

        if new_location[0] == self._location[0]:
            # Check to see if Queen is moving Horizontally
            return True

        elif new_location[1] == self._location[1]:
            # Check to see if Queen is moving Vertically
            return True

        elif space_moved_vert == space_moved_horiz:
            # Check to see if Queen is moving diagonally
            return True

        return False


class King(Piece):
    """
    Represents a King piece which is a child class of Super Class Piece.
    Kings can move one tile horizontally, vertically, or diagonally.
    """

    def __init__(self, location, color):
        super().__init__(location, color)
        self._name = "K" + self._name

    def check_if_valid(self, capture, new_location):
        """
        Checks if a location is valid based on the child class.
        """

        start_horizontal_index = self.alpha_to_index(self._location[0])
        end_horizontal_index = self.alpha_to_index(new_location[0])

        if new_location == self._location[0] + int(self._location[1]) + 1:
            # Check to see if King is moving 1 space forward
            return True

        elif new_location == self._location[0] + int(self._location[1]) - 1:
            # Check to see if King is moving 1 space backward
            return True

        elif end_horizontal_index == start_horizontal_index + 1 or end_horizontal_index == start_horizontal_index - 1:
            if int(new_location[1]) == int(self._location[1]) + 1 or int(new_location[1]) == int(self._location[1]) - 1:
                # Check to see if King is moving diagonally 1 space forward or backward
                return True

        return False
