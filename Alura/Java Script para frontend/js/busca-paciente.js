const botaoAdicionar = document.querySelector('#buscar-pacientes');

botaoAdicionar.addEventListener('click', function() {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api-pacientes.herokuapp.com/pacientes");

    xhr.addEventListener('load', function() {
        if (xhr.status == 200) {
            const resposta = xhr.responseText;
            const pacientes = JSON.parse(resposta);

            pacientes.forEach( function(paciente) {
                adicionarPacienteNaTabela(paciente);
            });
        } else {
            console.log(xhr.status);
            console.log(xhr.responseText);
            const errAjax = document.querySelector('#erro-ajax');
            errAjax.classList.remove('invisivel')
        }
    });

    xhr.send();
})
