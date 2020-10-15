async function AddClick(event) {
    event.preventDefault();
    try {
        let A = document.getElementsByTagName('input')[0].value;
        let B = document.getElementsByTagName('input')[1].value;
        let response = await makeRequest('http://localhost:8000/add/', 'POST', {'A': A, 'B': B});
        let data = await response.json();
        console.log(data)
        let p = document.createElement('p');
        p.innerHTML = data.answer;
        p.style.color = "green";
        let place = document.querySelectorAll('.place')[0];
        place.innerHTML = '';
        place.appendChild(p);
    } catch (error) {
        console.log(error);
    }
}

async function SubtractClick(event) {
    event.preventDefault();

    try {
        let place = document.querySelectorAll('.place')[0];
        place.innerHTML = '';
        let A = document.getElementsByTagName('input')[0].value;
        let B = document.getElementsByTagName('input')[1].value;
        let response = await makeRequest('http://localhost:8000/subtract/', 'POST', {'A': A, 'B': B});
        let data = await response.json();
        let p = document.createElement('p');
        p.innerHTML = data.answer;
        p.style.color = "green";
        place.appendChild(p);
    } catch (error) {
        console.log(error);
    }
}

async function MultilplyClick(event) {
    event.preventDefault();
    try {
        let A = document.getElementsByTagName('input')[0].value;
        let B = document.getElementsByTagName('input')[1].value;
        let response = await makeRequest('http://localhost:8000/multiply/', 'POST', {'A': A, 'B': B});
        let data = await response.json();
        let p = document.createElement('p');
        p.innerHTML = data.answer;
        p.style.color = "green";
        let place = document.querySelectorAll('.place')[0];
        place.innerHTML = '';
        place.appendChild(p);
    } catch (error) {
        console.log(error)
    }
}

async function DivideClick(event) {
    event.preventDefault();

    try {
        let place = document.querySelectorAll('.place')[0];
        place.innerHTML = '';
        let A = document.getElementsByTagName('input')[0].value;
        let B = document.getElementsByTagName('input')[1].value;
        let response = await makeRequest('http://localhost:8000/divide/', 'POST', {'A': A, 'B': B});
        let data = await response.json();
        let p = document.createElement('p');
        p.innerHTML = data.answer;
        p.style.color = "green";
        place.appendChild(p);
    } catch (error) {
        console.log(error);
    }
}

window.addEventListener('load', function () {
    const addButton = document.getElementById('add');
    const subtractButton = document.getElementById('subtract');
    const multiplyButton = document.getElementById('multiply');
    const divideButton = document.getElementById('divide');

    addButton.onclick = AddClick;
    subtractButton.onclick = SubtractClick;
    multiplyButton.onclick = MultilplyClick;
    divideButton.onclick = DivideClick;
    // for (let btn of unlikeButtons) {btn.onclick = onUnlike}
});