const buttonHeight = 50
const buttonWidth = 150

const maxWidth = window.innerWidth - buttonWidth;
const maxHeight = window.innerHeight - buttonHeight;

window.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('button');
    const button1 = document.getElementById('button1')
    button.addEventListener('click', () => alert('whyy'))
    button1.addEventListener('click', () => alert('I Know Bebe <3'))
    button.addEventListener('mouseover', () => {
        button.style.left = Math.floor(Math.random() * (maxWidth + 1)) + 'px';
        button.style.top = Math.floor(Math.random() * (maxHeight + 1)) + 'px';
    })
});


