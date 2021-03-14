// Exercice 1 :
// rescencement de la population
const rescencement = function(){
    //init
    let enfants=jAdultes=sAdultes=centenaires = 0;
    const ageMin = 20;
    const ageMax = 40;
    
    let age = 0;
    //boucle d'entree
    while (true){
        age = window.prompt('entrez votre age :');
        if(age <=0){
            window.alert('Entrez une valeur supperrieure à 0 !!');
            age = window.prompt('entrez votre age :');
        }
        if (age >= 100){
            centenaires++;
            break;
        }else if(age > 40){
            sAdultes++;
        }else if (age < 40 && age >= 20){
            jAdultes++;
        }else
            enfants++;
    };
    //affichage
    window.alert(`la population se répartit ainsi : centenaires :${centenaires}
    Adultes de plus de 40 ans : ${sAdultes}
    Adultes entre 20 et 40 ans : ${jAdultes}
    Enfants et adolescents : ${enfants}`)
}

                // Appel de la fonction
 //rescencement()

//********************************************************** */
// Exercice 2 table de multiplication

const tableMultiplication = function(n){
    const arr = [];

    for(let i = 1; i< 10; i++){
        res = (n * i);
        arr.push(res);
        console.log(`${i} fois ${n} donne : ${res}`)
    }
    //affichage mais on pourrait retourner le tableau
    window.alert(`cette donnée sera disponible dans ce tableau en retour de la fonction: ${arr}`);
    return arr;        
}
                // Appel de la fonction
// let n = 0
// while(n <= 0){
//     n = window.prompt('quelle table voulez vous (valeur supperieure à 0 !)')
// }
// const table = tableMultiplication(n);

//*********************************************** */

// Exercice 3 recherche de prénom
const memoire = function(){
    const tab = ["Audrey", "Aurélien", "Flavien", "Jérémy", "Laurent", "Melik", "Nouara", "Salem", "Samuel", "Stéphane"];
    window.alert(`Attention le tableau initial n'est affiché que 3 secondes:\n${tab}`);
    const initNom = window.prompt('qui cherchez vous ?');
    // on met la première lettre en majuscule charAt(0)premièr car slice supprime le premier car de initNom
    const nom = initNom.charAt(0).toUpperCase() + initNom.slice(1)
    // fonction qui renvoie l'index de l'item qui matche avec le nom donné
    const index = tab.findIndex(ind => ind === nom)
    if(index > -1){
        // si trouvé (>-1) on supprime et insére un vide en fin de tableau
        tab.splice(index,1);
        tab.push('');
    }
    console.log(tab) 
}

//memoire();

//****************************************************** */

// Exercice 4
// calcul de commande avec remise et frais de port
const commande = function(){
    const remise = port = pap = 0;
    const free = 500;
    const rem1 = .95;
    const rem2 = .9;
    const percentPort = .02;
    const portMin = 6;
    
    const pu = window.prompt('Entrez le prix de l\'article : '); 
    const qte = window.prompt('Entrez la qantité : ')
    //prix tot sans remises ni frais de port
    let pxtot = pu * qte
    
    // si tot < 100 pas de remise
    // sinon si 100<=tot<200 5%remise
    // sinon 10%remise
    pap = pxtot < 100 ? pxtot : (pxtot >= 100 && pxtot <= 200 ? pxtot * rem1 : pxtot * rem2);
    
    // si tot-remise > 500 port = 0
    // sinon si (tot-remise)*2% < 6 port = 6€ sinon (tot-remise)*2%
    //port min = 6€
    port = pap > free ? 0 : (pap * percentPort < portMin ? portMin : pap * percentPort);
    pap += port;
    console.log(`Le prix total est de : ${pap.toFixed(2)}`);    
}
//appel fonction
commande();