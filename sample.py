
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

