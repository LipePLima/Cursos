// Calculando IMC e validando dados dos pacientes.

// Criando um Array de pacientes com querySelectorAll.
const pacientes = document.querySelectorAll('.paciente'); // querySelector: Seleciona apenas um objeto. / querySelectorAll: Cria um Array.

// Arrow function para calcular o IMC.
const calcIMC  = ( peso, altura ) => (peso / (altura * altura)).toFixed(2);

// Looping para percorrer a array de pacientes.
for (let i = 0; i < pacientes.length; i++ ) {

    // variáveis para colher as informações do paciente.
    const paciente = pacientes[i];
    const peso     = paciente.querySelector('.info-peso').textContent;
    const altura   = paciente.querySelector('.info-altura').textContent;
    const IMC      = paciente.querySelector('.info-imc')

    // Condicionais para validar o cálculo.
    if ( peso <= 1 || peso >= 500 ) {
        IMC.textContent = "Peso inválido"; // Informa o erro
        IMC.classList.add('.valor-invalido'); // altera a cor

    } else if ( altura <= 1 || altura >= 3.00 ) {
        IMC.textContent = "Altura inválida"; // Informa o erro 
        IMC.classList.add('valor-invalido'); // altera a cor

    } else {
        IMC.textContent = calcIMC(peso, altura);
    }
}
