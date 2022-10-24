// O método reduce() precisa de 2 parametros(o acumulador e o atual). 

const salaJS     = [7, 8, 8, 10, 6.5, 4, 10, 7]
const salaJava   = [6, 5, 8, 9, 5, 6]
const salaPython = [7, 3.5, 8, 9.5]

// Função mediaSala para reduzir o código e não tornar repetitivo o processo de somar todos os valores de cada variável.
function mediaSala(notasDaSala) {
    // Arrow function para realizar a soma e armazenar na variavel somaDasNotas.
    const somaDasNotas = notasDaSala.reduce( (acum, atual) => atual + acum, 0 ) // O 0 foi colocado para representar o numero inicial da soma.
    return somaDasNotas / notasDaSala.length
}

console.log(`Média da sala de JavaScript é ${mediaSala(salaJS)}`)
console.log(`Média da sala de Java é ${mediaSala(salaJava)}`)
console.log(`Média da sala de Python é ${mediaSala(salaPython)}`)

console.log('--------------')

// um exemplo mais simples do método reduce()

const notas = [10, 6.5, 8, 7]
const media = notas.reduce( (acum, atual) => atual + acum, 0 ) / notas.length

console.log(media)
