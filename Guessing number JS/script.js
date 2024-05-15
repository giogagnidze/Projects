const minNum = 1;
const maxNum = 100;
const answer = Math.floor(Math.random() * (maxNum - minNum + 1)) + minNum;

let attempts = 0;
let running = true;

function checkGuess() {
    let guessElement = document.getElementById('guessInput');
    let guess = parseInt(guessElement.value);

    let messageElement = document.getElementById('message');

    if(isNaN(guess) || guess < minNum || guess > maxNum) {
        messageElement.textContent = "Please enter a valid number between " + minNum + " and " + maxNum;
    } else {
        attempts++;

        if (guess < answer) {
            messageElement.textContent = "TOO LOW! TRY AGAIN";
        } else if (guess > answer) {
            messageElement.textContent = "TOO HIGH! TRY AGAIN";
        } else {
            messageElement.textContent = "CORRECT! The answer was " + answer + ". It took you " + attempts + " attempts";
            running = false;
        }
    }

    guessElement.value = "";
}