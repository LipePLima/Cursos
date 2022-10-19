const listaDeChamada = ['João', ' Ana', ' Caio', ' Lara', ' Marjorie', ' Leo']

// listaDeChamada.splice(1, 2, ' Rodrigo') // os 2 primeiros parametros são para remoção e o terceiro(opcional) é para adição(le-se "a partir da posição 1, remova 2 itens e adicione 'Rodrigo'")

listaDeChamada.splice(2, 0, ' Rodrigo') // Neste caso, iremos adicionar o Rodrigo na posição 2, utilizando o 0 como parametro, isso é possivel

console.log(`Lista de chamada: ${listaDeChamada}`)
