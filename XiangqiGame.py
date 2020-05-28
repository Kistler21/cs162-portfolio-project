# Author: Michael Kistler
# Date: 3/4/2020
# Description: Contains classes for a piece which has children classes for each piece in a game of Xiangqi.
#              Contains a class representing a game of Xiangqi which has methods that allow the game to be played.


class Piece:

    """
    Parent class that all pieces will inherit from.
    Contain private data members for location and color of the piece.
    """

    def __init__(self, starting_pos, color):
        """Creates an instance of a Piece class."""
        self._location = starting_pos
        self._color = color
        self._valid_moves = []
        self._rank = None

    def get_location(self):
        """Returns the location of the piece."""
        return self._location

    def get_color(self):
        """Returns the color of the piece."""
        return self._color

    def get_rank(self):
        """Returns the rank of the piece."""
        return self._rank

    def set_location(self, new_pos):
        """Moves the piece to the inputted position."""
        self._location = new_pos

    def location_to_list(self):
        """Converts the _location attribute to a list representing the location."""
        letter_conversion = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9
        }
        return [letter_conversion[self._location[0]], int(self._location[1:])]

    @staticmethod
    def location_from_list(loc_list):
        """Converts a list representing a location back to an actual location."""
        list_conversion = {
            1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i'
        }
        return list_conversion[loc_list[0]] + str(loc_list[1])

    def get_valid_moves(self):
        """Returns a list of valid moves for the piece."""
        return self._valid_moves

    def __repr__(self):
        """Returns a representation of the object."""
        return f'{self.__class__.__name__}({self._location}, {self._color})'


class General(Piece):

    """Class representing a General piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of a General class."""
        super().__init__(starting_pos, color)
        self._rank = 'General'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        team_pieces = [
            piece for piece in other_pieces if piece.get_color() == self._color]
        team_locations = [piece.location_to_list() for piece in team_pieces]

        location = self.location_to_list()
        valid_moves = []
        # Check move to left
        if location[0] > 4 and [location[0] - 1, location[1]] not in team_locations:
            valid_moves.append(self.location_from_list(
                [location[0] - 1, location[1]]))

        # Check move to right
        if location[0] < 6 and [location[0] + 1, location[1]] not in team_locations:
            valid_moves.append(self.location_from_list(
                [location[0] + 1, location[1]]))

        # Check moves up and down for red
        if self._color == 'red':
            if location[1] > 1 and [location[0], location[1] - 1] not in team_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] - 1]))
            if location[1] < 3 and [location[0], location[1] + 1] not in team_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] + 1]))

        # Check moves up and down for black
        if self._color == 'black':
            if location[1] > 8 and [location[0], location[1] - 1] not in team_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] - 1]))
            if location[1] < 10 and [location[0], location[1] + 1] not in team_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] + 1]))

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'G'


class Advisor(Piece):

    """Class representing an Advisor piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of an Advisor class."""
        super().__init__(starting_pos, color)
        self._rank = 'Advisor'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        team_pieces = [
            piece for piece in other_pieces if piece.get_color() == self._color]
        team_locations = [piece.location_to_list() for piece in team_pieces]

        location = self.location_to_list()
        valid_moves = []
        # Check moves for red
        if self._color == 'red':
            # Check up-right
            if (
                location[0] < 6 and location[1] < 3
                and [location[0] + 1, location[1] + 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 1, location[1] + 1]))

            # Check up-left
            if (
                location[0] > 4 and location[1] < 3
                and [location[0] - 1, location[1] + 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 1, location[1] + 1]))

            # Check down-right
            if (
                location[0] < 6 and location[1] > 1
                and [location[0] + 1, location[1] - 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 1, location[1] - 1]))

            # Check down-left
            if (
                location[0] > 4 and location[1] > 1
                and [location[0] - 1, location[1] - 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 1, location[1] - 1]))

        # Check moves for black
        if self._color == 'black':
            # Check up-right
            if (
                location[0] < 6 and location[1] < 10
                and [location[0] + 1, location[1] + 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 1, location[1] + 1]))

            # Check up-left
            if (
                location[0] > 4 and location[1] < 10
                and [location[0] - 1, location[1] + 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 1, location[1] + 1]))

            # Check down-right
            if (
                location[0] < 6 and location[1] > 8
                and [location[0] + 1, location[1] - 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 1, location[1] - 1]))

            # Check down-left
            if (
                location[0] > 4 and location[1] > 8
                and [location[0] - 1, location[1] - 1] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 1, location[1] - 1]))

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'A'


