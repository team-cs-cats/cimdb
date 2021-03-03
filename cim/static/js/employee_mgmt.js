// employee_mgmt.js

// Loads the Edit Modal popup for the employee edit function
$(document).ready(function(){
		$("#editEmployee").on("show.bs.modal", function(event){
	// Get the button that triggered the modal
	var button = $(event.relatedTarget);

	// Extract value from the custom data-* attribute
	var titleData = button.data("title");
	$(this).find(".modal-title").text(titleData);

	var employeeIdData = button.data("employee-id");
	$(this).find("#employee-id-to-update").val(employeeIdData);

	var employeeFirstNameData = button.data("employee-first-name");
	$(this).find("#edit-employee-first-name").val(employeeFirstNameData);

	var employeeLastNameData = button.data("employee-last-name");        
	$(this).find("#edit-employee-last-name").val(employeeLastNameData);

	var employeeGroupData = button.data("employee-group");
	$(this).find("#edit-employee-group").val(employeeGroupData);

	var employeeSiteData = button.data("employee-site");
	$(this).find("#edit-employee-site").val(employeeSiteData);

	var employeeEmailData = button.data("employee-email");
	$(this).find("#edit-employee-email").val(employeeEmailData);

	
});
	});