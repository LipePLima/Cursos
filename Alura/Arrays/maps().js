//  map() cria uma nova matriz preenchida com os resultados da chamada de uma função fornecida em cada elemento na matriz de chamada.

// somar mais 1 ponto em cada nota
const notas = [10, 9, 8, 7, 6]

const notasAtualizadas = notas.map( nota => nota == 10 ? nota : ++nota)

console.log(notasAtualizadas)

console.log('----------------')

// padronizar a escrita de cada nome dentro do array
let nomes = ['ana Julia', 'Caio vinicius', 'BIA silva']

const nomesAtualizados = nomes.map( nome => nome.toUpperCase() )

console.log(nomesAtualizados)
