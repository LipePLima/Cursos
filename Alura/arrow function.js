let sub = (n1, n2) => { return n1 - n2 };
console.log(sub(1, 2))

let raiz = n1 => Math.sqrt(n1)
console.log(raiz(4)) 

let soma = (n1, n2) => n1 + n2;
console.log(soma(1, 2))

/* Todas essas são Arrow Function.
        A primeira é uma AF padrão, com parâmetros e um return, que torna obrigatório o uso de {}.

        A segunda, como tem somente 1 parâmetro, não há necessidade de (), da msm maneira que não precisa de um return, logo não precisa de {}.

        A terceira por ter 2 parâmetros, o uso de () se torna obrigatório. Mas ainda assim não há necessidade de return.

        O return e, consequentemente, as {}. Basicamente só serão utilizados para arrow function com mais de uma instrução.
        
        Assim como os () só serão utilizados para AF com mais de 1 parâmetro.

        OBS: AF não tem suporte para hoisting, pois é criada a partir de uma variável
*/ 
