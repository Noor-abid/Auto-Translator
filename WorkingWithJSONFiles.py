import json
college={
"college": "Engineering college",
"objectives": "Mastering Electrical and Computer Engineering",
"departments":{
    "dept1": "Electrical",
    "dept2":"Computer"
},
"years":["year 1","year 2","year 3","year 4"],
"numbers":[1,2,3,4],
"ID":[10,20,30,40]
}

#Save with JSON
with open("college.json","w") as f:
  json.dump(college, f,indent=4)

#Load back
with open("college.json","r") as f:
  new_college=json.load(f)
new_college