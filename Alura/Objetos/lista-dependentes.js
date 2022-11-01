const clientes = {
    nome: "Felipe",
    idade: 20,
    cpf: "15387642220",
    email: "felipe@email.com",
    fones: ["552292345687", "5521979543215"],
    dependentes: [{
        nome: "Sara Lima",
        parentesco: "filha",
        dataNasc: "20/03/2011"
    }]
}

clientes.dependentes.push({
    nome: "Samia Maria",
    parentesco: "filha",
    dataNasc: "04/01/2014"
})

const filhaMaisNova = clientes.dependentes.filter( dependente => dependente.dataNasc === "20/03/2011")

console.log(filhaMaisNova[0].nome)
