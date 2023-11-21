// Si los campos requeridos han sido completados, se activa el botón de envío del formulario.
window.addEventListener('load', () => {
    const form = document.querySelector('form');
    const submitButton = document.querySelector('#btn_enviar');
    const checkbox = document.querySelector('#condiciones');

    form.addEventListener('input', () => {
        if (!submitButton.disabled) {
            checkFormValidity();
        }
    });

    checkbox.addEventListener('change', () => {
        submitButton.disabled = !checkbox.checked;
        checkFormValidity();
    });

    function checkFormValidity() {
        const formFields = [...form.elements].filter(field => field.required);
        const formIsValid = formFields.every(field => field.value || field.checked);
        submitButton.disabled = !(formIsValid && checkbox.checked);
    }
});