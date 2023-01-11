from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
	row = [set() for _ in range(9)]
	col = [set() for _ in range(9)]
	sub_boxes = [set() for _ in range(9)]

	for i in range(9):
		for j in range(9):
			cell = board[i][j]
			if cell == ".":
				continue

			if cell in row[i]:
				return False
			else:
				row[i].add(cell)

			if cell in col[j]:
				return False
			else:
				col[j].add(cell)

			sub_boxes_index = i//3*3 + j//3
			if cell in sub_boxes[sub_boxes_index]:
				return False
			else:
				sub_boxes[sub_boxes_index].add(cell)

	return True



def main(board: List[List[str]]) -> bool:

	return isValidSudoku(board)

if __name__ == "__main__":
	board = [
		["5","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]

	board2 = [
		["8","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]

	result = main(board)
	print(result)

	result = main(board2)
	print(result)