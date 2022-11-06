const form     = document.querySelector('.container__form')
const botao    = document.querySelector('#botao');
const resposta = document.querySelector('#resposta');
const calcIMC  = ( peso, altura) => (peso / (altura*altura)).toFixed(2);
 
botao.addEventListener("click", function(e) {
    e.preventDefault();

    const pessoa = dados();
    const erro   = validaForm(pessoa);

    if (erro.length > 0) {
        resposta.classList.add('invisivel');
        exibeListaErro(erro);
        return;
    } else {
        exibeListaErro(erro);
        resposta.classList.remove('invisivel')
        resposta.textContent = `${pessoa.nome}, calculei seu IMC e o resultado foi ${pessoa.imc}`
    }

    form.reset();
})

function dados () {
    const nome   = document.querySelector('#inome');
    const altura = document.querySelector('#ialt');
    const peso   = document.querySelector('#ipeso');

    const dados = {
        nome: nome.value,
        peso: peso.value,
        altura: altura.value,
        imc: calcIMC(peso.value, altura.value)
    }

    return dados;
}
