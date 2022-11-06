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

function validaAltura (altura) {
    if(altura > 1 && altura < 3) {
        return true;
    } else {
        return false;
    }
}

function validaPeso (peso) {
    if(peso > 1 && peso < 500) {
        return true;
    } else { 
        return false;
    }
}

function validaForm (pessoa) {
    const erros = [];

    if (pessoa.nome.length == 0) {
        erros.push('Digite seu nome')
    }

    if (pessoa.altura.length == 0) {
        erros.push('Digite sua altura')
    } else if (!validaAltura(pessoa.altura)) {
        erros.push('Altura inválida')
    } 

    if (pessoa.peso.length == 0) {
        erros.push('Digite seu peso')
    } else if (!validaPeso(pessoa.peso)) {
        erros.push('Peso inválido')
    }

    return erros;
}

function exibeListaErro (erros) {
    const ul = document.querySelector('#erros')
    ul.innerHTML = '';

    erros.forEach(erro => {
        const li = document.createElement('li');
        li.classList.add('erro')
        li.textContent = erro;
        ul.appendChild(li);
    });
}

