import re
#re.split(regex, subject)
file = open("./football-league-results.txt", "r")
smallest_team = "Kano Pillars"
smallest_diff = 43

def file_loop(content,small_team,small_diff,gf,ga,fname,lname):

	for index, line in enumerate(content, 1):
		f = re.split('\s*', line)

		if index > 1 and len(f) >= 13 :
			a = int(f[gf])
			b = int(f[ga])
			diff = a - b
			if diff < small_diff:
				smallest_diff = diff
				small_team = f[fname] + " "  + f[lname]
	print "Team with least goals difference: ",small_team

file_loop(file,smallest_team,smallest_diff,8,10,2,3)