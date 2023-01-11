from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
	col1, col2, col3, col4, col5, col6, col7, col8, col9 = "", "", "", "", "", "", "", "", ""
	for i in range(3):
		row1="".join(board[3*i])
		row2="".join(board[3*i+1])
		row3="".join(board[3*i+2])

			#check rows
		if ((9-row1.count(".")) != (len(set(row1))-1)) | ((9-row2.count(".")) != (len(set(row2))-1)) | \
			((9-row3.count(".")) != (len(set(row3))-1)):
			return False

		col1 += row1[0]+row2[0]+row3[0]
		col2 += row1[1]+row2[1]+row3[1]
		col3 += row1[2]+row2[2]+row3[2]
		col4 += row1[3]+row2[3]+row3[3]
		col5 += row1[4]+row2[4]+row3[4]
		col6 += row1[5]+row2[5]+row3[5]
		col7 += row1[6]+row2[6]+row3[6]
		col8 += row1[7]+row2[7]+row3[7]
		col9 += row1[8]+row2[8]+row3[8]

		#check sub_boards
		for j in range(3):
			sub_board = row1[3*j:3*(j+1)] + row2[3*j:3*(j+1)] + row3[3*j:3*(j+1)]
			if (9-sub_board.count(".")) != (len(set(sub_board))-1):
				return False

	#check cols
	if ((9-col1.count(".")) != (len(set(col1))-1)) | ((9-col2.count(".")) != (len(set(col2))-1)) | \
		((9-col3.count(".")) != (len(set(col3))-1)) | ((9-col4.count(".")) != (len(set(col4))-1)) | \
		((9-col5.count(".")) != (len(set(col5))-1)) | ((9-col6.count(".")) != (len(set(col6))-1)) | \
		((9-col7.count(".")) != (len(set(col7))-1)) | ((9-col8.count(".")) != (len(set(col8))-1)) | \
		((9-col9.count(".")) != (len(set(col9))-1)):
		return False

	return True

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

	false_board = [
		["1","2",".",".",".",".","6",".","7"],
		[".",".",".",".",".",".",".",".","5"],
		[".",".","9",".","6",".","4",".","."],
		[".","6",".",".",".",".",".",".","."],
		[".",".",".",".","4",".",".","7","."],
		[".",".",".",".",".",".",".",".","."],
		[".",".",".","5",".",".",".",".","."],
		[".",".",".",".",".",".",".",".","2"],
		[".","9",".",".",".",".",".",".","7"]
	]

	print(isValidSudoku(board))
	print(isValidSudoku(board2))
	print(isValidSudoku(false_board))

'''
Time Complexity: O(n^2)
'''