
class RunTests:
    def __init__(self, client):
        self.client = client(db_directory="/home/marcus/Documents/pymongo-the-sql/tests/")

    def test(self):
        db = self.client.get_database("test")
        users = db["users"]
        errands = db["errands"]

        _id = users.find_one({"username": "marcus"}, "id")["id"]
        print(_id)
        print(errands.find({"subject": "LOL"}, "*"))


