let btn = document.querySelector('.btn');
let el = document.querySelector('.special');

btn.addEventListener('click', function () {
    el.scrollIntoView(true, {
        behavior: 'smooth'
    });
});