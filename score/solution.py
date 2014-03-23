def slope_style_score(scores):
	scores.sort()
	return int((sum(scores[1:-1]) / (len(scores) - 2))*100)/100