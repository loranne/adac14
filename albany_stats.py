# opening csv in python
# this block is my setup for the whole exercise
import csv
import pdb
import statistics 

with open ('albany_stats_2012.csv', 'r') as stats:
    myfile = csv.DictReader(stats)
    # "row" can be any fucking thing you want! it doesn't matter!
    data = [row for row in myfile]

# QUESTION 1: Who had the highest regular earnings?

# earnlist is a list comprehension that is the column of regular earnings
earnlist = [row['REGULAR EARNINGS'] for row in data]
# changes elements to a float (i.e. a number)
earnlist = [float(x) for x in earnlist]
# float converts to real numbers and is needed to call the function max on elements in earnlist. maxearn is a variable representing that value
maxearn = max(earnlist)
# this gets the index of the max value in earnlist 
maxearn_index = earnlist.index(maxearn)
print ('QUESTION 1 ANSWER IS...')
# print includes "end = ' '" in order to continue printing on the same line instead of different lines
print (maxearn, end = ' ')
print (data[maxearn_index]['EMPLOYEE NAME FIRST'], end = ' ')
print (data[maxearn_index]['EMPLOYEE NAME MI'], end = ' ') 
print (data[maxearn_index]['EMPLOYEE NAME LAST'], end = ' ')
print (data[maxearn_index]['EMPLOYEE NAME SUFFIX'])

# DEBUGGER
#pdb.set_trace()

# QUESTION 2: How many depts have more than 150 employees?

# list comprehension that means depts is a list of all dept names in data
depts = [row['DEPARTMENT NAME'] for row in data]
depts = set (depts)
#print (depts)

# this defines a new function called employee_in_dept
# dept here is a new variable that applies only to this function
def employee_in_dept (dept):
    #this is a list comprehension. not all functions are list comprehensions. it needs a name because we need the returned info.
    # says that for each row in data, given a department name, add it to the list.
    dept_total = [row for row in data if dept == row['DEPARTMENT NAME']]
    # return is storing the info from the function. return here is # of records with a given dept. name
    return len(dept_total)

print ('QUESTION 2 ANSWER IS...')
# list comprehension: for each dept name in depts, add it to this list if the function employee_in_dept of that dept name returns a result greater than 150.
big_depts = [dept_name for dept_name in depts if employee_in_dept(dept_name) > 150]
# prints the list of department names with more than 150 employees. 
print (big_depts)

#pdb.set_trace()

# QUESTION 3: What is the median of overtime earnings column for all employees in depts w/ more than 50 employees

# list comprehension, med_depts is a list of all dept names if the function defined on line 70 shows a result of more than 50 employees
med_depts = [dept_name for dept_name in depts if employee_in_dept(dept_name) > 50]
# makes another list comprehension based on data if the dept name is in the good dept list
ot_earn = [float(row['OVERTIME EARNINGS']) for row in data if row['DEPARTMENT NAME'] in med_depts]
# makes a new variable called median, which calls the median function on ot_earn
median = statistics.median(ot_earn)
print ('QUESTION 3 ANSWER IS...')
print (median)

# QUESTION 4: Which employees in the Fire Dept whose 1st names don't begin with R made more than the mayor in total earnings?

# makes a list comprehension that includes first, MI, last, and suffix of everyone's name in the fire dept who makes more than the mayor. Also concatenates names into 1 string each (from 4)
fire_dept = [row['EMPLOYEE NAME FIRST'] + ' ' + row['EMPLOYEE NAME MI'] + ' ' + row['EMPLOYEE NAME LAST'] + ' ' + row['EMPLOYEE NAME SUFFIX'] for row in data if row['DEPARTMENT NAME'] == 'FIRE DEPARTMENT' and float(row['TOTAL EARNINGS']) > 136403.42]
# listcomp redefines fire_dept as list of all employees' names whose first names don't start with R in the previous list.
fire_dept = [row for row in fire_dept if row[0] != 'R']
print ('QUESTION 4 ANSWER IS...')
print (fire_dept)

# QUESTION 5: Which departments have employees earning more than $1k longevity pay AND earned more than median household income for NY state in 2012?

#listcomp creates new list of department names if longevity pay and total earnings are above certain amounts. Floats are to convert from strings to numbers
high_earn = [row['DEPARTMENT NAME'] for row in data if float(row['LONGEVITY PAY']) > 1000 and float(row['TOTAL EARNINGS']) > 57683]
# listcomp transforms calling set function which makes list into only unique department names
high_earn = set (high_earn)
print ('QUESTION 5 ANSWER IS...')
print (high_earn)














