

// jQuery function for populating the Edit Special Component modal
$(document).ready(function(){

	$("#editSpecialComponent").on("show.bs.modal", function(event){
	// Get the button that triggered the modal
	var button = $(event.relatedTarget);

	// Extract value from the custom data-* attribute
	var titleData = button.data("title");
	$(this).find(".modal-title").text(titleData);

	var specCompSnData = button.data("spec-comp-serial-number");
	$(this).find("#spec-comp-serial-number").val(specCompSnData);

	var partNumberData = button.data("spec-comp-part-number");
	$(this).find("#spec-comp-edit-part-number").val(partNumberData);

	var specCompLocationData = button.data("spec-comp-edit-location");        
	$(this).find("#spec-comp-edit-location").val(specCompLocationData);
	
	// Referenced this StackOverflow discussion to determine how to adject the checked property using jquery
	// https://stackoverflow.com/questions/426258/setting-checked-for-a-checkbox-with-jquery/426276#426276 
	var specialComponentIsFreeData = button.data("spec-comp-is-free");        
	$(this).find("#spec-comp-edit-is-free").prop('checked', specialComponentIsFreeData);

	});

});



// jQuery function for populating the Delete Special Component modal
$(document).ready(function(){

	$("#deleteSpecialComponent").on("show.bs.modal", function(event){
	// Get the button that triggered the modal
	var button = $(event.relatedTarget);

	// Extract value from the custom data-* attribute
	var titleData = button.data("title");
	$(this).find(".modal-title").text(titleData);

	var specCompSnData = button.data("spec-comp-delete-serial-number");
	$(this).find("#spec-comp-delete-serial-number").val(specCompSnData);

	var partNumberData = button.data("spec-comp-delete-part-number");
	$(this).find("#spec-comp-delete-part-number").html(partNumberData);
	
	});

});


// Live Search Filter
$(document).ready(function(){
  $("#filterSpecCompsSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#specCompsResults tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});