// main.js
console.log('Hello from main.js!');

// runs a function that updates the current time of an element by id of clock
// source code modified from: https://stackoverflow.com/questions/28415178/how-do-you-show-the-current-time-on-a-web-page
(function clock() {

	// obtain a reference to the clock element
	var clockElement = document.getElementById( "clock" );

	// create a function that sets the inner html of the clock element to client local time
	function updateClock ( clock ) {
		clock.innerHTML = new Date().toLocaleTimeString();
	}

	// create an interval function that updates the clock element each second.
	setInterval(function () {
		updateClock( clockElement );
	}, 1000);

}());

