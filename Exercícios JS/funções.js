//  let x = "";
// console.log(x);
// x = "oi";

// 1) declara a função 

function imprimeMath (a, b) {

    console.log('---------------------');

    const soma  = Math.round(a + b);
    const sub   = Math.ceil(a - b);
    const mult  = Math.floor(a * b);
    const div   = Math.trunc(a / b);
    const total = `${soma}  ${sub}  ${mult}  ${div}`;

    console.log(total)
}

function imprimeOutrasMath (a = 1, b = 1) {
    console.log('---------------------');

    const pontencia = Math.pow(a, b);
    const raiz      = Math.sqrt(a);
    const min       = Math.min(a, b);
    const max       = Math.max(a, b);
    const aleatorio = Math.round(Math.random()*10);
    const total     = `${pontencia}  ${raiz}  ${min}  ${max}  ${aleatorio}`

    return total
}


// 2) executa a função (1 ou + vezes)

imprimeMath(5, 3)
console.log(imprimeOutrasMath(9, 2))


 