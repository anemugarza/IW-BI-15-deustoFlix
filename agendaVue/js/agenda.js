contactoEjemplo = {
    "nombre": 'John Doe',
    "email": 'john.doe@deusto.es',
    "telf": '555555555'
}

new Vue({
    el: "#contactos",
    data: {
        contactos: [contactoEjemplo],
        nuevoContacto: {
            "nombre": "",
            "email": "",
            "telf": ""
        }
    },
    methods: {
        anyadirContacto() {

            this.contactos.push({
                "nombre": this.nuevoContacto.nombre,
                "email": this.nuevoContacto.email,
                "telf": this.nuevoContacto.telf
            });

            this.nuevoContacto = {
                "nombre": "",
                "email": "",
                "telf": ""
            };
        },
        borrarContacto(indice) {
            this.contactos.splice(indice, 1);
        }
    }
});
