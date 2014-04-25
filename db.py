from csv_io import *

data_path = 'C:/users/sfonoimoana/documents/flask_apps/bootstrap/static/data.csv'
standard_path = 'C:/users/sfonoimoana/documents/flask_apps/bootstrap/static/standards_data.csv'

# 0-teacher 1-domain 2-standard 3-skill 4-skill_code 5-assessment 6-1 7-2 8-3 9-4
# 0-skill 1-skill_code 2-standard 3-standard_index 4-standard_code 5-standard_description 6-cluster 7-cluster_description 8-domain 9-domain_description 10-standard_index_code


data = read_csv(data_path)[1]
standards = read_csv(standard_path)[1]

def standard_description(domain,standard_index):
	for r in standards:
		if str(r[8]) == str(domain) and int(r[3]) == int(standard_index)+1:
			return r[4]
			break
	return 'Nothing'

# pass in the standard and get back skills with list of assessments and strength
def show_skills(standard_index_code):

	skills = sorted(set([str(r[1]) for r in standards if str(r[10])==str(standard_index_code)])) # get the base list of skills for the standard from standards table
	dataObj = [] # this will be our return object (list of dictionaries)
	for s in skills:
		passing = ([float(r[8])+float(r[9]) for r in data if str(r[4])==s])
		if len(passing)>0:
			strength = sum(passing)/len(passing)
		else:
			strength = 0
		obj = {}
		obj["skill"] = s
		obj["strength"] = strength
		obj["assessments"] = passing
		dataObj.append(obj)

	return dataObj

# standard strength distribution
def standard_strength(standard_index_code):
	one = float(sum([r[6] for r in data if str(r[1])+"."+str(r[2])[0]==str(standard_index_code)]))
	two = float(sum([r[7] for r in data if str(r[1])+"."+str(r[2])[0]==str(standard_index_code)]))
	three = float(sum([r[8] for r in data if str(r[1])+"."+str(r[2])[0]==str(standard_index_code)]))
	four = float(sum([r[9] for r in data if str(r[1])+"."+str(r[2])[0]==str(standard_index_code)]))
	total = one + two + three + four
	rdict = {}
	dlist = [one/total,two/total,three/total,four/total]	
	rdict['data'] = dlist
	rdict['strength'] = dlist[2]+dlist[3]
	return rdict

# standard strength distribution
def assessment_performance(skill):
	for r in data:
		if str(r[4]) == str(skill):
			return float(r[8])+float(r[9])
			break
	return 0

# for r in standards:
# 	print r
#standard_strength('3.OA.1')