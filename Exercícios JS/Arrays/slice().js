const nomes = ['João', 'Juliana', 'Ana', 'Caio', 'Lara', 'Marjorie', 'Guilherme', 'Aline', 'Fabiana', 'Andre', 'Carlos', 'Paulo', 'Bia', 'Vivian', 'Isabela', 'Vinicius', 'Renan', 'Renata', 'Daisy', 'Camilo']

const sala1 = nomes.slice(0, nomes.length/2) // Vai de João até Andre, ou seja, de 0 até 9 
const sala2 = nomes.slice(nomes.length/2) // O resultado desse calculo será 10, então como só tem um parametro, a função partira do número 10 até o final. Ou seja, de Carlos até Camilo

console.log(`Alunos da sala 1: ${sala1}`)
console.log(`Alunos da sala 2: ${sala2}`)

