// set the date we're counting down to
var target_date = new Date("Aug 15, 2019").getTime();
 
// variables for time units
var days, hours, minutes, seconds;
 
// get tag element
var day = document.getElementById("day");
var hour = document.getElementById("hours");
var mins = document.getElementById("mins");
var secs = document.getElementById("secs") 
// update the tag with id "countdown" every 1 second
setInterval(function () {
 
    // find the amount of "seconds" between now and target
    var current_date = new Date().getTime();
    var seconds_left = (target_date - current_date) / 1000;
 
    // do some time calculations
    days = parseInt(seconds_left / 86400);
    seconds_left = seconds_left % 86400;
     
    hours = parseInt(seconds_left / 3600);
    seconds_left = seconds_left % 3600;
     
    minutes = parseInt(seconds_left / 60);
    seconds = parseInt(seconds_left % 60);
     
    // format countdown string + set tag value

    day.innerHTML = days;
    hour.innerHTML = hours;
    mins.innerHTML = minutes;
    secs.innerHTML = seconds;

}, 1000);