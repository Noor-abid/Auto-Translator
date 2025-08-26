import json
college={
"college": "Engineering college",
"objectives": "Mastering Electrical and Computer Engineering",
"departments":{
    "dept1": "Electrical",
    "dept2":"Computer"
},
"years":[
    "year 1",
    "year 2",
    "year 3",
    "year 4"
],
"numbers":[1,2,3,4],
"ID":[10,20,30,40]
}
json.dump(college, open("college.json","w"))
new_college=json.load(open("college.json","r"))
new_college