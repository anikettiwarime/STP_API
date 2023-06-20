let api = 'http://127.0.0.1:8000/api/standards/'

const getStandards = () => {
    fetch(api)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            renderStandards(data);
        })
}

const renderStandards = (standard) => {
    let section = document.getElementById('section-1');
    standard.forEach(element => {
        console.log(element);
        let card = `
        <div>${element.name}</div>
        `
        section.innerHTML += card;

    });
}



getStandards()