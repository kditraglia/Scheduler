$(function getTimes() {
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
 });
