const stars = document.querySelectorAll('.star');
const objMessage = document.getElementById('select');
const demande = document.getElementById('demande');
const societe = document.getElementById('nom');
const personne = document.getElementById('prenom');
const cp = document.getElementById('cp');
const email = document.getElementById('email');
const cancel = document.getElementById('cancel');
const send = document.getElementById('send');
const conditions = document.getElementById('conditions');

//  fonction appelée par tous le controles 
checkEnter = function (e) {
  if (e.id === 'nom' || e.id === 'prenom' || e.id === 'date') {
    if (e.value.length < 1) {
      alert('vous devez saisir au moins un caractère');
      e.focus();
    }
  } else if (e.id === 'cp') {
    if (isNaN(parseInt(e.value, 10))) {
      alert('vous devez saisir une valeur numérique');
      e.focus();
    } else if (e.value.length < 5) {
      alert('vous devez saisir au moins 5 caractères');
      e.focus();
    }
  } else if (e.id === 'email') {
    if (e.value.indexOf('@') === -1) {
      alert('vous devez saisir une adresse mail valide');
      e.focus();
    }
  }else if (e.id === 'conditions'){
    if(demande.value.trim().length < 1){
      alert('vous devez saisir une demande');
      e.checked = false;
      e.focus();
    }
  } 
};

nom.addEventListener('focusout', (e) => {
  checkEnter(nom);
});

prenom.addEventListener('focusout', (e) => {
  checkEnter(prenom);
});

cp.addEventListener('focusout', (e) => {
  checkEnter(cp);
});

email.addEventListener('focusout', (e) => {
  checkEnter(email);
});

objMessage.addEventListener('blur', (e) => {
 // debugger;
  console.log(objMessage.selectedIndex);
  if (objMessage.selectedIndex === 0) {
    window.alert('vous devez choisir une option !')
    objMessage.focus();
  }
});
conditions.addEventListener('click', (e) =>{
  if(e.target.checked)
    checkEnter(conditions);
});

send.addEventListener('click', (e) => {
  if(!conditions.checked){
    e.preventDefault();
    window.alert('vous devez accepter les conditions d\'utilisation');
    conditions.focus();
  }
})
 
// cancel.addEventListener('click', (e) => {
//   e.preventDefault();
  
// })