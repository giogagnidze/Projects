let score = JSON.parse(localStorage.getItem('score')) || {
    wins: 0,
    losses: 0,
    ties: 0
};
updateScoreElement();
function playGame(playerMove) {
    const computerMove = pickComputerMove();
    result = '' 
    if(playerMove === 'scissors'){
        result = 'You Lose';
        if (computerMove === 'Rock') {
    }else if (computerMove === 'paper') {
            result = 'You Win';
        }else if (computerMove === 'scissors') {
            result = 'Tie';
        }
    }else if (playerMove === "paper") {
        if (computerMove === 'Rock') {
            result = 'You Win';
        }else if (computerMove === 'paper') {
            result = 'Tie';
        }else if (computerMove === 'scissors') {
            result = 'You Lose';
        }
        
    }else if (playerMove === "Rock") {
        if (computerMove === 'Rock') {
            result = 'Tie';
        }else if (computerMove === 'paper') {
            result = 'You Lose';
        }else if (computerMove === 'scissors') {
            result = 'You Win';
        }
    }
    if (result === 'You Win') {
        score.wins+= 1;
    }else if (result === 'You Lose') {
        score.losses += 1;
    }else if (result === "Tie") {
        score.ties += 1;
    }
    localStorage.setItem('score', JSON.stringify(score));
    updateScoreElement();       
    document.querySelector('.js-result').innerHTML = result;
    document.querySelector('.js-moves').innerHTML = `  You
<img src="./${playerMove}-emoji.png" class="move-icon">
<img src="./${computerMove}-emoji.png" class="move-icon">
Computer`; 
}
function updateScoreElement() {
    document.querySelector('.js-score').innerHTML = `Wins: ${score.wins}, Losses: ${score.losses}, Ties: ${score.ties}`
}



function pickComputerMove() {
    computerMove = '';

    randomNumber = Math.random();

    if (randomNumber >= 0 && randomNumber < 1 / 3) {
        computerMove = 'Rock';
    } else if (randomNumber >= 1 / 3 && randomNumber < 2 / 3) {
        computerMove = 'paper';
    } else if (randomNumber >= 2 / 3 && randomNumber < 1 ) {
        computerMove = 'scissors';
    }

    return computerMove;
    }
