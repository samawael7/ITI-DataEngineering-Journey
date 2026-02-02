//1
db.createCollection("employee", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required : ["name", "age", "department"],
            properties : {
                name : {
                    bsonType : "string",
                    description: "name must be a string and is required"
                    
                },
                age : {
                    bsonType : "int",
                    minimum : 18,
                    description: "age must be an int and is required"

                },
                department : {
                    bsonType : "string",
                    enum : ["HR", "Engineering", "Finance"],
                    description: "department must be a string and is required"

                }
            }
        }
    }
})


//2
use Demo
db.createCollection("trainningCenter1")
db.createCollection("trainningCenter2")

//2-a
var data = [
{
    _id : 1,
    "name" : {
        "fname" : "sama",
        "lname" : "wael"
    },
    "age" : 22,
    "address" : "cairo",
    "status" : ["active"]
    
}
]

//withoutt using data[0]??

//2-b


var doc = data.shift()
db.trainningCenter1.insertOne(doc)

db.getCollection("trainningCenter1").find({})

//2-c
db.trainningCenter2.insertMany(data)

db.getCollection("trainningCenter1").find({})

//3
db.trainningCenter1.find({ age: 22 }).explain("executionStats")


//4
db.trainningCenter1.createIndex({age:1}, {name : "IX_age"})

//5
db.trainningCenter1.find({ age: 22 }).explain("executionStats")

//6
db.trainningCenter1.find({
    "name.fname": "sama",
    "name.lname": "wael"
}).explain("executionStats")

db.trainningCenter1.createIndex(
{"name.fname" : 1, "name.lname" : 1},
{name : "compound"}
)

db.trainningCenter1.find({
    "name.fname": "sama",
    "name.lname": "wael"
}).explain("executionStats")


db.dropDatabase()
show dbs