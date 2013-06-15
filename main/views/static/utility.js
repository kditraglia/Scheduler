$(document).ready(function(){
    $(".dateinput").datepicker();
    $(".timeinput").timepicker({
        'step': 15,
        'minTime': '8:00am',
	'maxTime': '5:00pm',
    });;
    $('#select-choice-1').prop('selectedIndex', -1)
    $('#select-choice-2').prop('selectedIndex', -1)
    $("#id_phys").hide();
    $("#id_problem").hide();
    $("#id_checkup").hide();
    
    $("#select-choice-1").change(function () {
        $("#id_phys").hide();
        $("#id_problem").hide();
        $("#id_checkup").hide();
        var option = $("#select-choice-1 option:selected").text();
        if (option == "Problems") {
            $("#id_problem").show();
        }
        else if (option == "Checkup") {
            $("#id_checkup").show();
        }
        else {
            $("#id_phys").show();
        }
    });
});