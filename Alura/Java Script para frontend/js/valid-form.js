function validaPeso (peso) {
    if (peso > 1 && peso < 500) {
        return true;
    } else {
        return false;
    }
}

function validaAltura (altura) {
    if (altura > 1 && altura <= 3.00) {
        return true;
    } else {
        return false;
    }
}

function validaGordura (gordura) {
    if (gordura > 0 && gordura < 90) {
        return true;
    } else {
        return false;
    }
}

function validaPaciente (paciente) {
    const erros = [];

    if (paciente.nome.length == 0) {
        erros.push('Preencha o campo Nome');
    }

    if (paciente.peso.length == 0) {
        erros.push('Preencha o campo Peso');
    } else if (!validaPeso(paciente.peso)) {
        erros.push('O campo Peso é inválido')
    }

    if (paciente.altura.length == 0) {
        erros.push('Preencha o campo Altura')
    } else if (!validaAltura(paciente.altura)) {
        erros.push('O campo Altura é inválido')
    }

    if (paciente.gordura.length == 0) {
        erros.push('Preencha o campo % de gordura');
    } else if (!validaGordura(paciente.gordura)) {
        erros.push('O campo %¨de gordura é inválido')
    }
    
    return erros;
}

function exibeMensagensErro (erros) {
    const ul = document.querySelector('#mensagens-erro');
    ul.innerHTML = '';

    erros.forEach(erro => {
        const li = document.createElement('li');
        li.textContent = erro;
        ul.appendChild(li);
    });
}
