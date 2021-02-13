console.log("I am  connected!")



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



