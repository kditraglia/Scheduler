$(function(){
    $(".dateinput").datepicker();
    $('#select-choice-1').prop('selectedIndex', -1)
    $("#id_phys").hide();
    $("#id_sick").hide();
    
    $("#select-choice-1").change(function () {
        var option = $("#select-choice-1 option:selected").text();
        if (option == "Sick") {
            $("#id_phys").hide();
            $("#id_sick").show();
        }
        else {
            $("#id_phys").show();
            $("#id_sick").hide();
        }
    });
});