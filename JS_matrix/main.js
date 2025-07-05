let matrix = [];
const MIN_INT = 1;
const MAX_INT = 10;
const NUM_ROWS = 3;
const NUM_COLUMNS = 3;

for (let i = 0; i < NUM_ROWS; i++) {
    let row = [];
    for (let j = 0; j < NUM_ROWS; j++) {
        let random_int = Math.floor(Math.random() * (MAX_INT - MIN_INT + 1)) + MIN_INT;
        row.push(random_int);
    }
    matrix.push(row);
}

for (let i = 0; i < NUM_ROWS; i++) {
    let output_string = "";
    for (let j = 0; j < NUM_ROWS; j++) {
        output_string += matrix[i][j] + ", "
    }
    let output_string_trunc = output_string.substring(0, output_string.length - 2);
    console.log(output_string_trunc);
}
