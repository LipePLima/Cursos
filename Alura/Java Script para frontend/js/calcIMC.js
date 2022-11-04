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

    const alturaValida = validaAltura(altura);
    const pesoValido   = validaPeso(peso);
    
    // Condicionais para validar o cálculo.
    if (!pesoValido) {
        IMC.textContent = "Peso inválido"; // Informa o erro
        IMC.classList.add('.valor-invalido'); // altera a cor

    } 
    
    if (!alturaValida) {
        IMC.textContent = "Altura inválida"; // Informa o erro 
        IMC.classList.add('valor-invalido'); // altera a cor

    } 
    
    if (pesoValido && alturaValida) {
        IMC.textContent = calcIMC(peso, altura);
    }
}
