class NQueen {

    constructor(size) {

        this.board = new Array(size).fill().map(() => new Array(size).fill('.'))
        this.size = size
    }

	isValid([row, col]){
    // function to check if the placement of the queen in the given location is valid

    // checking the left of the current row

		for(let i=0; i < col; i++)
		{
			if(this.board[row][i] === 'Q') return false
		}


        // checking the upper left diagonal
        for(let i=row, j=col; i >=0 && j >=0; i--, j--){
            if(this.board[i][j] === 'Q') return false
        }

        // checking the lower left diagonal
        for(let i=row, j=col; j>= 0 && i < this.size; i++, j--){
            if (this.board[i][j] === 'Q') return false
        }

        return true
	}

    solve(col =0){
        // function to solve the board
		console.log(`col ${col}`)
        if(col >= this.size) { return true }

        for(let i=0; i< this.size; i++){
            if(this.isValid([i, col])){
                this.board[i][col] = 'Q'
				console.log('board ', this.board[i][col])
                if(this.solve(col+1)) {console.log(`return true ${col} => ${i}`); return true }

                // backtracking
                this.board[i][col] = '.'
            }
        }
		console.log(`return false ${col}`)
        return false
    }


    printBoard(){
        for(const row of this.board){
            console.log(...row)
        }
    }
}


const main = () => {
    const board = new NQueen(3)

    console.log(board.board)
    board.printBoard()
    console.log('\n')
    board.solve()

    board.printBoard()
}

main()
