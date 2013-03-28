$(function(){
  var $schedDialog = $('#sched-details').dialog({
    autoOpen: false,
    model: true,
    height: 300,
    width: 350
  });
  var $dialog = $('#appointment-detail').dialog({
    autoOpen: false,
    model: true,
    height: 300,
    width: 350
  });

  $('#calendar').fullCalendar({
    disableDragging: true,
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    events: [],
    eventClick: function(event,jsEvent,view){
      showAppointment(jsEvent, event.start);
    },
    dayClick: function(date, allDay, jsEvent, view) {
      showAppointment(jsEvent, date);
    },
  });

  function showAppointment(jsEvent, date) {
    $(".fc-state-highlight").removeClass("fc-state-highlight");
    $(jsEvent.currentTarget).addClass("fc-state-highlight");
    document.getElementById("appointment-info").style.visibility="visible";
    document.getElementById("Date").value = date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate();
    getTimes();
  }
    function getTimes() {
      var l = [];
      var a = new Date(1,1,1,8,0,0);
      for (var i=0; i<37;i++) {
          var c = document.getElementById("appt-times");
          var o = document.createElement("option");
          o.text = a.toString("hh:mm tt");
          o.value = a.toString("hh:mm tt");
          try {
              c.add(o, null); //Standard 
          }catch(error) {
              c.add(o); // IE only
          }
		      a.setMinutes(a.getMinutes() + 15);
      }
   };
});
