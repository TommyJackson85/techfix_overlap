//Bugs and Features pages
$('#finished_bugs').hide();
$(".toggle_bug_data").click(function () {
    if ($("#in_progress_bugs").is(":visible")) {
         $("#in_progress_bugs").hide();
         $("#finished_bugs").show();
    } else {
        $("#finished_bugs").hide();
        $("#in_progress_bugs").show();
    }
});