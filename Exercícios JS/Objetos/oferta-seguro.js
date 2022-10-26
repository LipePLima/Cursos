// Percorrer um objeto, verificar se existe a chave 'dependetes' e, caso exista, enviar uma mensagem de oferta de seguro.

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
    ]
}

for (let info in clientes) {
    
}
