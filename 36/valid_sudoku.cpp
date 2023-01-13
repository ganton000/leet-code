#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;



bool isValidSudoku(const vector<vector<char>> &board) {

	int length = board.size();

	vector<set<char>> rows(length), cols(length), sub_boards(length);
	pair<set<char>::iterator, bool> hasValue;

	for(size_t i{0}; i < length; ++i) {
		for(size_t j{0}; j < board[0].size(); ++j) {
			int sub_board_idx = 3*floor(i/3) + floor(j/3);

			char cell = board[i][j];
			if (cell == '.') continue;

			hasValue = rows[i].insert(cell);
			if (!hasValue.second) return false;

			hasValue = cols[j].insert(cell);
			if (!hasValue.second) return false;

			hasValue = sub_boards[sub_board_idx].insert(cell);
			if (!hasValue.second) return false;
		}
	}

	return true;
}

int main() {


	const vector<vector<char>> board  = {
		{'5','3','.','.','7','.','.','.','.'},
		{'6','.','.','1','9','5','.','.','.'},
		{'.','9','8','.','.','.','.','6','.'},
		{'8','.','.','.','6','.','.','.','3'},
		{'4','.','.','8','.','3','.','.','1'},
		{'7','.','.','.','2','.','.','.','6'},
		{'.','6','.','.','.','.','2','8','.'},
		{'.','.','.','4','1','9','.','.','5'},
		{'.','.','.','.','8','.','.','7','9'}
	};

	const vector<vector<char>> board2 =	{
		{'8','3','.','.','7','.','.','.','.'},
		{'6','.','.','1','9','5','.','.','.'},
		{'.','9','8','.','.','.','.','6','.'},
		{'8','.','.','.','6','.','.','.','3'},
		{'4','.','.','8','.','3','.','.','1'},
		{'7','.','.','.','2','.','.','.','6'},
		{'.','6','.','.','.','.','2','8','.'},
		{'.','.','.','4','1','9','.','.','5'},
		{'.','.','.','.','8','.','.','7','9'}
	};

	bool result = isValidSudoku(board);
	cout << "result: " << boolalpha << result << endl;
	bool result2 = isValidSudoku(board2);
	cout << "result: " << boolalpha << result2 << endl;

	return 0;
}