class Elephant(Piece):

    """Class representing an Elephant piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of an Elephant class."""
        super().__init__(starting_pos, color)
        self._rank = 'Elephant'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        team_pieces = [
            piece for piece in other_pieces if piece.get_color() == self._color]
        other_locations = [piece.location_to_list() for piece in other_pieces]
        team_locations = [piece.location_to_list() for piece in team_pieces]

        location = self.location_to_list()
        valid_moves = []
        # Check moves for red
        if self._color == 'red':
            # Check up-right
            if (
                location[0] < 8 and location[1] < 4
                and [location[0] + 1, location[1] + 1] not in other_locations
                and [location[0] + 2, location[1] + 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 2, location[1] + 2]))

            # Check up-left
            if (
                location[0] > 2 and location[1] < 4
                and [location[0] - 1, location[1] + 1] not in other_locations
                and [location[0] - 2, location[1] + 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 2, location[1] + 2]))

            # Check down-right
            if (
                location[0] < 8 and location[1] > 2
                and [location[0] + 1, location[1] - 1] not in other_locations
                and [location[0] + 2, location[1] - 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 2, location[1] - 2]))

            # Check down-left
            if (
                location[0] > 2 and location[1] > 2
                and [location[0] - 1, location[1] - 1] not in other_locations
                and [location[0] - 2, location[1] - 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 2, location[1] - 2]))

        # Check moves for black
        if self._color == 'black':
            # Check up-right
            if (
                location[0] < 8 and location[1] < 9
                and [location[0] + 1, location[1] + 1] not in other_locations
                and [location[0] + 2, location[1] + 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 2, location[1] + 2]))

            # Check up-left
            if (
                location[0] > 2 and location[1] < 9
                and [location[0] - 1, location[1] + 1] not in other_locations
                and [location[0] - 2, location[1] + 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 2, location[1] + 2]))

            # Check down-right
            if (
                location[0] < 8 and location[1] > 7
                and [location[0] + 1, location[1] - 1] not in other_locations
                and [location[0] + 2, location[1] - 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] + 2, location[1] - 2]))

            # Check down-left
            if (
                location[0] > 2 and location[1] > 7
                and [location[0] - 1, location[1] - 1] not in other_locations
                and [location[0] - 2, location[1] - 2] not in team_locations
            ):
                valid_moves.append(self.location_from_list(
                    [location[0] - 2, location[1] - 2]))

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'E'


class Horse(Piece):

    """Class representing a Horse piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of a Horse class."""
        super().__init__(starting_pos, color)
        self._rank = 'Horse'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        team_pieces = [
            piece for piece in other_pieces if piece.get_color() == self._color]
        other_locations = [piece.location_to_list() for piece in other_pieces]
        team_locations = [piece.location_to_list() for piece in team_pieces]

        location = self.location_to_list()
        valid_moves = []
        # Check up-right
        if (
            location[0] < 9 and location[1] < 9
            and [location[0], location[1] + 1] not in other_locations
            and [location[0] + 1, location[1] + 2] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] + 1, location[1] + 2]))

        # Check up-left
        if (
            location[0] > 1 and location[1] < 9
            and [location[0], location[1] + 1] not in other_locations
            and [location[0] - 1, location[1] + 2] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] - 1, location[1] + 2]))

        # Check down-right
        if (
            location[0] < 9 and location[1] > 2
            and [location[0], location[1] - 1] not in other_locations
            and [location[0] + 1, location[1] - 2] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] + 1, location[1] - 2]))

        # Check down-left
        if (
            location[0] > 1 and location[1] > 2
            and [location[0], location[1] - 1] not in other_locations
            and [location[0] - 1, location[1] - 2] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] - 1, location[1] - 2]))

        # Check right-up
        if (
            location[0] < 8 and location[1] < 10
            and [location[0] + 1, location[1]] not in other_locations
            and [location[0] + 2, location[1] + 1] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] + 2, location[1] + 1]))

        # Check right-down
        if (
            location[0] < 8 and location[1] > 1
            and [location[0] + 1, location[1]] not in other_locations
            and [location[0] + 2, location[1] - 1] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] + 2, location[1] - 1]))

        # Check left-up
        if (
            location[0] > 2 and location[1] < 10
            and [location[0] - 1, location[1]] not in other_locations
            and [location[0] - 2, location[1] + 1] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] - 2, location[1] + 1]))

        # Check left-down
        if (
            location[0] > 2 and location[1] > 1
            and [location[0] - 1, location[1]] not in other_locations
            and [location[0] - 2, location[1] - 1] not in team_locations
        ):
            valid_moves.append(self.location_from_list(
                [location[0] - 2, location[1] - 1]))

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'H'


