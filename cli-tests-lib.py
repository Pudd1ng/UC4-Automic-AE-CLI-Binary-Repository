#!/usr/bin/python
import os,subprocess,re

Release = 1.0

## Path to Folders containing all binaries
CliBinFolder = "C:\\Automic\\CLI\\UC4-Automic-AE-CLI-Binary-Repository\\"
ConfigFile = CliBinFolder + "connection.config"

def checkConfigFile():
	if (not os.path.isfile(ConfigFile)):
		return False
	if 'AE_IP_ADR' not in open(ConfigFile).read():
		print " \t -- Warning: AE_IP_ADR missing from config file"
	if 'AE_PRIMARY_PORT' not in open(ConfigFile).read():
		print " \t -- Warning: AE_PRIMARY_PORT missing from config file"
	if 'AE_CLIENT' not in open(ConfigFile).read():
		print " \t -- Warning: AE_CLIENT missing from config file"
	if 'AE_LOGIN' not in open(ConfigFile).read():
		print " \t -- Warning: AE_LOGIN missing from config file"
	if 'AE_DEPT' not in open(ConfigFile).read():
		print " \t -- Warning: AE_DEPT missing from config file"
	if 'AE_PASSWORD' not in open(ConfigFile).read():
		print " \t -- Warning: AE_PASSWORD missing from config file"			
	return True

# Get all available JARS in an array
def getJarBinsInArray():
	BinArrayName = []
	for file in os.listdir(CliBinFolder):
		if file.endswith(".jar"):
			BinArrayName.append(file)
	return BinArrayName

# Get all Std Parameters from a given Jar (should always be the same..)
def getStdHelpLines(BinName):
	ArrayLines = []
	#print " \t %% Running Command for binary: " + BinName
	proc = subprocess.Popen(['java', '-jar', BinName, '-help'], stdout=subprocess.PIPE,)
	stdout_value = proc.communicate()[0]
	AllOutputLines = stdout_value.split("\n")
	for line in AllOutputLines:
		if line.startswith(" -"):
			ArrayLines.append(line)
			#print "FOUND: " + line
	return ArrayLines

# Get all Std Parameters from a given Jar (should always be the same..)
def getSpecHelpLines(BinName):
	ArrayLines = []
	#print " \t %% Running Command for binary: " + BinName
	proc = subprocess.Popen(['java', '-jar', BinName, '-h'], stdout=subprocess.PIPE,)
	stdout_value = proc.communicate()[0]
	AllOutputLines = stdout_value.split("\n")
	for line in AllOutputLines:
		if line.startswith(" -"):
			ArrayLines.append(line)
			#print "FOUND: " + line
	return ArrayLines

def isStdLineCompliant(StdLine):
	StdRegExp = "^ -[C|D|H|L|P|W],.+"
	StdRegExpHelp = "^ -help,--help"
	reMatch = re.match(StdRegExp,StdLine)
	reMatchHelp = re.match(StdRegExpHelp,StdLine)
	if not reMatch and not reMatchHelp:
		print "\t -- ERROR: Line Not Compliant with STD Parameters:" + StdLine
	#else:
		#print "Match Found:" + StdLine

def checkSpecHelp(lines):
	for line in lines:
		if (re.match("^ -h[ ]*[Dd]isplay [Hh]elp & [Aa]vailable [Pp]arameters",line)):
			return True
	return False

# Commit flag needs to show the commit option syntax AND its Optional aspect
def checkSpecCommit(lines):
	for line in lines:
		if (re.match("^ -commit.+",line) and re.match(".+[OPTIONAL].+",line)):
			return True
	return False

#-commit              [OPTIONAL] - Commit (Only Simulations run by default)
#-f_category <arg>    [OPTIONAL] (RegEx supported) - Filter by License Category.
#-f_name <arg>        [OPTIONAL] (RegEx supported) - Filter by Agent Name.
#-f_sm_name <arg>     [OPTIONAL] (RegEx supported) - Filter by Service Manager Name.
def parseParamLine(line):
	# We first process the param name, whether there is arguments expected and the OPTIONAL / MANDATORY flag
	strs = line.split()
	paramName = strs[0]
	if "<arg>" in line:
		paramType = strs[2]
		strs.remove("<arg>")
	else:
		paramType = strs[1]
		
	strs.remove(paramType)
	strs.remove(paramName)
	
	remainder = ''.join(strs)
	#print "DEBUG:"+remainder
	strs = remainder.split("-")
	Format = strs[0]
	if(len(strs)==2):
		Description = strs[1]
	else:
		Description = ""
	return [paramName, paramType, Format, Description]
	
	
# MAIN
checkConfigFile()
AllBins = getJarBinsInArray()
#print AllBins
for item in AllBins:
	print " %% Starting Process for: " + item
	# check std parameters (connection stuff)
	StdLines = getStdHelpLines(item)
	for StdLine in StdLines:
		isStdLineCompliant(StdLine)
	
	# check generalized spec parameters (-h and -commit)
	SpecLines = getSpecHelpLines(item)
	# if 0 the binary requires no parameters.. no need to check in that case
	if len(SpecLines) > 0:
		if not checkSpecHelp(SpecLines):
			print "\t -- ERROR: Help Option -h is not Compliant or not found"
		if not checkSpecCommit(SpecLines):
			print "\t -- ERROR: Commit Option -commit is not Compliant or not found"

	# check specific parameters
	for line in SpecLines:
		if '-commit' not in line and 'display help' not in line and "-- Error:" not in line:
			#print "DEBUG Processing Line: " + line
			resArray = parseParamLine(line)
			# Expected: [0]: parameter name [1]: Optional or Mandatory [2]: Format (can be empty) [3]: Description (cannot be empty)
			if not resArray[0]:
				print "\t -- ERROR: Parameter Name Format is empty"
				
			if(not re.match("^-[a-z_]+",resArray[0])):
				print "\t -- ERROR: Parameter Name Format is wrong: " + resArray[0]
				
			if not resArray[1]:
				print "\t -- ERROR: Parameter Type is empty (Should be MANDATORY or OPTIONAL)"
			
			if('MANDATORY' not in resArray[1] and 'OPTIONAL' not in resArray[1]):
				print "\t -- ERROR: Parameter Type is Wrong (Should contain MANDATORY or OPTIONAL at least): " + resArray[0]
	
			if not resArray[3]:
				print "\t -- ERROR: Something is wrong. No Description Found for option: " + resArray[0]
				print "\t =>    Line is: " + line #+ " | " + str(resArray)

print " ++ End Of Processing."			
			#print myArray