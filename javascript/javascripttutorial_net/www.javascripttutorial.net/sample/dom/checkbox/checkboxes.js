 function getSelectedCheckboxValues(name) {
        let checkboxes = document.querySelectorAll(`input[name="${name}"]:checked`);
        let values = [];
        checkboxes.forEach((checkbox) => {
            values.push(checkbox.value);
        });
        return values;
    }

    const btn = document.querySelector('#btn');
    btn.addEventListener('click', (event) => {
        alert(getSelectedCheckboxValues('color'));
    });    