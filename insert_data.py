print("🚀 Starting...")

import pandas as pd
import pymysql

try:
    df = pd.read_csv(r"D:\Intern\clean_superstore.csv", encoding='utf-8', on_bad_lines='skip')
    print("✅ CSV Loaded:", len(df), "rows")

    df.columns = [
        col.encode('ascii', 'ignore').decode().replace(' ', '_').replace('.', '_')
        for col in df.columns
    ]

    df = df.loc[:, df.columns != '']

    print("📊 Clean Columns:", df.columns.tolist())

    print("🔌 Connecting to MySQL...")

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root123",   # ✅ NEW PASSWORD
        database="intern_task3",
        port=3306
    )

    cursor = conn.cursor()
    print("✅ Connected to MySQL")

    cursor.execute("DROP TABLE IF EXISTS superstore")

    columns = ", ".join([f"`{col}` TEXT" for col in df.columns])
    cursor.execute(f"CREATE TABLE superstore ({columns});")

    print("✅ Table Created")

    data = [tuple(str(x) for x in row) for row in df.values]
    placeholders = ", ".join(["%s"] * len(df.columns))

    cursor.executemany(
        f"INSERT INTO superstore VALUES ({placeholders})",
        data
    )

    conn.commit()

    print("🎉 Data Inserted Successfully!")
    print("Total rows inserted:", len(df))

    cursor.close()
    conn.close()

except Exception as e:
    print("🚨 ERROR:", e)