//1. Find documents where the "tags" field exists. 
db.inventory.find({
    tags: {$exists : true}
})

//2. Find documents where the "tags" field does not contain values "ssl" or "security." 

db.inventory.find({
    tags: {$nin: ["ssl", "security"]}
})

//3. Find documents where the "qty" field is equal to 85. 

db.inventory.find({
    qty: {$eq: 85}
})

db.inventory.find({qty : 85})


//4. Find documents where the "tags" array contains all of the values [ssl, security] using the `$all` operator. 

db.inventory.find({
    tags: {$all: ["ssl", "security"]}
})


//a) Question: If you need to find only the two values "ssl" and "security", what change would you make to your query? 
db.inventory.find({
    tags: {$all: ["ssl", "security"]}
}, {_id : 0, code:0, qty : 0})


db.inventory.find({
    tags: {$all: ["ssl", "security"],
    $size: 2}
})


//5.Update the "item" field in the "paper" document, update "size.uom" to "meter" and using the `$currentDate` operator. 

db.inventory.updateOne({item: "paper"},
{
    $set: {
        "size.uom": "meter" 
    },
    $currentDate: {
        lastModified: true
    }
})


//a)
db.inventory.updateOne({item: "laptopDevice"},
{
    $set: {
        "size.uom": "meter" 
    },
    $currentDate: {
        lastModified: true
    }
},
    {
        upsert: true
    })


db.inventory.find({_id: ObjectId("697dfb1b4724b82fae17f64d")})

//b)

db.inventory.updateOne({ item : "laptopSame" },    
    {
        $set: {
            "size.uom": "meter" 
        },
        
        $currentDate : {
             lastModified : true
        },
        
        $setOnInsert : {
            dataSource: "todayRegister"
        }
        
    },
        {
            upsert : true
        })
        
db.inventory.find({_id: ObjectId("697dfd104724b82fae17f64e")})


db.inventory.updateOne(
    { item: "laptopSame" },
    {
        $set: { "size.uom": "meter" },
        $currentDate: { lastModified: true },
        $setOnInsert: { dataSource: "todayRegister" }
    },
    { upsert: true }
)


db.inventory.find({_id: ObjectId("697dfd104724b82fae17f64e")})



//c)
db.inventory.updateMany(
  { item: "paper" },
  {
    $set: { "size.uom": "meter" },
    $currentDate: { lastModified: true }
  }
)


//d)
db.inventory.replaceOne(
  { item: "paper" },
  {
    item: "paper",
    qty: 100,
    size: {
      h: 8.5,
      w: 11,
      uom: "meter"
    },
    status: "D",
  }
)


//6. Insert a document with incorrect field names "neme" and "ege," then rename them to "name" and "age."
 // Insert document with wrong field names
db.inventory.insertOne({
  neme: "Ahmad",
  ege: 25
})

// Rename the fields
db.inventory.updateOne(
  { neme: { $exists: true } },
  {
    $rename: {
      "neme": "name",
      "ege": "age"
    }
  }
)

//7. Try to reset any document field using the `$unset` function. 
db.inventory.updateOne(
  { item: "paper" },
  {
    $unset: { status: "" }
  }
)


//8. Try update operators like `$inc`, `$min`, `$max`, and `$mul` to modify document fields. 

db.inventory.updateOne(
  { name: "EmployeeSama" },
  {
    $setOnInsert: {
      salary: 2000,
      overtime: 20,
      age: 22,
      quantity: 10,
      price: 100
    }
  },
  { upsert: true }
)

db.inventory.find({name : "EmployeeSama"})

db.inventory.updateOne(
  { name: "EmployeeSama" },
  {
    $max: { salary: 10000 },
    $min: { overtime: 15 },
    $inc: { age: 1 },
    $mul: { quantity: 2, price: 2 }
  }
)


db.inventory.find({name : "EmployeeSama"})


// Calculate the total revenue for product from sales
//a)
db.sales.aggregate([
  {
    $match: {
      date: {
        $gte: ISODate("2020-01-01T00:00:00.000Z"),
        $lte: ISODate("2023-01-01T00:00:00.000Z")
      }
    }
  },
  {
    $group: {
      _id: "$product",
      totalRevenue: {
        $sum: { $multiply: ["$quantity", "$price"] }
      }
    }
  },
  {
    $sort: { totalRevenue: -1 }
  }
])


//10. Calculate the average salary for employees for each department from the employee’s collection. 
db.employees.aggregate([{
    $group: {
        _id: "$department",
        avgSalary: {
            $avg: "$salary"
        }
    }
}])


//11. Use likes Collection to calculate max and min likes per title 
db.likes.aggregate([{
    $group: {
        _id: "$title"
    ,
    maxlikes: { $max: "$likes"},
    minlikes: { $min: "$likes"}
    }
}])
