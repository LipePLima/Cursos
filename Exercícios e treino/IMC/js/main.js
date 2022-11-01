const botao    = document.querySelector('#botao');

botao.addEventListener("click", function(e) {
    e.preventDefault();

    const nome     = document.querySelector('#inome');
    const altura   = document.querySelector('#ialt');
    const peso     = document.querySelector('#ipeso');
    const resposta = document.querySelector('#resposta');

    const valorNome   = nome.value;
    const valorAltura = altura.value;
    const valorPeso   = peso.value;
    const calculaIMC  = (valorPeso / (valorAltura * valorAltura)).toFixed(2);

    resposta.textContent = `${valorNome}, calculei seu IMC e o resultado é ${calculaIMC}`
})
    

