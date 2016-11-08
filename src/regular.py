import re

# def is_whole(str):
# 	if str.count(' ') >= 1:
# 		print str
# 		return False
# 	return True

def replaceOP(str):
	pattern1 = ur'\+'
	pattern2 = ur'-'
	pattern3 = ur'\*'
	pattern4 = ur'/'
	pattern5 = ur'\('
	pattern6 = ur'\)'
	pattern7 = ur'\['
	pattern8 = ur'\]'
	pattern9 = ur'<='
	pattern10 = ur'>='
	pattern11 = ur'<'
	pattern12 = ur'<'
	pattern13 = ur'='
	pattern14 = ur'&'
	pattern15 = ur'\^'

	res = re.sub(pattern1, ' Plus ', str)
	res = re.sub(pattern2, ' Minius ', res)
	res = re.sub(pattern3, ' Multiply ', res)
	res = re.sub(pattern4, ' Devide ', res)
	res = re.sub(pattern5, ' Lrb ', res)
	res = re.sub(pattern6, ' Rrb ', res)
	res = re.sub(pattern7, ' Lsb ', res)
	res = re.sub(pattern8, ' Rsb ', res)
	res = re.sub(pattern9, ' LE ', res)
	res = re.sub(pattern10, ' GE ', res)
	res = re.sub(pattern11, ' LT ', res)
	res = re.sub(pattern12, ' GT ', res)
	res = re.sub(pattern13, ' EQ ', res)
	res = re.sub(pattern14, ' AND ', res)
	res = re.sub(pattern15, ' INDEX ', res)

	# print str,'\t->', res

	return res

def replaceNumbers(str):
	ptfloat = '\d+.\d+'
	ptint = '\d+'

	replfloat = ' floatNumber '
	replint = ' intNumber '
	res = re.sub(ptfloat, replfloat, str)
	res = re.sub(ptint, replint, res)
	return res

# replaceOP('+-*/()[]=')
def replaceVarXYZ(str):
	ptx = ur'[xX]'
	pty = ur'[yY]'
	ptz = ur'[zZ]'

	res = re.sub(ptx, ' VARX ', str)
	res = re.sub(pty, ' VARY ', res)
	res = re.sub(ptz, ' VARZ ', res)
	# print str, '->', res
	return res

def iswhole(str):
	if str.count(' ') >= 1:
		# print 'not whole', str
		return False
	return True

def replaceLinkSymbol(str):
	pt1 = ur'-[\d]+'
	repl1 = ' NumberAfterLinkSymbol '
	new_str = re.sub(pt1, repl1, str)

	pt2 = ur'-'
	repl2 = ' '
	new_str = re.sub(pt2, repl2, new_str)

	# print new_str
	return new_str

def replaceNumberAfterP(str):
	pt = ur'(P\d+$)|(p\d+$)'
	repl = 'P NumberAfterP'
	new_str = re.sub(pt, repl, str)
	return new_str

def replace_(str):
	pt = ur'[_]'
	repl = ' '
	new_str = re.sub(pt, repl, str)
	return new_str

def replaceAndSplitbyNumbers(str):
	pt = ur'[\d]+'
	repl = ' NumberInShortProblemName '
	new_str = re.sub(pt, repl, str)
	return new_str

def replaceNumberAfterSplitbyLinkSymbol(str):
	pt = ur'\d+'
	repl = ' NumberInPartSplitByLinkSymbol '
	new_str = re.sub(pt, repl, str)
	return new_str

def has_link_symbol(str):
	if '-' in str and '=' not in str:
		# print 'has -:', str 
		return True
	return False

def handle_whole(str):
	new_str = ''
	if has_link_symbol(str):
		# like this: GLFM-TICKETS
		new_str = replaceLinkSymbol(str)
		new_str = replaceNumberAfterP(new_str)
		new_str = replaceNumberAfterSplitbyLinkSymbol(new_str)
		# print str, '--->', new_str
	else:
		# might be SY=-100X-500&Y=50X+150
		# might be 2PTFB16
		if '=' in str or '&' in str:
			new_str = replaceNumbers(str)
			new_str = replaceVarXYZ(new_str)
			new_str = replaceOP(new_str)
			# print str, '--->', new_str
		else:
			# might be 'FOR08_SP',  'BH1T02A'
			new_str = replace_(str)
			new_str = replaceAndSplitbyNumbers(new_str) 
			# print str, '->', new_str
	assert new_str != ' '
	return new_str




def handle_right(str):
	new_str = str
	new_str= replaceVarXYZ(new_str)
	new_str = replaceOP(new_str)
	new_str = replaceNumbers(new_str)
	return new_str