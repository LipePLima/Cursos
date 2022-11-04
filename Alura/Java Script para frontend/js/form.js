// Adicionando novo paciente.

// encontrando o botão.
const btn = document.querySelector('#adicionar-paciente');

// Adicionando uma função para o evento de "click" no botão.
btn.addEventListener("click", function(event) {
    event.preventDefault(); // impedindo que o formulário seja enviar(previnindo a sua função padrão).

    const form     = document.querySelector('#form-adiciona'); // capturando informações do formulário.
    const paciente = dadosNovoPaciente(form);
    const linha    = montaTr(paciente);

    form.reset()
})

function dadosNovoPaciente (form) {
    const paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calcIMC(form.peso.value, form.altura.value)
    }

    return paciente;
}

function montaTr (paciente) {
    const table = document.querySelector('#tabela-pacientes'); // capturando informções da tabela.

    // Criando as tag de linha e coluna para adicionar dados de um novo paciente.
    const pacientetr = document.createElement('tr');
    pacientetr.classList.add('paciente')

    // Atribuindo os "tds" a tag "tr".
    pacientetr.appendChild(montaTd(paciente.nome, 'info-nome'));
    pacientetr.appendChild(montaTd(paciente.peso, 'info-peso'));
    pacientetr.appendChild(montaTd(paciente.altura, 'info-altura'));
    pacientetr.appendChild(montaTd(paciente.gordura, 'info-gordura'));
    pacientetr.appendChild(montaTd(paciente.imc, 'info-imc'));

    // atribuindo a tag "tr" à tabela.
    table.appendChild(pacientetr);
}

// atribuindo os dados inseridos no formulário à linha do novo paciente.
function montaTd (dado, classe) {
    const td = document.createElement('td')
    td.textContent = dado;
    td.classList.add(classe);

    return td;
}
