// Remova o último elemento da lista de notas e calcule a média

const notas = [10, 7, 8, 5, 10]

notas.pop()
console.log(notas)

let media = (notas[0] + notas[1] + notas[2] + notas[3]) / notas.length;
console.log(media)
