async function onLike(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        const counter = addBtn.parentElement.getElementsByClassName('counter')[0];
        counter.innerText = data;
    } catch (error) {
        console.log(error);
    }

    likeBtn.classList.add('hidden');
    const unlikeBtn = likeBtn.parentElement.getElementsByClassName('unlike')[0];
    unlikeBtn.classList.remove('hidden');
}