#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """Prints stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of documents
    total_logs = collection.count_documents({})

    # Count documents by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method})
                     for method in methods}

    # Count documents with method GET and path /status
    status_check = collection.count_documents
    ({"method": "GET", "path": "/status"})

    # Print results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
