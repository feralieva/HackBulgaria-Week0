def what_is_my_sign(day, month):
	if month == 1:
		if day >= 21:
			sign = "Aquarius"
		else:
			sign = "Capricorn"
	if month == 2:
		if day >= 20:
			sign = "Pisces"
		else:
			sign = "Aquarius"
	if month == 3:
		if day >= 21:
			sign = "Aries"
		else:
			sign = "Pisces"
	if month == 4:
		if day >= 21:
			sign = "Taurus"
		else:
			sign = "Aries"
	if month == 5:
		if day >= 22:
			sign = "Gemini"
		else:
			sign = "Taurus"
	if month == 6:
		if day >= 22:
			sign = "Cancer"
		else:
			sign = "Gemini"
	if month == 7:
		if day >= 23:
			sign = "Leo"
		else:
			sign = "Cancer"
	if month == 8:
		if day >= 23:
			sign = "Virgo"
		else:
			sign = "Leo"
	if month == 9:
		if day >= 24:
			sign = "Libra"
		else:
			sign = "Virgo"
	if month == 10:
		if day >= 24:
			sign = "Scorpio"
		else:
			sign = "Libra"
	if month == 11:
		if day >= 23:
			sign = "Sagittarius"
		else:
			sign = "Scorpio"
	if month == 12:
		if day >= 22:
			sign = "Capricorn"
		else:
			sign = "Sagittarius"
	return sign