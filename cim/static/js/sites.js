	
// Edit Site Details modal
$(document).ready(function(){

	$("#editSite").on("show.bs.modal", function(event){

		// Get the button that triggered the modal
		var button = $(event.relatedTarget);

		// Extract value from the custom data-* attribute
		var titleData = button.data("title");
		$(this).find(".modal-title").text(titleData);

		var siteIDData = button.data("site-id-to-edit");
		$(this).find("#site-id-to-edit").val(siteIDData);

		var siteAddress1Data = button.data("site-address-1");
		$(this).find("#site-edit-address-1").val(siteAddress1Data);

		var siteAddress2Data = button.data("site-address-2");        
		$(this).find("#site-edit-address-2").val(siteAddress2Data);

		var siteCityData = button.data("site-address-city");
		$(this).find("#site-edit-city").val(siteCityData);

		var siteStateData = button.data("site-address-state");
		$(this).find("#site-edit-state").val(siteStateData);

		var siteZipData = button.data("site-address-postal-code");        
		$(this).find("#site-edit-zip").val(siteZipData);

	});

});


// Delete Site Modal
$(document).ready(function(){

	$("#deleteSite").on("show.bs.modal", function(event){

		// Get the button that triggered the modal
		var button = $(event.relatedTarget);

		// Extract value from the custom data-* attribute
		var titleData = button.data("title");
		$(this).find(".modal-title").text(titleData);

		var siteIDData = button.data("site-id-to-delete");
		$(this).find("#site-id-to-delete").val(siteIDData);

		var siteCityData = button.data("site-address-city");
		$(this).find("#site-delete-city").html(siteCityData);

	});

});


// Live Search Filter
$(document).ready(function(){
  $("#filterSiteSearch").on("keyup", function() {
  	console.log('got it');
    var value = $(this).val().toLowerCase();
    $("#siteResults tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});