console.log("JS functions are connected!")



//get component information details
function products_info(workorder_number){
  console.log("clicked")
 // validate the workorder via SQL
valid=["879845","815348"]
if(valid.includes(workorder_number)){
    var url='/wo-details?'+'wo_id='+workorder_number
    console.log("URL IS: ",url)
    
    window.location.href=url
}else{
  alert('only "879845" and "815348" are implemented for demo')
}



};

//edit workorder information 
function edit_workorder_info(workorder_number){
  console.log("clicked")
  alert("Workorder: "+workorder_number+" will be editted later!")
};

//delete workorder 
function delete_workorder(workorder_number){
  console.log("clicked")
  alert("Workorder: "+workorder_number+" will be DELETED later!")
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

