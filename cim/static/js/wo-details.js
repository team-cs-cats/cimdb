console.log("JS functions are connected!")

function go_back() {
  window.history.back();
}

// Open another wo using the wo_id
//reloads the page
function reload_workorder(){
  
  var wo=document.getElementById("wo_id_reload").value;
  
  valid=["879845","815348"]
  if(true){
      
    var url='/wo-details?'+'wo_id='+wo
        
    window.location.href=url
  }else{
  alert('only "879845" and "815348" are implemented for demo')
}
}




  

//get component information details
function components_info(serial_number){
      
  valid=["P7125","P8766"]
if(true){
  var url='/product-details?'+'product_sn='+serial_number
    
  window.location.href=url
}else{
  alert('only "P7125" and"P8766" are implemented for demo')

};

}

//edit product information 
function edit_product_info(serial_number){
  console.log("clicked")
  alert("Product: "+serial_number+" will be editted later!")
};

//delete product details
function delete_product(serial_number){
  console.log("clicked")
  alert("Product: "+serial_number+" will be DELETED later!")
};


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
    // console.log("selected: ",family)
    var models = document.getElementById("product_pn")
    //clear options
    models.innerHTML = ""
    // console.log("Data is: ",d)
    var topmax = d[family].length
    // console.log("max is: ", topmax, " and values are: ",d[family])
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


//add new product
function add_new_product(wo_id,employee_id){

  sc_pn=this.product_pn.value.slice(-2)
  console.log("sc.slice(0) is ",sc_pn.slice(0))
    
  if(wo_id===undefined || sc_pn[0] !='i'){
    alert("unvalid work order ID! or select correct product family")
  }else{

    const data = {product_pn: this.product_pn.value,
                  product_family:this.product_pn.value,
                  wo_id:wo_id,
                  employee_id:employee_id,
                  sc_pn:sc_pn
                 };
    console.log("add a new product! data is ",data)

    fetch('/wo-details', {
      method: 'POST',
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



// edit product details
function edit_workorder_details(){
  const data={
    product_sn: this.product_sn_to_edit.value,
    product_pn: this.product_pn_to_edit.value,
    product_family: this.product_family_to_edit.value,
    product_date_assembly: this.product_assembly_date_to_edit.value,
    product_qc_date: this.product_qc_date_to_edit.value,
    product_warranty_expiration_date: this.product_warranty_date_to_edit.value,
    product_location_id: this.product_location_to_edit.value
  }
  console.log("edit clicked",data)

  // make an Update request to server
  fetch('/wo-details', {
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
  
};


// delete product details
function delete_workorder_details(){
  const data={
    product_sn: this.delete_WorkOrderDetails_title.innerText,
  }
  console.log("delete clicked",data)

  // make an Update request to server
  fetch('/wo-details', {
    method: 'DELETE',
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
  
};


// Edit product Modal
$(document).ready(function() {
  $('#editWorkOrderDetails').on('shown.bs.modal', function (event) {
    	
    // Get the button that triggered the modal
		var button = $(event.relatedTarget);
    
    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("edit_WorkOrderDetails_title").innerText=button.attr("data-product-sn")
    document.getElementById("product_family_to_edit").value=button.attr("data-product_family")
    document.getElementById("product_pn_to_edit").value=button.attr("data-product_pn")
    document.getElementById("product_sn_to_edit").value=button.attr("data-product-sn")
    document.getElementById("product_assembly_date_to_edit").value=button.attr("data-product_date_assembly")
    document.getElementById("product_qc_date_to_edit").value=button.attr("data-product_qc_date")
    document.getElementById("product_warranty_date_to_edit").value=button.attr("data-product_warranty_expiration_date")
    document.getElementById("product_location_to_edit").value=button.attr("data-product_location_id")  
	});   
});

// Delete product Modal
$(document).ready(function() {
  $('#deleteWorkOrderDetails').on('shown.bs.modal', function (event) {
    	// Get the button that triggered the modal
		var button = $(event.relatedTarget);

    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("delete_WorkOrderDetails_title").innerText=button.attr("data-product_sn")
       		
	});
    
});

//event listener for edit Modal
document.addEventListener('input', function (event) {

  // Only run on our select menu
if (event.target.id !== 'product_family_to_edit') return;

update_pn_in_edit_modal()

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

