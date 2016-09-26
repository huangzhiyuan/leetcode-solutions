def lengthOfLongSubstring(s):
	max = 0
	tmpstr = ""
	for ch in s:
		if not ch in tmpstr:
			tmpstr += ch
			if len(tmpstr) > max:
				max = len(tmpstr)
		else:
			tmpstr = tmpstr[tmpstr.find(ch)+1:]+ch
	return max
