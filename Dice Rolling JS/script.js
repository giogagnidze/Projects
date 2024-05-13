let playerWins = 0;
let playerLosses = 0;
let ComputerWins = 0;
let ComputerLosses = 0;

function rollDice() {
    let result = Math.floor(Math.random() * 6) + 1;
    let computerMove =  Math.floor(Math.random() * 6) + 1;
    document.getElementById('result').innerText = `You rolled a ${result}. Computer rolled a ${computerMove}`;

    if (result === computerMove) {
        document.getElementById('winner').innerText = 'Tie';
    } else if (result > computerMove) {
        document.getElementById('winner').innerText = 'You Win';
        playerWins++;
        ComputerLosses++;
    } else if (result < computerMove) {
        document.getElementById('winner').innerText = 'You Lose';
        playerLosses++;
        ComputerWins++;
    }

    document.getElementById('score').innerText = `Wins: ${playerWins}, Losses: ${playerLosses}`;
    document.getElementById('computerscore').innerText = `Wins: ${ComputerWins}, Losses: ${ComputerLosses}`;
}