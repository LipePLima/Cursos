var nome = document.getElementById('#inome');
var altura = document.getElementById('#ialt');
var peso = document.getElementById('#ipeso');
var resposta = document.getElementById('#resposta');
var botao = document.getElementById('#botao');


function calculaIMC(altura, peso) {
    var imc = peso / (altura*altura)
    return imc
}

botao.onclick = calculaIMC;
alert(nome + 'seu IMC é ' + botao);
