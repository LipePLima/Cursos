// const notas = [10, 6.5, 8, 7.5]

// let somaDasNotas = 0

// a função forEach precida de outra função como parametro, ela é o que se chama de call-back.
// notas.forEach( nota => {
//     somaDasNotas += nota
// })

// let media = somaDasNotas / notas.length

// console.log(media)

const notas1 = [10, 6.5, 8 ,7.5]
const notas2 = [9, 6, 6]
const notas3 = [8.5, 9.5]

const notasGerais = [notas1,notas2,notas3]


let media = 0

for (let i = 0; i < notasGerais.length; i++) {
  for (let j = 0; j < notasGerais[i].length; j++) {
    media += notasGerais[i][j]/notasGerais[i].length;
  }
}

media = media/notasGerais.length

console.log(media)
