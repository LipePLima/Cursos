const form  = document.querySelector('#novoItem');
const lista = document.querySelector('#lista');
const itens = JSON.parse(localStorage.getItem("items")) || [];

itens.forEach( (elemento) => {
    console.log(elemento.nome, elemento.quantidade)
});

form.addEventListener('submit', (evento) => {
    evento.preventDefault();

    const nome       = evento.target.elements['nome'].value;
    const quantidade = evento.target.elements['quantidade'].value;
    const itemAtual  = {
        'nome': nome.value,
        'quantidade': quantidade.value
    }
    
    itens.push(itemAtual);
    
    localStorage.setItem("items", JSON.stringify(itens))
    
    criaElemento(nome, quantidade);

    form.reset()
})

function criaElemento(nome, quantidade) {
    const novoItem = document.createElement('li');
    const numItem  = document.createElement('strong');

    novoItem.classList.add('item');

    novoItem.innerHTML += nome;
    numItem.innerHTML = quantidade;

    lista.appendChild(novoItem)
    novoItem.appendChild(numItem);
}
