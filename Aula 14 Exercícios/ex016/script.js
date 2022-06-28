function Contar() {
    var inicio = document.getElementById("txtinit")
    var fim = document.getElementById("txtfim")
    var passo = document.getElementById("txtpass")
    var res = document.getElementById("res")

    if (inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0) {
        res.innerHTML = "Impossivel contar!"
        window.alert("ERRO: Tente novamente")
    } else {
        res.innerHTML = "Contando: <br>"
        var ini = Number(inicio.value)
        var f = Number(fim.value)
        var pass = Number(passo.value)
        
        if (pass <= 0) {
            window.alert('Passo inválido. Considerando PASSO igual a 1')
            pass = 1
        }
        // Contagem crescente
        if (ini < f) {
            for(let c = ini; c <= f; c += pass) {
            res.innerHTML += `${c} \u{1F449} `
            }
        } else {
            // Contagem Regressiva
            for(let c = ini; c >= f; c -= pass) {
                res.innerHTML += `${c} \u{1F449}`
            }
        } 
        res.innerHTML += `\u{1F3c1}`
    }
}