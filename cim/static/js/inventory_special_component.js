
$(document).ready(function(){

	$("#editSpecialComponent").on("show.bs.modal", function(event){
	// Get the button that triggered the modal
	var button = $(event.relatedTarget);

	// Extract value from the custom data-* attribute
	var titleData = button.data("title");
	$(this).find(".modal-title").text(titleData);

	var partNumberData = button.data("spec-comp-part-number");
	$(this).find("#spec-comp-edit-part-number").val(partNumberData);

	var specCompLocationData = button.data("spec-comp-edit-location");        
	$(this).find("#spec-comp-edit-location").val(specCompLocationData);

	// var siteNameData = button.data("spec-comp-site-name");        
	// $(this).find("#spec-comp-edit-site").val(siteNameData);

	// var roomNumberData = parseInt(button.data("spec-comp-room-number"));
	// $(this).find("#spec-comp-edit-room-number").val(roomNumberData);

	// var shelfNumberData = parseInt(button.data("spec-comp-shelf-number"));
	// $(this).find("#spec-comp-edit-shelf-number").val(shelfNumberData);

	// Referenced this StackOverflow discussion to determine how to adject the checked property using jquery
	// https://stackoverflow.com/questions/426258/setting-checked-for-a-checkbox-with-jquery/426276#426276 
	var specialComponentIsFreeData = button.data("spec-comp-is-free");        
	$(this).find("#spec-comp-edit-is-free").prop('checked', specialComponentIsFreeData);

	});

});