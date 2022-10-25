const clientes = {
    nome: "Felipe",
    idade: 20,
    cpf: "15387642220",
    email: "felipe@email.com",
    fones: ["552292345687", "5521979543215"],
    dependentes: [
        {
            nome: "Sara Lima",
            parentesco: "filha",
            dataNasc: "20/03/2011"
        },
        {
            nome: "Samia Maria",
            parentesco: "filha",
            dataNasc: "04/01/2014"
        }
    ],
    saldo: 100,
    depositar: function (valor) {
        this.saldo += valor
    }
}

clientes.depositar(40)
console.log(clientes.saldo)
