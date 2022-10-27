class cliente {
    constructor(nome, idade, cpf, email, saldo) {
        this.name = nome
        this.year = idade
        this.cpf = cpf
        this.email = email
        this.saldo = saldo
    }
}

const dados = new cliente('felipe', 20, 123456789, 'felipe@email.com', 300, 500)

console.log(dados)
