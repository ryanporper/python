x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)

people = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(some_list):
    for each_key in some_list:
        print(each_key)

iterate_dictionary(people)

def iterate_dictionary2(a_list):
    for i in range(len(a_list)):
        print(a_list[i]["first_name"])
    for i in range(len(a_list)):
        print(a_list[i]["last_name"])
    
iterate_dictionary2(people)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    print(len(some_dict['locations']), 'Locations')
    for i in range(len(some_dict['locations'])):
        print(some_dict['locations'][i])

    print(len(some_dict['instructors']), 'Instructors')
    for i in range(len(some_dict['instructors'])):
        print(some_dict['instructors'][i])

print_info(dojo)
