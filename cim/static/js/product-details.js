console.log("I am  connected!")

function reload_product(){
  console.log("clicked")
  var sn=document.getElementById("product_sn_reload").value;
  
  // validate the SN via SQL
  valid=["P7125","P8766"]
  if(valid.includes(sn)){
    console.log("valid sn")
    var url='/product-details?'+'product_sn='+sn
    console.log("URL IS: ",url)
    
    window.location.href=url
  }else{
    alert("wrong sn!")
  }
    
};


function go_back() {
  window.history.back();
}
