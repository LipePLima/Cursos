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
