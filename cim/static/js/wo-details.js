console.log("I am  connected!")


// Open another wo using the wo_id
//reloads the page
function reload_workorder(){
  console.log("clicked")
  var wo=document.getElementById("wo_id_reload").value;
  
  var url='/wo-details?'+'wo_id='+wo
  console.log("URL IS: ",url)
  
  window.location.href=url
};


var d

fetch('/data/product_catalog')
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
  d=data
})
.catch((error) => {
  console.error('Error:', error);
});

document.addEventListener('input', function (event) {

    // Only run on our select menu
	if (event.target.id !== 'product_family') return;

	// The selected value
	console.log(event.target.value);
    var family=document.getElementById("product_family").value
    console.log("selected: ",family)
    var models = document.getElementById("product_pn")
    //clear options
    models.innerHTML = ""
    console.log("Data is: ",d)
    var topmax = d[family].length
    console.log("max is: ", topmax, " and values are: ",d[family])
    // console.log("values are: ",d[family])
    for (var i = 0; i < d[family].length; i++) {
        var o = document.createElement("option");
        o.value = d[family][i]
        o.text = d[family][i]
        models.appendChild(o);
}

	// The selected option element
	console.log(event.target.options[event.target.selectedIndex]);

}, false)


