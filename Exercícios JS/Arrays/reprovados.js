// Metodo filter() utilizado com valores boleanos


const nomes      = ['Ana', 'Marcos', 'Maria', 'Mauro', 'Fernando']
const notas      = [7, 4.5, 8, 7.5, 3]
const reprovados = nomes.filter( (aluno, indice) => notas[indice] < 5)

console.log(reprovados)
