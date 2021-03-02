// // calcul de 30 moyennes
// // méthode de création du tableau de tableau
// const creatArr = function () {
//   let arr = [];
//   for (let i = 0; i < 3; i++) {
//     let tp = Math.round(Math.random(i) * 20);
//     arr.push(tp);
//   }
//   return arr;
// };

// // insertion des notes des 30 éléves
// const array = [];
// for (let i = 0; i < 30; i++) {
//   array.push(creatArr());
// }

// // calcule des moyenne et insertion dans un tableau de moyennes
// const calcMoy = (array) => {
//   const moy = [];
//   array.forEach((element) => {
//     let tot = 0;
//     element.forEach((el) => {
//       tot = tot + el;
//     });
//     moy.push(Math.round(tot / element.length));
//   });
//   return moy;
// };

// // affichage
// const moyenne = calcMoy(array);
// moyenne.forEach((m, i) =>
//   console.log(`la moyenne de l'étudiant ${i + 1} est de ${m} `)
// );
// // -------------------tri insertion
// const t = [];
// let i=0;
// let min = 0;
// while(i < 4){
//     let nom = window.prompt(`Entrez un chiffre ${i + 1} `);
//     t.push(nom);
//     i++;
// }

// // for(let i = 1; i<t.length; i++){
// //     let init = t[i];
// //     for(j = i;j > 0 && t[j -1]> init ; j--){
// //         t[j] = t[j - 1];
// //     }
// //     t[j] = init;
// // };
// // console.log(t);

// //-------------
// // tri bulles
// // let permut = true;
// // while(permut){
// //     permut = false;
// //     let tp;
// //     for (let i = 0; i< t.length - 1; i++){
// //         if (t[i] > t[i + 1]){
// //             permut = true;
// //             tp = t[i];
// //             t[i] = t[i + 1];
// //             t[i + 1] = tp;
// //         }
// //     }    
// // }
// // console.log(t);

// // tri recursif
// const recursif = function(tab){
//     const ind_pivot = Math.floor(Math.random() * (tab.length -1));
//     let pivotN = tab[ind_pivot];
//     let inf = [];
//     let sup = [];
//     let pivot = [];
//     if (tab.length < 2) return tab
//     tab.forEach((el) =>{
//         if(el < pivotN)
//             inf.push(el);
//         else if (el > pivotN)
//             sup.push(el);
//         else
//             pivot.push(el);
//     })
//     return recursif(inf) + pivot + recursif(sup)
// }
// let rec = recursif(t).slice();
// console.log(rec);
// /*  #region 

// //---------------------algo tiercé   

// let x, y; 
// let  factP = 1;

// const nbChevauxPartants = window.prompt('partants ?')
// const nbChevauxjoués = window.prompt('joués ?')
// //chevaux partant
// const fact  = function(num){
//     let factp = 1;
//     if (num === 1) return 1;
//     for(let i = 1; i <= num; i++){
//         factp = (i) * factp;
//     }
//     return factp;
// }
// //chances de gagner dans l'ordre
// x = Math.round(fact(Number(nbChevauxPartants)) / fact((nbChevauxPartants - nbChevauxjoués)));
// console.log(`Vous avez une chance sur ${x} de gagner dans l'ordre en jouant ${nbChevauxjoués}` );
// //chance de gagner dans le désordre
// y = Math.round(fact(Number(nbChevauxPartants)) / (fact(Number(nbChevauxjoués)) * fact(Number(nbChevauxPartants - nbChevauxjoués))));
// console.log(`Vous avez une chance sur ${y} de gagner dans le désordre en jouant ${nbChevauxjoués}` );

//         //#endregion
// */

// const fact  = function(num){
//     if ((num) === 0) return 1;
//     return  num * fact(num - 1) ;
// }
// console.log(`la factorielle de 5 est : ${fact(5)}`);


// // let max = 0;
// // for(let i = 1; i<=5; i++){
// //     let nb = window.prompt('entrez 20 nombres');
// //     if(nb > max) max = nb;   
// // }
// // alert(`le plus grand nombre est ${max}`) ;

// let t2 = [[1,2,5,6],[25,4,8,4],[12,9,33,4]];
// for(let i = 0;i < t2.length; i++){
//     for (let j = 0; j< 3; j++){
//         console.log(t2[j]);
//     }
// }
const img = 'images/papillon.jpg';
const calcProduit = function(x,y){
  return x * y
}

const affichImage = function(image){
  const n = window.prompt('entrez un nombre') 
  const p = window.prompt('entrez un multiplicateur');
  let el = document.querySelector('.visible');
  const res = calcProduit(n, p)
  el.innerHTML=`<div><img src=${image} alt='papillon'></div>
  <div>le produit de ${n} par ${p} est</div><div width="20px"> ${res} <div/>`
  console.log(calcProduit(n,p))
}

affichImage(img)