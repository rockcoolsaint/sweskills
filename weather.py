import re
#re.split(regex, subject)
file = open("./port-harcourt-weather.txt", "r")
smallest_day = "1"
smallest_temp_spread = 29

def file_loop(content,small_day,small_spread,max,min,dy):

	for index, line in enumerate(content, 1):
		f = re.split('\s*', line)

		if index > 1 and len(f) >= 13 :
			a = int(f[max])
			b = int(f[min])
			diff = a - b
			if diff < small_spread:
				small_spread = diff
				small_day = f[dy]
	print "Day with smallest temperature spread: Day",small_day

file_loop(file,smallest_day,smallest_temp_spread,2,3,1)