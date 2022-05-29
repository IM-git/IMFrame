import pymongo
from .credential import Credential

LOGIN = Credential.LOGIN
PASSWORD = Credential.PASSWORD
LINK_CLUSTER = Credential.LINK_CLUSTER


class MongodbMain:
    """
    This is the main methods which use in mongodb.
    """

    def __init__(self):
        self.client = pymongo.MongoClient(
            f"mongodb+srv://{LOGIN}:{PASSWORD}{LINK_CLUSTER}")
        self.database = self.client.testdata
        self.collection = self.database.users

    def insert_document(self, data):
        """
        Function to insert a document into a collection and
        return the document's id.
        """
        self.collection.insert_one(data)

    def find_document(self, elements, multiple=False):
        """
        Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        if multiple:
            results = self.collection.find(elements)
            return [r for r in results]
        else:
            return self.collection.find_one(elements)

    def update_document(self, query_elements, new_values):
        """
        Function to update a single document in a collection.
        """
        self.collection.update_one(query_elements, {'$set': new_values})

    def delete_document(self, query):
        """
        Function to delete a single document from a collection.
        """
        self.collection.delete_one(query)