class Chariot(Piece):

    """Class representing a Chariot piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of a Chariot class."""
        super().__init__(starting_pos, color)
        self._rank = 'Chariot'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        team_pieces = [
            piece for piece in other_pieces if piece.get_color() == self._color]
        enemy_pieces = [
            piece for piece in other_pieces if piece.get_color() != self._color]
        team_locations = [piece.location_to_list() for piece in team_pieces]
        enemy_locations = [piece.location_to_list() for piece in enemy_pieces]

        valid_moves = []
        # Check all moves if piece is moving up
        location = self.location_to_list()
        # Loop until another piece is encountered
        while location[1] < 10:
            if [location[0], location[1] + 1] in team_locations:
                break
            elif [location[0], location[1] + 1] in enemy_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] + 1]))
                break
            else:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] + 1]))
            location[1] += 1

        # Check all moves if piece is moving down
        location = self.location_to_list()
        # Loop until another piece is encountered
        while location[1] > 1:
            if [location[0], location[1] - 1] in team_locations:
                break
            elif [location[0], location[1] - 1] in enemy_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] - 1]))
                break
            else:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] - 1]))
            location[1] -= 1

        # Check all moves if piece is moving right
        location = self.location_to_list()
        # Loop until another piece is encountered
        while location[0] < 9:
            if [location[0] + 1, location[1]] in team_locations:
                break
            elif [location[0] + 1, location[1]] in enemy_locations:
                valid_moves.append(self.location_from_list(
                    [location[0] + 1, location[1]]))
                break
            else:
                valid_moves.append(self.location_from_list(
                    [location[0] + 1, location[1]]))
            location[0] += 1

        # Check all moves if piece is moving left
        location = self.location_to_list()
        # Loop until another piece is encountered
        while location[0] > 1:
            if [location[0] - 1, location[1]] in team_locations:
                break
            elif [location[0] - 1, location[1]] in enemy_locations:
                valid_moves.append(self.location_from_list(
                    [location[0] - 1, location[1]]))
                break
            else:
                valid_moves.append(self.location_from_list(
                    [location[0] - 1, location[1]]))
            location[0] -= 1

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'R'


class Cannon(Piece):

    """Class representing a Cannon piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of a Cannon class."""
        super().__init__(starting_pos, color)
        self._rank = 'Cannon'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        enemy_pieces = [
            piece for piece in other_pieces if piece.get_color() != self._color]
        other_locations = [piece.location_to_list() for piece in other_pieces]
        enemy_locations = [piece.location_to_list() for piece in enemy_pieces]

        valid_moves = []
        # Check all moves if piece is moving up
        location = self.location_to_list()
        collisions = 0
        while location[1] < 10:
            # Check if cannon has encountered another piece yet
            if collisions == 1:
                if [location[0], location[1] + 1] in enemy_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0], location[1] + 1]))
                    break
            else:
                # Check if next spot is occupied
                if [location[0], location[1] + 1] in other_locations:
                    collisions += 1
                else:
                    valid_moves.append(self.location_from_list(
                        [location[0], location[1] + 1]))
            location[1] += 1

        # Check all moves if piece is moving down
        location = self.location_to_list()
        collisions = 0
        while location[1] > 1:
            # Check if cannon has encountered another piece yet
            if collisions == 1:
                if [location[0], location[1] - 1] in enemy_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0], location[1] - 1]))
                    break
            else:
                # Check if next spot is occupied
                if [location[0], location[1] - 1] in other_locations:
                    collisions += 1
                else:
                    valid_moves.append(self.location_from_list(
                        [location[0], location[1] - 1]))
            location[1] -= 1

        # Check all moves if piece is moving right
        location = self.location_to_list()
        collisions = 0
        while location[0] < 9:
            # Check if cannon has encountered another piece yet
            if collisions == 1:
                if [location[0] + 1, location[1]] in enemy_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0] + 1, location[1]]))
                    break
            else:
                # Check if next spot is occupied
                if [location[0] + 1, location[1]] in other_locations:
                    collisions += 1
                else:
                    valid_moves.append(self.location_from_list(
                        [location[0] + 1, location[1]]))
            location[0] += 1

        # Check all moves if piece is moving left
        location = self.location_to_list()
        collisions = 0
        while location[0] > 1:
            # Check if cannon has encountered another piece yet
            if collisions == 1:
                if [location[0] - 1, location[1]] in enemy_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0] - 1, location[1]]))
                    break
            else:
                # Check if next spot is occupied
                if [location[0] - 1, location[1]] in other_locations:
                    collisions += 1
                else:
                    valid_moves.append(self.location_from_list(
                        [location[0] - 1, location[1]]))
            location[0] -= 1

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'C'


