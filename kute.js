const tween1 = KUTE.fromTo(
	"#blob1",
	{ path: "#blob1" },
	{ path: "#blob2" },
	{ repeat: true, duration: 3000, yoyo: true }
);

tween1.start();

const tween2 = KUTE.fromTo(
	"#blob3",
	{ path: "#blob3" },
	{ path: "#blob4" },
	{ repeat: true, duration: 3000, yoyo: true }
);

tween2.start();

const tween3 = KUTE.fromTo(
	"#blob5",
	{ path: "#blob5" },
	{ path: "#blob6" },
	{ repeat: true, duration: 3000, yoyo: true }
);

tween3.start();
