// Criar um relatório para análise do cliente

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

// variavel com uma string vazia para ser preenchida pelas informações do objeto
let relatorio = '';

// laço de repetição para percorrer o objeto
for (let info in clientes) {
    // Condicional para não adicionar informações ilegíveis
    if (typeof clientes[info] === 'object' || typeof clientes[info] === 'function') {
        continue
    } else {
        relatorio += `
        ${info} ==> ${clientes[info]}`
    }
}

console.log(relatorio)
