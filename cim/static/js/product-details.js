console.log("I am  connected!")

function reload_product(){
  console.log("clicked")
  var sn=document.getElementById("product_sn_reload").value;
  
  var url='/product-details?'+'product_sn='+sn
  console.log("URL IS: ",url)
  
  window.location.href=url
};


// var d

// fetch('/data/product_catalog')
// .then(response => response.json())
// .then(data => {
//   console.log('Success:', data);
//   d=data
// })
// .catch((error) => {
//   console.error('Error:', error);
// });

// document.addEventListener('input', function (event) {

// 	// Only run on our select menu
// 	if (event.target.id !== 'family') return;

// 	// The selected value
// 	console.log(event.target.value);
//   console.log("HOYYYYYYY!!!!!!!!!!!!!!!!!")
//   var family=document.getElementById("family").value
//   console.log("selected: ",family)
//   var models = document.getElementById("models")
//   //clear options
//   models.innerHTML = ""
//   console.log("Data is: ",d)
//   var topmax = d[family].length
//   console.log("max is: ", topmax, " and values are: ",d[family])
//   // console.log("values are: ",d[family])
//   for (var i = 0; i < d[family].length; i++) {
//     var o = document.createElement("option");
//     o.value = d[family][i]
//     o.text = d[family][i]
//     models.appendChild(o);
// }



// 	// The selected option element
// 	console.log(event.target.options[event.target.selectedIndex]);

// }, false);


// // var select1 = document.getElementById("select1");
// // var select2 = document.getElementById("select2");
// // select1.onchange = function() {
// //     // empty select2
// //     while (select2.firstChild) {
// //         select2.removeChild(select2.firstChild);
// //     }
// //     if (select1.selectedIndex == 0) {
// //         return;
// //     }
// //     for (var i = select1.selectedIndex; i < select1.options.length; i++) {
// //         var o = document.createElement("option");
// //         o.value = select1.options[i].value;
// //         o.text = select1.options[i].text;
// //         select2.appendChild(o);
// //     }
// // }