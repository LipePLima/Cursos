var chute = document.querySelector('input')
var botao = document.querySelector('button')

function separa() {
    document.write('<br>');
}

function sorteia(n) {
    return Math.round(Math.random()*n);
}

var numeroPensado = sorteia(parseInt(prompt('Digite até que número eu posso sortear?')));
console.log(numeroPensado);
chute.focus();

function verifica() {
    if (chute.value == numeroPensado) {
        alert('Parabéns, você acertou!')
    } else { 
        if (chute.value < numeroPensado) {
            alert('Seu número foi menor que o número pensado por mim!');
        } else {
            alert('Seu número foi maior que o número pensado por mim!');
        } 
    }
    chute.value = "";
    chute.focus();
}

botao.onclick = verifica;
