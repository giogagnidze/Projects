function generatePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols) {
    const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numberChars = "0123456789";
    const symbolChars = "!@#$%^&*()_+-=";

    let allowedChars = "";
    let password = "";

    allowedChars += includeLowercase ? lowercaseChars : "";
    allowedChars += includeUppercase ? uppercaseChars : "";
    allowedChars += includeNumbers ? numberChars : "";
    allowedChars += includeSymbols ? symbolChars : "";

    if (length <= 0) {
        return "(password length must be at least 1)";
    }
    if (allowedChars.length === 0) {
        return "(At least 1 set of characters needs to be selected)";
    }

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * allowedChars.length);
        password += allowedChars[randomIndex];
    }

    return password;
}

document.getElementById("generateBtn").addEventListener("click", function () {
    const passwordLength = parseInt(document.getElementById("passwordLength").value);
    const includeLowercase = document.getElementById("includeLowercase").checked;
    const includeUppercase = document.getElementById("includeUppercase").checked;
    const includeNumbers = document.getElementById("includeNumbers").checked;
    const includeSymbols = document.getElementById("includeSymbols").checked;

    const password = generatePassword(passwordLength, includeLowercase, includeUppercase, includeNumbers, includeSymbols);

    document.getElementById("password").textContent = "Generated password: " + password;
});






// function generatePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols){

//     const lowercaseChars = "abcdefghijklmnopqrstuvwxyz"
//     const UppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
//     const numberChars = "0123456789"
//     const sysmbolChars = "!@#$%^&*()_+-="

//     let allowedChars = ""
//     let password = ""

//     allowedChars += includeLowercase ? lowercaseChars : "";
//     allowedChars += includeUppercase ? UppercaseChars : ""
//     allowedChars += includeNumbers ? numberChars : ""
//     allowedChars += includeSymbols ? sysmbolChars : ""

//     if(length <= 0){
//         return `(password length must be at least 1)`
//     }
//     if(allowedChars.length === 0){
//         return `(At least 1 set of character needs to be selected)`
//     }

//     for(let i = 0; i < length; i++){
//         const randomIndex = Math.floor(Math.random() * allowedChars.length)
//         password += allowedChars[randomIndex]
//     }
 
//     return password
// }

// const passwordLength = 12
// const includeLowercase = true
// const includeUppercase = true
// const includeNumbers = true
// const includeSymbols = true

// const password = generatePassword(passwordLength, 
//                                   includeLowercase, 
//                                   includeUppercase, 
//                                   includeNumbers, 
//                                   includeSymbols)

// console.log(`Generated password: ${password}`);


