// 1. Create a Database named "ITI_Mongo". 
use ITI_Mongo

show dbs

//2. Create a Collection named "Staff". 
db.createCollection("Staff")

//3. Insert one document into the "Staff" collection: {_id, name, age, gender, department}. 
db.Staff.insertOne({
   "_id":27,
   "Name":"Sama",
   "Age":22,
   "Gender":"F",
   "Department":"Data Engineering"
})

//4. Insert many documents into the "Staff" collection
db.Staff.insertMany(
[{
_id : 28,
"Name" : "seif" ,
"Age" : 20,
"Gender" : "Male",
"Department" : "Java"
},
{
_id : 29,
"Name" : "omnia" ,
"Age" : 25,
"Gender" : "Female",
"managerName" : "Ahmed",
"Department" : "IT"
},
{
_id : 30,
"Name" : "muhammed" ,
"Age" : 15,
"Gender" : "Male",
"DateOfBirth" : ISODate("2003-07-27")
}]
)

//Query to find data from the "Staff" collection: 
 //1) Find all documents. 
 db.Staff.find()
 
 //2) Find documents where gender is "male". 
 db.Staff.find({Gender : "Male"})
 
 //3) Find documents with age between 20 and 25. 
 db.Staff.find({Age : {
     $gte : 20,
     $lte : 25
 }})
 
 //4) Find documents where age is 25 and gender is "female". 
 db.Staff.find({Age : 25 , Gender : "Female"})
 
 //5) Find documents where age is 20 or gender is "female". 
 db.Staff.find({
     $or : [
     {Age  : 20},
     {Gender : "Female"}
     ]
 })
 
//6.Update one document in the "Staff" collection where age is 15, set the name to "yourname"
db.Staff.updateOne({Age : 15},
{
    $set : {Name : "Sama"}
})

//7. Update many documents in the "Staff" collection, update the department to "AI". 
db.Staff.updateMany(
{},
{
    $set : {Department : "AI"}
}
)

db.Staff.find()


//8. Create a new collection called "test" and insert documents from Question 4. 
db.createCollection("test")

db.test.insertMany(
[{
_id : 28,
"Name" : "seif" ,
"Age" : 20,
"Gender" : "Male",
"Department" : "Java"
},
{
_id : 29,
"Name" : "omnia" ,
"Age" : 25,
"Gender" : "Female",
"managerName" : "Ahmed",
"Department" : "IT"
},
{
_id : 30,
"Name" : "muhammed" ,
"Age" : 15,
"Gender" : "Male",
"DateOfBirth" : ISODate("2003-07-27")
}]
)

//9. Try to delete one document from the "test" collection where age is 15. 
db.test.deleteOne(
{Age : 15}
)

db.test.find()

db.test.insertMany(
[{
_id : 5,
"Name" : "ahmed" ,
"Age" : 15
},
{
_id : 6,
"Name" : "eman" ,
"Age" : 15
}])


//10.  try to delete all male gender 

db.test.deleteMany(
{Gender : "Male"})

//11. Try to delete all documents in the "test" collection. 
db.test.deleteMany({}); 

// id 5, muhammed , age 15
// id 1 , sama, age 15


