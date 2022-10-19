const num = [100, 200, 300, 400, 500, 600, 700, 800]

for (let i = 0; i < num.length; i++) {
    console.log(i, num[i])
}

console.log('----------------------')
// outro exercicio de for

const notas = [10, 6.5, 8, 7.5]

let somaDasNotas = 0

for (let i = 0; i < notas.length; i++) {
    somaDasNotas += notas[i];
}

let media = somaDasNotas / notas.length;

console.log(media)
