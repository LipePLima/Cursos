var agora = new Date()
var hora = agora.getHours()
var minuto = agora.getMinutes()
console.log(`São exatamente ${hora}:${minuto} horas.`)
if (hora >= 6 && hora < 12) {
    console.log('Bom dia')
} else if (hora < 18) {
    console.log('Boa tarde')
} else {
    console.log('Boa noite')
}