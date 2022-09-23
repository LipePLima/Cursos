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

function verifica() {
    var tentativas = 3;

    while (tentativas >= 1) {
        if (chute.value == numeroPensado) {
            alert('Parabéns, você acertou!')
            break;
        } else { 
            if (chute.value < numeroPensado) {
                alert('Seu número foi menor que o número pensado por mim! Você só tem mais ' + (tentativas) + ' tentativas!');
            } 
            else if (chute.value < numeroPensado) {
                alert('Seu número foi maior que o número pensado por mim! Você só tem mais ' + (tentativas) + ' tentativas!');
            } 
        }
        tentativas--;
    }
}

botao.onclick = verifica;