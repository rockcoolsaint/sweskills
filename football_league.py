import re
#re.split(regex, subject)
file = open("./football-league-results.txt", "r")
smallest_team = "Kano Pillars"
smallest_diff = 43

def file_loop(content,small_team,small_diff,gf,ga,fname=None,lname=None):
	
	for index, line in enumerate(content, 1):
		if index > 1:
			f = line.lstrip()
			f = f.rstrip()
			f = re.split('\s*', f)

		if index > 1 and re.match(r'[^-]+',f[0]):	
			a = int(f[gf])
			b = int(f[ga])
			diff = a - b
			if diff < small_diff:
				small_diff = diff
				small_team = f[fname] + " "  + f[lname]
	print "Team with least goals difference: ",small_team, small_diff

file_loop(file,smallest_team,smallest_diff,7,9,1,2)