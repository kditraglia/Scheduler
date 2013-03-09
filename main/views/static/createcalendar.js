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
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    editable: true,
    events: [
        {% for app in appointments %}
        {
            title: '{{ app.firstName }} {{ app.lastName }}',
            start: new Date({{ app.dateScheduled.year }}, {{ app.dateScheduled.month }}, {{ app.dateScheduled.day }}, 14, 0),
            condition: '{{ app.problem }}'
        },
        {% endfor %}
    ],
    eventClick: function(event,jsEvent,view){
      $dialog.dialog({title:event.title});
      $('p',$dialog).empty().append(
        $('<p />').text(event.title + " has an appointment for " + event.condition)
      );
      $dialog.dialog('open');
    },
    dayClick: function(date, allDay, jsEvent, view) {
      $schedDialog.dialog({title:date.toDateString()});
      document.getElementById("Date").value = date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate();
      $schedDialog.dialog('open');
    }
  });
});
