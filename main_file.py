import SudokuMaster
	board = SudokuMaster.makeBoard()
	puzzle = SudokuMaster.makePuzzleBoard(board, "easy")
	SudokuMaster.printBoard(puzzle)
	

	if SudokuMaster.solveBoard(puzzle):
	    print("\n Solved Solution is: ")
	    SudokuMaster.printBoard(puzzle)
	else:
	    print("0 Solution")
