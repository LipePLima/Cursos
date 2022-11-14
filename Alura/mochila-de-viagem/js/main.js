const form  = document.querySelector('#novoItem');
const lista = document.querySelector('#lista');
const itens = JSON.parse(localStorage.getItem("items")) || [];

itens.forEach( (elemento) => {
    criaElemento(elemento)
});

form.addEventListener('submit', (evento) => {
    evento.preventDefault();

    const nome       = evento.target.elements['nome'].value;
    const quantidade = evento.target.elements['quantidade'].value;
    const existe     = itens.find( elemento => elemento.nome == nome.value )
    const itemAtual  = {
        'nome': nome.value,
        'quantidade': quantidade.value
    }

    if (existe) {
        itemAtual.id = existe.id
        
        atualizaElemento(itemAtual)
    } else {
        itemAtual.id = itens.length

        criaElemento(itemAtual)

        itens.push(itemAtual)
    }
    
    itens.push(itemAtual);
    
    localStorage.setItem("items", JSON.stringify(itens))
    
    criaElemento(nome, quantidade);

    form.reset()
})

function criaElemento(item) {
    const novoItem = document.createElement('li');
    const numItem  = document.createElement('strong');

    novoItem.classList.add('item');

    novoItem.innerHTML += nome;
    numItem.innerHTML = quantidade;

    lista.appendChild(novoItem)
    novoItem.appendChild(numItem);
}
