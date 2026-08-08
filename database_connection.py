import oracledb

# Enable Thick mode
oracledb.init_oracle_client(
    lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin"
)

connection = oracledb.connect(
    user="SCOTT",
    password=tiger,
    dsn="localhost:1521/XE"
)

print("Oracle Connected Successfully!")

cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM cell_performance_view"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
