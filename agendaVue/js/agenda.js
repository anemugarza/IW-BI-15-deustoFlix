contactoEjemplo = {
    "nombre": 'Ane Mugarza',
    "email": 'ane@deusto.com',
    "telf": '555-555-5555'
}

contactoEjemplo2 = {
    "nombre": 'Mar Múgica',
    "email": 'mar@deusto.com',
    "telf": '666-666-6666'
}

contactoEjemplo3 = {
    "nombre": 'Imanol Alonso',
    "email": 'imanol@deusto.com',
    "telf": '777-777-7777'
}

contactoEjemplo4 = {
    "nombre": 'Paule Zugaza',
    "email": 'paule@deusto.com',
    "telf": '888-888-8888'
}


let contactos = new Vue({
    el: "#contactos",
    data: {
        contactos: [contactoEjemplo, contactoEjemplo2],
        nuevoContacto: {
            "nombre": "",
            "email": "",
            "telf": ""
        }
    },
    methods: {
        anyadirContacto() {
            this.contactos.push(this.nuevoContacto);
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