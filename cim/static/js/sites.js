	
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

		// var siteAddress1Data = button.data("site-address-1");
		// $(this).find("#site-delete-address-1").val(siteAddress1Data);

		// var siteAddress2Data = button.data("site-address-2");        
		// $(this).find("#site-delete-address-2").val(siteAddress2Data);

		var siteCityData = button.data("site-address-city");
		$(this).find("#site-delete-city").html(siteCityData);

		// var siteStateData = button.data("site-address-state");
		// $(this).find("#site-delete-state").val(siteStateData);

		// var siteZipData = button.data("site-address-postal-code");        
		// $(this).find("#site-delete-zip").val(siteZipData);

	});

});


// Live Search Filter
// $(document).ready(function(){

//     // select 
//     $("#filterSearch").on("input",function(e){
        
//         $("#datalist").empty();
//         $.ajax({
//             method:"post",
//             url:"/site-mgmt",
//             data:{text:$("#filterSearch").val()},

//             success:function(res){
//                 var data = "<ul>";
//                 console.log('res is ' + res);
//                 $.each(res,function(index,value){
//                     console.log(value.site_id);
//                     data += "<li>"+value.site_id+"</li>";
//                 });
//                 data += "</ul>";
//                 $("#datalist").html(data);
//             }
//         });
//     });
// });
