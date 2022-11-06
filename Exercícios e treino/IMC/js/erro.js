function exibeListaErro (erros) {
    const ul = document.querySelector('#erros')
    ul.innerHTML = '';

    erros.forEach(erro => {
        const li = document.createElement('li');
        li.classList.add('erro')
        li.textContent = erro;
        ul.appendChild(li);
    });
}
