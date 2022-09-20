var nome = document.getElementById('#nome')
var altura = document.getElementById('#altura')
var peso = document.getElementById('#peso')
var resposta = document.getElementById('#resposta')


function calculaIMC(altura, peso) {
    var imc = peso / (altura*altura)
    return imc
}

resposta.innerHTML(nome + ' o seu IMC foi ' + calculaIMC());
