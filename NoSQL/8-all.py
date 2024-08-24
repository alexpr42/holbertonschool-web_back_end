#!/usr/bin/env python3
"""function that list all documents in collection"""


def insert_school(mongo_collection, **kwargs):
    """
        Inserts a new document using the provided kwargs.

        Args:
            mongo_collection: The MongoDB collection.

        Returns:
            The id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
