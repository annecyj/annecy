# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Capella": {
	"RA": "05h 16m 41.4s",
	"Dec": "+45° 59′ 53″",
	"Magnitude": 0.08,
	"Spectral Type": "G3III"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def star_name(dictionary):
	for star_name in dictionary:
		print(f"{star_name}")
print(star_name(targets))
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_spectral_type(dictionary):
	for star_name, star_info in dictionary.items():
		spectral_type = star_info["Spectral Type"]
		print(f"{star_name}: {spectral_type}")

print(name_spectral_type(targets))
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def bright_mag_stars(dictionary):
	bright_stars = {}
	for star_name, star_info in dictionary.items():
		if star_info["Magnitude"] > 0.1:
			bright_stars[star_name] = star_info
			print(f"{star_name}: {bright_stars[star_name]["Magnitude"]}")
print(bright_mag_stars(targets))
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def bright_dec_star(dictionary):
	brightest_star = max(dictionary.values())
	for star_name, star_info in dictionary.items():
		if brightest_star and 15 >= star_info["Dec"] >= 25:
			print(f"{star_name}: {bright_stars[star_name]["Dec"]}")
	return(bright_dec_star(targets))
# 6) What is your favorite constellation?
# cygnus

