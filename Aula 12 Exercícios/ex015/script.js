function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('ERRO: Verifique os dados e tente novamente')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 12) {
                // Criança
                img.setAttribute('src', 'homembebe.png')
            } else if (idade < 27) {
                // Jovem
                img.setAttribute('src', 'jovemhome.png')
            } else if (idade < 50) {
                // Adulto
                img.setAttribute('src', 'homemadulto.png')
            } else {
                // Idoso
                img.setAttribute('src', 'homemvelho.png')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 12) {
                // Criança
                img.setAttribute('src', 'mulherbebe.png')
            } else if (idade < 27) {
                // Jovem
                img.setAttribute('src', 'jovemmulher.png')
            } else if (idade < 50) {
                // Adulto
                img.setAttribute('src', 'mulheradulta.png')
            } else {
                // Idoso
                img.setAttribute('src', 'mulhervelha.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}