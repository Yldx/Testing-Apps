import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if len(results) > 0:
    for result in results:
        print(result[1])

else:
    print("No word found!")

