

// shipping modal (View Work Order)
$(document).ready(function(){
    $("#shipWorkOrder").on("show.bs.modal", function(event){
        // Get the button that triggered the modal
        var button = $(event.relatedTarget);

        // Extract value from the custom data-* attribute
        var titleData = button.data("title");
        $(this).find(".modal-title").text(titleData);

        var woIDdata = parseInt(button.data("work_order_id"));
        $(this).find("#view-work-order-id").val(woIDdata);

        var woRefNumData = button.data("work-order-reference-number");
        $(this).find("#view-work-order-reference-number").val(woRefNumData);

    });
});