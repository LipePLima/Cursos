// Função padrão

function soma (n1, n2) {
    return n1 + n2
}

console.log(soma(1, 2))

// Expressão de função
const soma = function(n1, n2) { return n1 + n2 }

console.log(soma(1, 2))
 

// A grande diferença entra esta função e a função padrão é o fato desta função não poder ser chamada antes dela(Hoisting), por ser formada dentro de uma variável. E como sabemos, variáveis não podem ser utilizadas antes de serem processadas.
