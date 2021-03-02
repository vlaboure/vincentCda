const stars = document.querySelectorAll('.star');
const labLangage = document.getElementById('select');
const language = document.getElementById('langage');
const societe = document.getElementById('societe');
const personne = document.getElementById('personne');
const cp = document.getElementById('cp');
const email = document.getElementById('email');
const cancel = document.getElementById('cancel');

checkEnter = function (e) {
  if (e.id === 'societe' || e.id === 'personne') {
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
  }
};

societe.addEventListener('focusout', (e) => {
  checkEnter(societe);
});

personne.addEventListener('focusout', (e) => {
  checkEnter(personne);
});

cp.addEventListener('focusout', (e) => {
  checkEnter(cp);
});

email.addEventListener('focusout', (e) => {
  checkEnter(email);
});

labLangage.addEventListener('change', (e) => {
  if (labLangage.selectedIndex > 0) {
    langage.value += labLangage.options[labLangage.selectedIndex].value + '\n';
  }
});

stars.forEach((element) => {
  element.innerHTML = '*';
});
 
// cancel.addEventListener('click', (e) => {
//   e.preventDefault();
  
// })