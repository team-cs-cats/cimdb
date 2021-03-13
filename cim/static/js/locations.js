


// open locations edit modal popup
$(document).ready(function(){
	$("#editLocation").on("show.bs.modal", function(event){
		// Get the button that triggered the modal
		var button = $(event.relatedTarget);

		// Extract value from the custom data-* attribute
		var titleData = button.data("title");
		$(this).find(".modal-title").text(titleData);

		var roomNumberData = parseInt(button.data("location-room-number"));
		$(this).find("#room-number").val(roomNumberData);

		var shelfNumberData = parseInt(button.data("location-shelf-number"));
		$(this).find("#shelf-number").val(shelfNumberData);

		var siteNameData = parseInt(button.data("site-id"));        
		$(this).find("#location-site").val(siteNameData); 

		var locationIdData = button.data("location-id");    
		$(this).find("#location-id-to-edit").val(locationIdData);
	});
});



// open locations DELETE modal popup
$(document).ready(function(){
	$("#deleteLocation").on("show.bs.modal", function(event){
		// Get the button that triggered the modal
		var button = $(event.relatedTarget);

		// Extract value from the custom data-* attribute
		var titleData = button.data("title");
		$(this).find(".modal-title").text(titleData);

		var roomNumberData = parseInt(button.data("location-room-number"));
		$(this).find("#room-number").val(roomNumberData);

		var shelfNumberData = parseInt(button.data("location-shelf-number"));
		$(this).find("#shelf-number").val(shelfNumberData);

		var siteNameData = parseInt(button.data("site-id"));        
		$(this).find("#location-site").val(siteNameData); 

		var locationIdData = button.data("location-id");    
		$(this).find("#location-id-to-delete").val(locationIdData);
	});
});


//add a new location
function add_new_location(){

	// create a new data constant that packages this collected information
	const data = {

		// Pull the selected site id, new room number and new shelf number from the add new location form 
		add_new_location_site : this.add_new_location_site.value, 
		add_location_room_number : this.add_location_room_number.value, 
		add_location_shelf_number : this.add_location_shelf_number.value 
	};

	// load the locations page
	fetch('/locations', 

		// load a POST request by sending the packaged data in the body of the request
		{
		method: 'POST',
		headers: {
		'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
		})

	// Then, save the POST response and reload the page
	.then(response => response.json())
	.then(data => {
		console.log('Success:', data);
		location.reload()
	})

	// If there are any loading errors, log to console
	.catch((error) => {
		console.error('Error:', error);
	});
}


// Live Search Filter
$(document).ready(function(){
  $("#filterLocationSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#locationResults tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});