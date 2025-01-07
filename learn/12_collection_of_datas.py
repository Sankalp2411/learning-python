#tuple
browser = ('chrome','edge','brave','firefox','firefox');
print(browser);
#indexing
print(browser[0]);#positive
print(browser[-1]);#negative
print(browser[1:3]);#slicing
browser = browser + browser #adding
print(browser);
browser = browser*2 #multiplying
print(browser);
#operations on tuple
browser.count('edge');
browser.index('edge');
len(browser);
max(browser);
min(browser);
browser = list(browser);


#list
students = ['sankalp','vaishnavi','aditya','aaditya'];
print(students);
#indexing
print(students[0]);#positive
print(students[-1]);#negative
print(students[1:3]);#slicing
students=students+students #adding
print(students);
students=students*3 #multipying
print(students);
#operations on list
students.append('me');
student=[];
student.extend(students);
students.insert(2,'me');
students.remove('me');
students.pop(2);
students.index("aditya");
students.count("aditya");
students.sort();
students.reverse();
student.clear();
students.copy();
students.len();
students.max();
students.min();
students = tuple(students);


#dictionary
myself = {'name':'sankalp','surname':'jadhav','age':20,'email':'jadhavsankalp2004@gmail.com'};
seq ={1:1,2:10,3:11,4:100};
v={1:'I',2:'II',3:'III',4:'IV'};
print(myself);
myself.get('name');#accessing
myself['name']='Sankalp';#updating
myself['address']='satara';#adding
del(myself['age']);#deleting
myself.pop('email');#deleting
myself.popitem();#deleting
myself.keys(); #veiw keys
myself.values(); #veiw values
myself.copy(); #copy
myself.fromkeys(seq[v]); #fromkeys
v.clear(); #clear
myself.items(); #veiw items
v.update(seq); #update
myself.len(); #length
seq.max(); #max
seq.min(); #min
myself.all(); #select all
myself.any(); #select any
seq.cmp(v); #compare
myself.sort(); #sort
