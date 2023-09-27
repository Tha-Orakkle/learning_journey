function speakSomething(what, howMany=10) {
	for (var i = 0; i < howMany; i++) {
		console.log(what, "("  + i + ")");
	}

	return;
}

speakSomething('hey hey');