class Soldier(Piece):

    """Class representing a Soldier piece."""

    def __init__(self, starting_pos, color):
        """Creates an instance of a Soldier class."""
        super().__init__(starting_pos, color)
        self._rank = 'Soldier'

    def update_valid_moves(self, other_pieces):
        """
        Updates the list of valid moves for the piece.
        Doesn't check if the move puts the General in check.
        """
        team_pieces = [
            piece for piece in other_pieces if piece.get_color() == self._color]
        team_locations = [piece.location_to_list() for piece in team_pieces]

        location = self.location_to_list()
        valid_moves = []
        # Check moves for red
        if self._color == 'red':
            # Check move forward
            if location[1] < 10 and [location[0], location[1] + 1] not in team_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] + 1]))

            # Check if the piece has crossed the river
            if location[1] > 5:
                # Check move to right
                if location[0] < 9 and [location[0] + 1, location[1]] not in team_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0] + 1, location[1]]))

                # Check move to left
                if location[0] > 1 and [location[0] - 1, location[1]] not in team_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0] - 1, location[1]]))

        # Check moves for black
        if self._color == 'black':
            # Check move forward
            if location[1] > 1 and [location[0], location[1] - 1] not in team_locations:
                valid_moves.append(self.location_from_list(
                    [location[0], location[1] - 1]))

            # Check if the piece has crossed the river
            if location[1] < 6:
                # Check move to right
                if location[0] < 9 and [location[0] + 1, location[1]] not in team_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0] + 1, location[1]]))

                # Check move to left
                if location[0] > 1 and [location[0] - 1, location[1]] not in team_locations:
                    valid_moves.append(self.location_from_list(
                        [location[0] - 1, location[1]]))

        self._valid_moves = valid_moves

    def __str__(self):
        """Returns a string representing the piece used in print statements."""
        return self._color.upper()[0] + 'S'


