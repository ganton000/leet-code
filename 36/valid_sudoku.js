"use strict";
exports.__esModule = true;
var createSetArray = function (length) { return Array(length).fill(0).map(function (_) { return new Set(); }); };
var createSubBoard = function (i, j) { return 3 * Math.floor(j / 3) + Math.floor(i / 3); };
function isValidSudoku(board) {
    var rows = createSetArray(board.length);
    var cols = createSetArray(board.length);
    var sub_boards = createSetArray(board.length);
    for (var i = 0; i < board.length; i++) {
        for (var j = 0; j < board[0].length; j++) {
            var cell = board[i][j];
            if (cell === ".")
                continue;
            var sub_board = createSubBoard(i, j);
            if (rows[i].has(cell) || cols[j].has(cell) || sub_boards[sub_board].has(cell)) {
                return false;
            }
            else {
                rows[i].add(cell);
                cols[j].add(cell);
                sub_boards[sub_board].add(cell);
            }
        }
    }
    return true;
}
function main() {
    var board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ];
    var board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ];
    var result = isValidSudoku(board);
    var result2 = isValidSudoku(board2);
    console.log(result);
    console.log(result2);
}
main();
