from typing import List

def check_3_by_3(board: List[List[str]]) -> bool:
	for i in range(3):
		for j in range(3):
			row1 = board[3*i][3*j:3*(j+1)]
			row2 = board[3*i+1][3*j:3*(j+1)]
			row3 = board[3*i+2][3*j:3*(j+1)]
			sub_board = row1+row2+row3
			result = transform_array_to_str(sub_board)
			hasNoDuplicates = len(result) == len(set(result))
			if not hasNoDuplicates:
				return False

	return True

def transform_array_to_str(arr: List[str]):
	return "".join(arr).replace(".","")

def remove_value(value: str, possible_values: List[str]):
	try:
		possible_values.remove(value)
		return True
	except ValueError:
		return False

def check_rows(board: List[List[str]]) -> bool:
	for row in board:
		possible_values = ["1","2","3","4","5","6","7","8","9"]
		for val in row:
			if val.isnumeric():
				result = remove_value(val, possible_values)
				if not result:
					return False
	return True


def check_columns(board: List[List[str]]) -> bool:
	for cols in zip(*board):
		str_repr = transform_array_to_str(cols)
		set_count = len(set(str_repr))
		str_count = len(str_repr)
		if set_count != str_count:
			return False

	return True


def isValidSudoku(board: List[List[str]]) -> bool:
	result = check_rows(board)
	if result:
		result = check_columns(board)
		if result:
			result = check_3_by_3(board)
			return result

		return result

	return result

def main(board):

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