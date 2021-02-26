console.log("I am  connected!")

function reload_product(){
  console.log("clicked")
  var sn=document.getElementById("product_sn_reload").value;
  
  // validate the SN via SQL
  valid=["P7125","P8766"]
  // if(valid.includes(sn))
  if(true){
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


//add new product
function get_cpu_sn(pn,method){

  console.log("pn is: ",pn)
  // product_pn=document.getElementById("product_pn").value.slice(-2)
  product_pn=pn.slice(-2)

        
  if(product_pn[0] !='i'){
    alert("Invalid SC Part Number!")
  }else{

    const data = {product_pn: this.product_pn,
                  method: method
                  };
    console.log("add a new product! data is ",data)

    fetch('/data/free_sn', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success! sn:', data);
      document.getElementById("product_sc_sn").value=data["sn"]
    })
    .catch((error) => {
      console.error('Error:', error);
    });

  }
  
}

function update_product_compoennets(product_sn){

  const product_data={
  sc_sn:this.product_sc_sn.value || this.product_sc_sn.placeholder ,
  MB:this.motherboard.value,
  Case:this.case.value,
  GC:this.gc.value,
  RAM:this.ram.value,
  RAM_quant:this.ram_quant.value || this.ram_quant.placeholder ,
  HDD:this.hdd.value,
  HDD_quant:this.hdd_quant.value || this.hdd_quant.placeholder,
  product_sn:product_sn
  }

  console.log("data is: ",product_data)

  if (product_data["product_sn"]==""){
    alert("Invalid Product Sn! Refresh the page with Valid Product SN")
  }else{
    fetch('/data/product_components_exist', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(product_data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success! compoennets exist:', data);
      // if product compoennets exists: update otherwise: add
      if(data.result==false){
        add_compoenents(product_data)
      }else{
        alert("Update is not impelemented yet!")
      }
      
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }

}

function add_compoenents(input_data){

  console.log("adding new componets with the data: ",input_data)
  fetch('/product-details', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(input_data),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success! compoennets exist:', data);
    location.reload()
  })
  .catch((error) => {
    console.error('Error:', error);
  });



}

// function update_compoenents(){

// }