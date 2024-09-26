import motor.motor_asyncio

from bson import ObjectId


MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.production
productioncoll = database.get_collection("productionColl")


# helpers
def productionHelper(production) -> dict:
    return {
        "id": str(production["_id"]),
        "date": str(production["date"]),
        "quantity": int(production["quantity"]),
        "hours": int(production["hours"]),
        "productionList": str(production["productionList"]),
        "departmentList": str(production["departmentList"]),
        "comment": str(production["comment"]),
    }


# Retrieve all production entries
async def retrieveProductions():
    productionEntries = []
    async for productionCat in productioncoll.find():
        productionEntries.append(productionHelper(productionCat))
    return productionEntries


# Add a new production
async def addProduction(productionData: dict) -> dict:
    production = await productioncoll.insert_one(productionData)
    newProduction = await productioncoll.find_one({"_id": production.inserted_id})
    return productionHelper(newProduction)


# Retrieve a production
async def getProduction(id: str) -> dict:
    production = await productioncoll.find_one({"_id": ObjectId(id)})
    if production:
        return productionHelper(production)


# Update a production
async def updateProduction(id: str, data: dict):
    # Return false if an empty request body is sent
    if len(data) < 1:
        return False
    production = await productioncoll.find_one({"_id": ObjectId(id)})
    if production:
        updatedProduction = await productioncoll.update_one(
            {"_id": ObjectId}, {"$set": data}
        )
    if updatedProduction:
        return True
    return False


# delete a production
async def deleteProduction(id: str):
    production = await productioncoll.find_one({"_id": ObjectId(id)})
    if production:
        await productioncoll.delete_one({"_id": ObjectId(id)})
        return True
