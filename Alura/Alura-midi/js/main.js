function tocarSom(idElementoAudio) {
    const elemento = document.querySelector(idElementoAudio);

    if(elemento && elemento.localName === 'audio') {       
        elemento.play();
    }

    else {
        console.log('Elemento não encontrado ou seletor inválido')
    }
}

const ListaDeTeclas = document.querySelectorAll('.tecla');

for(let contador = 0  ;contador < ListaDeTeclas.length; contador++) {

    const tecla = ListaDeTeclas[contador];
    const instrumento = tecla.classList[1];

    //template string
    const idAudio = `#som_${instrumento}`;

    tecla.onclick = function() {
        tocarSom(idAudio)
    }

    tecla.onkeydown = function(evento) {
        if (evento.code === 'space' || evento.code === 'Enter') {
            tecla.classList.add('ativa') 
        }
    }

    tecla.onkeyup = function() {
        tecla.classList.remove('ativa')
    }
}
