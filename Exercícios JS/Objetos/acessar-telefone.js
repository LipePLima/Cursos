const clientes = {
    nome: "Felipe",
    idade: 20,
    cpf: "15387642220",
    email: "felipe@email.com",
    fones: ["552292345687", "5521979543215"]
}

// por "fones" ser um array, podemos trabalhar com propriedades do array e neste caso, utilizamos o forEach
clientes.fones.forEach( fone => console.log(fone) )
