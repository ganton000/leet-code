export {}

const createSetArray = (length: number) => Array(length).fill(0).map(_ => new Set()) as Array<Set<string>>;

function isValidSudoku(board: string[][]): Boolean {
	let rows: string[] = [];
	let cols: string[] = [];
	let sub_board: string[] = [];

	console.log(createSetArray(board.length));

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