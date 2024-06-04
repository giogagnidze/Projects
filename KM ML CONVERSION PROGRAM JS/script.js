const textBox = document.getElementById("textBox");
const toMiles = document.getElementById("toMiles");
const toKilometers = document.getElementById("toKilometers");
const result = document.getElementById("result");
let temp;

function convert(){
    if(toMiles.checked){
        temp = Number(textBox.value);
        temp *= 0.621371;
        result.textContent = temp + " Miles";
    }
    else if(toKilometers.checked){
        temp = Number(textBox.value);
        temp *= 1.60934;
        result.textContent = temp + " Kilometers";
    }
    else{
        result.textContent = "Select a unit";
    }
}
