
//Edit Regular Component Detail Popup
$(document).ready(function(){
    $("#editRegularComponent").on("show.bs.modal", function(event){
        // Get the button that triggered the modal
        var button = $(event.relatedTarget);

        // Extract value from the custom data-* attribute
        var titleData = button.data("title");
        $(this).find(".modal-title").text(titleData);

        var partNumberData = parseInt(button.data("reg-comp-part-number"));
        $(this).find("#reg-comp-edit-part-number").html(partNumberData);

        var siteNameData = button.data("reg-comp-site-name");        
        $(this).find("#reg-comp-edit-site").html(siteNameData);

        var roomNumberData = parseInt(button.data("reg-comp-room-number"));
        $(this).find("#reg-comp-edit-room-number").html(roomNumberData);

        var shelfNumberData = parseInt(button.data("reg-comp-shelf-number"));
        $(this).find("#reg-comp-edit-shelf-number").html(shelfNumberData);

        var regularComponentQuantityData = button.data("reg-comp-quantity");        
        $(this).find("#reg-comp-edit-quantity").val(regularComponentQuantityData);
    });
});


// Edit Regular Quantity Modal Popup
$(document).ready(function(){
    $("#editRegularComponentQuantity").on("show.bs.modal", function(event){
        // Get the button that triggered the modal
        var button = $(event.relatedTarget);

        // Extract value from the custom data-* attribute
        var titleData = button.data("title");
        $(this).find(".modal-title").text(titleData);

        var regularComponentQuantityData = button.data("reg-comp-quantity");        
        $(this).find("#reg-comp-edit-quantity").val(regularComponentQuantityData);

        // add data for site
        var regularComponentSiteData = button.data("reg-comp-site-name");
        $(this).find("reg-comp-view-site").val(regularComponentSiteData)

        // add data for room number
        var regularComponentRoomData = button.data("reg-comp-room-number");
        $(this).find("reg-comp-view-room-number").val(regularComponentRoomData)

        // add data for shelf number
        var regularComponentShelfData = button.data("reg-comp-shelf-number");
        $(this).find("reg-comp-view-shelf-number").val(regularComponentShelfData)

    });
});



// Tooltip Toggle
	
// $('[data-toggle="tooltip"]').tooltip({
//    container: 'body'
// });




