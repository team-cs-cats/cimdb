
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

  //make an Update request to server
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
    // location.reload()
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
    // location.reload()
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

  const data = { id: employee_id, reference:reference_number, date:date };
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