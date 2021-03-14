//get component information details
function components_info(serial_number){
  console.log("clicked")
    
  var url='/product-details?'+'product_sn='+serial_number
  console.log("URL IS: ",url)
  
  window.location.href=url

}


// Edit product Modal
$(document).ready(function() {
  $('#pass_assembly').on('shown.bs.modal', function (event) {
    	
    // Get the button that triggered the modal
		var button = $(event.relatedTarget);
    
    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("pass_assembly_title").innerText=button.attr("data_product_sn")
});
});


$(document).ready(function() {
  $('#failed_assembly').on('shown.bs.modal', function (event) {
    	
    // Get the button that triggered the modal
		var button = $(event.relatedTarget);
    
    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("failed_assembly_title").innerText=button.attr("data_product_sn")
});
});


function assembly_approval(){
  var product_sn=this.pass_assembly_title.innerHTML
  var product_date_assembly=this.assembly_approval_date.value

  if(product_date_assembly === ""){
    alert("Select Assembly approval date")
    return
  }
  else{
    // console.log(product_sn,"  ",product_date_assembly)
    const data={
      product_sn: product_sn,      
      product_date_assembly: product_date_assembly
    }
    
  
    // make an Update request to server
    fetch('/assembly', {
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
  

// function filter(){
//   var filter_key=document.getElementById("filter-key").value
//   var filter_value=document.getElementById(filter_key).value
//   console.log("key and values are: ",filter_key)

//   const data = { filter_key: filter_key, filter_value:filter_value, req:"filter" };
//   console.log(data)

//   fetch('/workorders', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(data),
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log('Success:', data);
//     // location.reload()
//   })
//   .catch((error) => {
//     console.error('Error:', error);
//   });
// }

$(document).ready(function(){
  $("#filterBtn").on("click", function() {
  	console.log('clicked!');
    var filter_key=$("#filter-key").val().toLowerCase();
    var filter_value=$("#"+filter_key).val().toLowerCase();
    console.log("key and values are: ",filter_key,filter_value)
    $("#assembly-results tr").filter(function() {
      if($(this).attr('id')!='table-head'){
        // $(this).css("background-color", "#000000");
        $(this).toggle($(this).text().toLowerCase().indexOf(filter_value) > -1)
       }    
    });
  });
});

$(document).ready(function(){
  $("#filterClearBtn").on("click", function() {
    location.reload()  	
  });
});