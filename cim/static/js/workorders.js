
console.log("JS functions are connected!")



//get component information details
function products_info(workorder_number){
  console.log("clicked")
 // validate the workorder via SQL

if(true){
    var url='/wo-details?'+'wo_id='+workorder_number
    console.log("URL IS: ",url)
    
    window.location.href=url
}else{
  alert('only "879845" and "815348" are implemented for demo')
}



};

//edit workorder information 
function edit_workorder_info(){
  
  const data={
    wo_id: this.wo_id_to_edit.value,
    wo_open_date: this.wo_open_date_to_edit.value,
    wo_close_date: this.wo_close_date_to_edit.value,
    wo_status: this.wo_status_to_edit.value,
    wo_reference_number: this.wo_refrence_number_to_edit.value,
    wo_employee_name: this.wo_employee_to_edit.value
  }
  console.log("edit clicked",data)

  // make an Update request to server
  fetch('/workorders', {
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

//delete workorder 
function delete_workorder_info(workorder_number){
  console.log("clicked")
  const data={
    wo_id: this.delete_WorkOrder_title.innerText,
  }
  console.log("delete clicked",data)

  //make a Delete request to server
  fetch('/workorders', {
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


//add a new work order
function add_new_workorder(){
  employee_id=this.wo_employee_name_assign.value
  reference_number=this.wo_reference_number_assign.value
  date=this.wo_open_date_assign.value
  console.log("a new work order for ",employee_id," created on ",date," and ref number is: ",reference_number)

  const data = { id: employee_id, reference:reference_number, date:date , req:"add"};
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
    location.reload()
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}




$(document).ready(function() {
  $('#editWorkOrder').on('shown.bs.modal', function (event) {
    	// Get the button that triggered the modal
		var button = $(event.relatedTarget);

    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("editWorkOrder-title").innerText=button.attr("data-wo-id")
    document.getElementById("wo_id_to_edit").value=button.attr("data-wo-id")
    document.getElementById("wo_open_date_to_edit").value=button.attr("data-wo-open-date")
    document.getElementById("wo_close_date_to_edit").value=button.attr("data-wo-close-date")
    document.getElementById("wo_status_to_edit").value=button.attr("data-wo-status")
    document.getElementById("wo_refrence_number_to_edit").value=button.attr("data-wo-refrence-number")
    document.getElementById("wo_employee_to_edit").value=button.attr("data-wo-employee-full-name")
   		
	});
    
});


$(document).ready(function() {
  $('#deleteWorkOrder').on('shown.bs.modal', function (event) {
    	// Get the button that triggered the modal
		var button = $(event.relatedTarget);

    //Extract value from the custom data-* attribute and update modal attr
    document.getElementById("delete_WorkOrder_title").innerText=button.attr("data-wo-id")
       		
	});
    
});



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
  else if(filter_key=="wo_refrence_number"){
    number_input(filter_key)
    return

  }else if(filter_key=="wo_employee_id"){
    employee_filter_input(filter_key)
    return

  }else if(filter_key=="wo_status"){
    status_filter_input(filter_key)
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

//status input
function status_filter_input(name){

   
  fetch('/data/wo_status_cataloge')
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
  
  var form=document.getElementById("filter-value")
  var input=document.createElement("select")

  input.setAttribute("id",name)

  for( var status of data){
    var o = document.createElement("option");
    o.value = status['value']
    o.text = status['value']
    input.appendChild(o);
  }

  form.appendChild(input)
  
})
.catch((error) => {
  console.error('Error:', error);
});
}


//employee input
function employee_filter_input(name){

   
  fetch('/data/list_of_employees')
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
  
  var form=document.getElementById("filter-value")
  var input=document.createElement("select")

  input.setAttribute("id",name)

  for( var employee of data){
    var o = document.createElement("option");
    o.value = employee
    o.text = employee
    input.appendChild(o);
  }

  form.appendChild(input)
  
})
.catch((error) => {
  console.error('Error:', error);
});
}

// sql problem in back end

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
//     location.reload()
//   })
//   .catch((error) => {
//     location.reload();
//   });
// }

$(document).ready(function(){
  $("#filterBtn").on("click", function() {
  	console.log('clicked!');
    var filter_key=$("#filter-key").val().toLowerCase();
    var filter_value=$("#"+filter_key).val().toLowerCase();
    console.log("key and values are: ",filter_key,filter_value)
    $("#wo-results tr").filter(function() {
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

