def whats_next(self):
    winning_lines = [
        # Rows
        [
            self.board_array[0][0],
            self.board_array[0][1],
            self.board_array[0][2],
        ],
        [
            self.board_array[1][0],
            self.board_array[1][1],
            self.board_array[1][2],
        ],
        [
            self.board_array[2][0],
            self.board_array[2][1],
            self.board_array[2][2],
        ],

        # Columns
        [
            self.board_array[0][0],
            self.board_array[1][0],
            self.board_array[2][0],
        ],
        [
            self.board_array[0][1],
            self.board_array[1][1],
            self.board_array[2][1],
        ],
        [
            self.board_array[0][2],
            self.board_array[1][2],
            self.board_array[2][2],
        ],

        # Diagonals
        [
            self.board_array[0][0],
            self.board_array[1][1],
            self.board_array[2][2],
        ],
        [
            self.board_array[0][2],
            self.board_array[1][1],
            self.board_array[2][0],
        ],
    ]

    for line in winning_lines:
        if line == ["X", "X", "X"]:
            return (True, "X has won")

        if line == ["O", "O", "O"]:
            return (True, "O has won")

    board_is_full = all(
        space != " "
        for row in self.board_array
        for space in row
    )

    if board_is_full:
        return (True, "Cat's Game")

    if self.turn == "X":
        return (False, "X's turn")

    return (False, "O's turn")