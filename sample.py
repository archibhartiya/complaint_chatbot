# import asyncio
# import aiohttp

# async def fetch(session, url):
#     async with session.get(url) as response:
#         data = await response.json()
#         return data

# async def fetch_both():
#     url1 = "https://jsonplaceholder.typicode.com/todos/1"
#     url2 = "https://dummyjson.com/products/1"
    
#     async with aiohttp.ClientSession() as session:
#         task1 = asyncio.create_task(fetch(session, url1))
#         task2 = asyncio.create_task(fetch(session, url2))
        
#         result1, result2 = await asyncio.gather(task1, task2)
        
#         print(result1)
#         print(result2)

# # Run the asynchronous function
# if __name__ == "__main__":
#     asyncio.run(fetch_both())
# from fastapi import FastAPI
# import httpx

# app = FastAPI()

# @app.get("/external-data")
# async def get_external_data():
#     url = "https://api.adviceslip.com/advice"
    
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         return response.json()

import sqlite3

def view_complaints():
    # Connect to the database
    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    # Show all tables
    print("📋 Tables in the database:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)

    # Show column names of the 'complaint' table
    print("\n🧱 Columns in 'complaint' table:")
    cursor.execute("PRAGMA table_info(complaint);")
    columns = cursor.fetchall()
    for col in columns:
        print(f"- {col[1]} ({col[2]})")

    # Show all rows from complaint table
    print("\n📦 Complaint Records:")
    cursor.execute("SELECT * FROM complaint;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    view_complaints()
