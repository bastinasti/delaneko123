

var url = "https://apis.digital.gob.cl/dpa/regiones";

fetch(url).then(function (result) {
  if (result.ok) {
    return result.json();
  }

}).then(function (data) {
  data.forEach(function (element) {
    let regiones = document.getElementById("regiones");
    let opt = document.createElement("option");
    opt.appendChild(document.createTextNode(element.nombre));
    opt.value = element.codigo;

    regiones.appendChild(opt);

  })
})

var url2 = "https://apis.digital.gob.cl/dpa/provincias";

fetch(url2).then(function (result) {
  if (result.ok) {
    return result.json();
  }

}).then(function (data) {
  data.forEach(function (element) {
    let regiones = document.getElementById("city");
    let opt = document.createElement("option");
    opt.appendChild(document.createTextNode(element.nombre));
    opt.value = element.codigo;

    regiones.appendChild(opt);

  })
})



fetch(url2).then(function (result) {
  if (result.ok) {
    return result.json();
  }

}).then(function (data) {
  data.forEach(function (element) {
    let regiones = document.getElementById("city");
    let opt = document.createElement("option");
    opt.appendChild(document.createTextNode(element.nombre));
    opt.value = element.codigo;

    regiones.appendChild(opt);

  })
})




/*validacion form*/
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')




const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo (NOSE OCUPA por ahora 0 preguntas plis ta de emergencia grasia.)
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{8,9}$/ // 7 a 14 numeros.
  
}
const campos = {
  nombre: false,
  ap1: false,
  numero: false,
  email: false,
  password: false,
}

const validarFormulario = (e) => {
  switch(e.target.name){
    case "nombre":
      validarCampo(expresiones.nombre, e.target, 'nombre');
    break;
      

    case "apellido1":
      validarCampo(expresiones.nombre, e.target, 'ap1');
    break;

    case "numero":
      validarCampo(expresiones.telefono, e.target, 'numero');
    break;

    case "email":
      validarCampo(expresiones.correo, e.target, 'email');
    break;

    case "con1":
      validarCampo(expresiones.password, e.target, 'password');
      validarPassword2();
    break;

    case "con2":
      validarPassword2();
    break;

  }

}

const validarCampo = (expresion, input, campo) => {
  if(expresion.test(input.value)){
    document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
    document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
    document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
    document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
    document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
    campos[campo] = true;
  
  } else {
    document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
    document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
    document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
    document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
    document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
    campos[campo] = false;
  }
}

const validarPassword2 = () => {
  const inputCon1 = document.getElementById('con1');
  const inputCon2 = document.getElementById('con2');

  if(inputCon1.value !== inputCon2.value){
    document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
    document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
    document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
    document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
    document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
    campos['password'] = false;
  } else {
    document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
    document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
    document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
    document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
    document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
    campos['password'] = true;
  }
}

inputs.forEach((input) => {
  input.addEventListener('keyup', validarFormulario);
  input.addEventListener('blur', validarFormulario);
});


formulario.addEventListener('submit', (e) => {
  e.preventDefault();


  const terminos = document.getElementById('terminos');
  if(campos.nombre && campos.ap1 && campos.ap2 && campos.numero && campos.email && campos.password && terminos.checked ){
    formulario.reset();

    document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
    setTimeout(() => {
      document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
    }, 5000)
    


    document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
      icono.classList.remove('formulario__grupo-correcto');
    })
  } else {
    document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
  }
});


/* 
function calcularEdad(fecha) {
  var hoy = new Date();
  var cumpleanos = new Date(fecha);
  var edad = hoy.getFullYear() - cumpleanos.getFullYear();
  var m = hoy.getMonth() - cumpleanos.getMonth();
  if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
      edad--;
  }
  return edad;
}

var edad = calcularEdad("date");
if(edad >= 18){
  document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
}else{
  alert("Eres menor de edad :( ");
}
*/