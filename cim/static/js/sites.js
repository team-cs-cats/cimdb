	$(document).ready(function(){
		$("#editSite").on("show.bs.modal", function(event){
	// Get the button that triggered the modal
	var button = $(event.relatedTarget);

	// Extract value from the custom data-* attribute
	var titleData = button.data("title");
	$(this).find(".modal-title").text(titleData);

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