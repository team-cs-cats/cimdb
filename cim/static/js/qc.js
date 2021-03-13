console.log("I am  connected!")

  

//get component information details
function components_info(serial_number){
  console.log("clicked")
    
  valid=["P7125","P8766"]
if(true){
  var url='/product-details?'+'product_sn='+serial_number
  console.log("URL IS: ",url)
  
  window.location.href=url
}else{
  alert('only "P7125" and"P8766" are implemented for demo')

};

}

//assembel product information 
function qc_product(serial_number){
  console.log("clicked")
  alert("Product: "+serial_number+" will be QC'ed later!")
};

//report product details
function report_product(serial_number){
  console.log("clicked")
  alert("Product: "+serial_number+" will be REPORTED later!")
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

// Edit product Modal
$(document).ready(function() {
  $('#pass_qc').on('shown.bs.modal', function (event) {
    	
    // Get the button that triggered the modal
		var button = $(event.relatedTarget);
    
    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("pass_qc_title").innerText=button.attr("data_product_sn")
});
});


$(document).ready(function() {
  $('#failed_qc').on('shown.bs.modal', function (event) {
    	
    // Get the button that triggered the modal
		var button = $(event.relatedTarget);
    
    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("failed_qc_title").innerText=button.attr("data_product_sn")
});
});

function qc_approval(){
  var product_sn=this.pass_qc_title.innerHTML
  var product_qc_date=this.qc_approval_date.value

  if(product_qc_date === ""){
    alert("Select QC approval date")
    return
  }
  else{
    // console.log(product_sn,"  ",product_qc_date)
    const data={
      product_sn: product_sn,      
      product_qc_date: product_qc_date
    }
    
  
    // make an Update request to server
    fetch('/qc', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      location.reload()
    })
    .catch((error) => {
      console.error('Error:', error);
    });


  }
}



//Dynamic Filter


//event listener for edit Modal
document.addEventListener('input', function (event) {

  // Only run on our select menu
if (event.target.id !== 'filter-key') return;

generate_filter_value_input()

}, false)

function update_pn_in_edit_modal(){

  // The selected value
  
  var family=document.getElementById("product_family_to_edit").value

  var models = document.getElementById("product_pn_to_edit")
  //clear options
  models.innerHTML = ""

  //add new options
  for (var i = 0; i < d[family].length; i++) {
      var o = document.createElement("option");
      // o.value = d[family][i]
      o.text = d[family][i]
      models.appendChild(o);
  }
  
}

//generate_filter_value_input()
function generate_filter_value_input(){

  var filter_key=document.getElementById("filter-key").value
 
  //remove other value inputs
  const parent = document.getElementById("filter-value")
  while (parent.firstChild) {
    parent.firstChild.remove()
}
  //create new input labels based on the filter key

  if(filter_key=="wo_id"){
    number_input(filter_key)
    return

  }else if(filter_key=="wo_open_date"){
    date_input(filter_key)
    return

  }
  else if(filter_key=="wo_close_date"){
    date_input(filter_key)
    return
  }
  else if(filter_key=="product_sn"){
    number_input(filter_key)
    return

  }else if(filter_key=="product_family"){
    prduct_family_filter_input(filter_key)
    return

  }else if(filter_key=="product_pn"){
    product_pn_filter_input(filter_key)
    return

  }else if(filter_key=="product_assembly_date"){
    date_input(filter_key)
    return
  }
   
}

//Date input
function date_input(name){
  var form=document.getElementById("filter-value")
  var input=document.createElement("input")

  input.setAttribute("type","date")
  input.setAttribute("id",name)

  form.appendChild(input)
    
}

//number input
function number_input(name){
  var form=document.getElementById("filter-value")
  var input=document.createElement("input")

  input.setAttribute("type","number")
  input.setAttribute("id",name)

  form.appendChild(input)
    
}

//product family input
function prduct_family_filter_input(name){

   
  fetch('/data/product_catalog')
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
  
  var form=document.getElementById("filter-value")
  var input=document.createElement("select")

  input.setAttribute("id",name)

  const prodcut_family=Object.keys(data)

  for( var family of prodcut_family){
    var o = document.createElement("option");
    o.value = family
    o.text = family
    input.appendChild(o);
  }

  form.appendChild(input)
  
})
.catch((error) => {
  console.error('Error:', error);
});
}


//product pn input
function product_pn_filter_input(name){

    
  fetch('/data/product_catalog')
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    
    var form=document.getElementById("filter-value")
    var input=document.createElement("select")
  
    input.setAttribute("id",name)
  
    const product_pn=Object.values(data)
  
    for( var family of product_pn){
      for( var pn of family){
        var o = document.createElement("option");
        o.value = pn
        o.text = pn
        input.appendChild(o);
        }
    }
  
    form.appendChild(input)
    
  })
  .catch((error) => {
    console.error('Error:', error);
  });
  }
  

function filter(){
  var filter_key=document.getElementById("filter-key").value
  var filter_value=document.getElementById(filter_key).value
  console.log("key and values are: ",filter_key)

  const data = { filter_key: filter_key, filter_value:filter_value, req:"filter" };
  console.log(data)

  fetch('/workorders', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    // location.reload()
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}

// $(document).ready(function(){
//   $("#filterBtn").on("click", function() {
//   	console.log('clicked!');
//     var filter_key=$("#filter-key").val()
//     var filter_value=$("#"+filter_key).val()
//     console.log("key and values are: ",filter_key,filter_value)
//     $("#wo-results tr").filter(function() {
//       $(this).toggle($(this).text().toLowerCase().indexOf(filter_key) > -1)
//     });
//   });
// });