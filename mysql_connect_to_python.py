import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Shail@123",
    database="shaileshdb"
)
print("connect sucessfully")

cursor = conn.cursor()
to_insert_data = """
    INSERT INTO students (student_id,first_name, last_name, age, grade)
    VALUES (%s,%s, %s, %s, %s)
"""
data = (1,"Alice", "Smith", 18, 95.5)
cursor.execute(to_insert_data, data)
conn.commit()

to_update_data = """
    UPDATE students
    SET grade = %s
    WHERE first_name = %s
"""
new_grade = (97.0, "Alice")
cursor.execute(to_update_data, new_grade)
conn.commit()

to_delete_data = """
    DELETE FROM students
    WHERE last_name = %s
"""
deleted_student = ("Smith",)
cursor.execute(to_delete_data, deleted_student)
conn.commit()

to_fetch_data = """
    SELECT * FROM students
"""
cursor.execute(to_fetch_data)
students = cursor.fetchall()
for student in students:
    print(student)

cursor.close()
conn.close()
