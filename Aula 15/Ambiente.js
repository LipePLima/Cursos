let num = [9, 0, 1, 2] //Variável Composta
console.log(`Nosso vetor é o ${num}`)
console.log(`A quantidade de numeros é ${num.length}`) //num.length informa a quantidade de valores dentro da variável
console.log('')
num.push(4) //num.push acrescenta um valor no final da variável
console.log(num)
num.sort() //num.sort organiza em ordem crescente os valores
console.log(`Os novos valores são ${num}`)
console.log('')

//Diferentes formas do FOR para informar posição e valor
for (let posicao = 0; posicao < num.length; posicao++) {
    console.log(`A posição ${posicao} tem o valor ${num[posicao]}`)
}
console.log('')
for (let posicao in num) {
    console.log(`A posição ${posicao} tem o valor ${num[posicao]}`)
}
console.log('')
let pos = num.indexOf(0) //num.inderxOf() informa a posição do valor informado entre ()
console.log(pos)
