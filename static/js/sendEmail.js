function sendMail(contactForm) {
	emailjs.send("gmail", "west_cork_trail_runners", {
			"from_name": contactForm.name.value,
			"from_email": contactForm.email.value,
			"info_request": contactForm.info_request.value
		})
		.then(
			function(response) {
				console.log("SUCCESS", response);
			},
			function(error) {
				console.log("FAILED", error);
			}
		);
	return false; // To block from loading a new page
}