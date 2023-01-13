export {}

const createSetArray = (length: number) => Array(length).fill(0).map(_ => new Set()) as Array<Set<string>>;
const createSubBoard = (i: number, j: number): number => 3 * Math.floor(j/3) + Math.floor(i/3);

function isValidSudoku(board: string[][]): Boolean {
	let rows: Array<Set<string>> = createSetArray(board.length);
	let cols: Array<Set<string>> = createSetArray(board.length);
	let sub_boards: Array<Set<string>> = createSetArray(board.length);

	for (let i=0; i< board.length; i++) {
		for(let j=0; j< board[0].length; j++) {
			let cell: string = board[i][j];

			if (cell === ".") continue;

			let sub_board = createSubBoard(i,j);

			if (rows[i].has(cell) || cols[j].has(cell) || sub_boards[sub_board].has(cell)) {
				return false;
			} else {
				rows[i].add(cell);
				cols[j].add(cell);
				sub_boards[sub_board].add(cell);
			}
		}
	}

	return true
}


function main() {

	const board: Array<string[]> = [
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

	const board2: Array<string[]> =	[
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

	const result = isValidSudoku(board);
	const result2 = isValidSudoku(board2);

	console.log(result);
	console.log(result2);


}


main();