class XiangqiGame:

    """
    Class representing a game of Xiangqi.
    Will contain all of the methods and members needed to make the game playable.
    """

    def __init__(self):
        """Creates an instance of a XiangqiGame class."""
        self._game_state = 'UNFINISHED'
        self._turn = 'red'
        # Initialize all pieces
        self._pieces = [
            General('e1', 'red'), General(
                'e10', 'black'), Advisor('d1', 'red'),
            Advisor('f1', 'red'), Advisor(
                'd10', 'black'), Advisor('f10', 'black'),
            Elephant('c1', 'red'), Elephant(
                'g1', 'red'), Elephant('c10', 'black'),
            Elephant('g10', 'black'), Horse('b1', 'red'), Horse('h1', 'red'),
            Horse('b10', 'black'), Horse('h10', 'black'), Chariot('a1', 'red'),
            Chariot('i1', 'red'), Chariot(
                'a10', 'black'), Chariot('i10', 'black'),
            Cannon('b3', 'red'), Cannon('h3', 'red'), Cannon('b8', 'black'),
            Cannon('h8', 'black'), Soldier('a4', 'red'), Soldier('c4', 'red'),
            Soldier('e4', 'red'), Soldier('g4', 'red'), Soldier('i4', 'red'),
            Soldier('a7', 'black'), Soldier(
                'c7', 'black'), Soldier('e7', 'black'),
            Soldier('g7', 'black'), Soldier('i7', 'black')
        ]
        self._captured_pieces = []

        # Populate all of the initial moves for the pieces
        self.update_moves()

    def get_game_state(self):
        """Returns the current state of the game."""
        return self._game_state

    def is_in_check(self, color):
        """Takes a color as input and returns whether that player is in check."""
        # Locate the general
        for piece in self._pieces:
            if piece.get_color() == color and piece.get_rank() == 'General':
                general_location = piece.get_location()
                break

        enemy_pieces = [
            piece for piece in self._pieces if piece.get_color() != color]

        # See if the General is in any of the enemy pieces valid moves lists
        for piece in enemy_pieces:
            if general_location in piece.get_valid_moves():
                return True

        # Get other general location
        for piece in self._pieces:
            if piece.get_color() != color and piece.get_rank() == 'General':
                enemy_general_location = piece.get_location()
                break

        # Check if Generals are on the same file with no intervening pieces
        if general_location[0] == enemy_general_location[0]:
            non_generals = [
                piece for piece in self._pieces if piece.get_rank() != 'General']
            # Loop through all pieces to see if any are on same file
            for piece in non_generals:
                if piece.get_location()[0] == general_location[0]:
                    return False
            return True

        return False

    def is_game_over(self, color):
        """Takes a color as input and returns whether that player has been defeated."""
        friendly_pieces = [
            piece for piece in self._pieces if piece.get_color() == color]

        # Check if any possible moves do not result in check
        for piece in friendly_pieces:
            for move in piece.get_valid_moves():
                # Make the move
                previous_location = piece.get_location()
                piece_to_capture = self.piece_from_location(move)
                piece.set_location(move)
                if piece_to_capture:
                    self.remove_piece(piece_to_capture)
                self.update_moves()
                in_check = self.is_in_check(color)

                # Undo the move
                piece.set_location(previous_location)
                if piece_to_capture:
                    self.add_piece(piece_to_capture)
                self.update_moves()

                # Return false if the move does not result in check
                if not in_check:
                    return False

        return True

    def piece_from_location(self, location):
        """Takes a location as input and returns the piece on that location."""
        for piece in self._pieces:
            if piece.get_location() == location:
                return piece

    def remove_piece(self, piece):
        """Takes a piece as input and moves it to the captured pieces list."""
        self._pieces.remove(piece)
        self._captured_pieces.append(piece)

    def add_piece(self, piece):
        """Adds a piece back to the game in case of an illegal move."""
        self._captured_pieces.remove(piece)
        self._pieces.append(piece)

    def make_move(self, current_pos, new_pos):
        """
        Takes a piece's current location and location to move to as input and makes
        the move if the move is determined to be valid. Returns True if the move is made
        and False otherwise.
        """
        piece_to_move = self.piece_from_location(current_pos)
        piece_to_capture = self.piece_from_location(new_pos)

        # Check for basic exceptions to a valid move
        if (
            not piece_to_move
            or self._game_state != 'UNFINISHED'
            or self._turn != piece_to_move.get_color()
            or new_pos not in piece_to_move.get_valid_moves()
        ):
            return False

        # Make the move
        piece_to_move.set_location(new_pos)
        if piece_to_capture:
            self.remove_piece(piece_to_capture)
        self.update_moves()

        # Revert the move if it puts the player moving in check
        if self.is_in_check(self._turn):
            piece_to_move.set_location(current_pos)
            if piece_to_capture:
                self.add_piece(piece_to_capture)
            self.update_moves()
            return False

        # Update the turn
        if self._turn == 'red':
            self._turn = 'black'
        else:
            self._turn = 'red'

        # Check if the game is over
        if self.is_game_over(self._turn):
            if self._turn == 'red':
                self._game_state = 'BLACK_WON'
            else:
                self._game_state = 'RED_WON'

        return True

    def update_moves(self):
        """Updates the valid_moves list for all pieces in the game."""
        for current_piece in self._pieces:
            other_pieces = [
                piece for piece in self._pieces if piece != current_piece]
            current_piece.update_valid_moves(other_pieces)

    def __str__(self):
        """Returns a string representation of the board."""
        board = '-' + '|----' * 9 + '|-' + '\n'
        for row in range(10, 0, -1):
            board += ' '
            for column in range(1, 10):
                board += '|'

                # Determine if a piece is in current spot
                piece_check = False
                for piece in self._pieces:
                    if piece.location_to_list() == [column, row]:
                        board += ' ' + str(piece) + ' '
                        piece_check = True
                if not piece_check:
                    board += '    '

            # Print dividers to make board easily readable
                if column == 9:
                    board += f'| {row}\n'
            if row == 6:
                board += ('-' + '|----' * 9 + '|-' + '\n') * 2
            else:
                board += '-' + '|----' * 9 + '|-' + '\n'

        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for col in cols:
            board += f'   {col} '

        return board
