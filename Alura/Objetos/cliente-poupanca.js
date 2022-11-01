function cliente(nome, idade, cpf, email, saldo) {
    this.name = nome
    this.year = idade
    this.cpf = cpf
    this.email = email
    this.saldo = saldo
}


class clientePoupanca {
    constructor(nome, idade, cpf, email, saldo, saldoPoup) {
        cliente.call(this, nome, idade, cpf, email, saldo)
        this.saldoPoup = saldoPoup
    }
}

const cliente1 = new clientePoupanca("felipe", 20, '11122233344452', 'felipe@email.com', 300, 200)

console.log(cliente1)
