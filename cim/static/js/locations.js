
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

        var siteNameData = button.data("site-name");        
        $(this).find("#location-site").val(siteNameData);
    });
});
