from db import get_connection

def add_question():
    conn = get_connection()
    cursor = conn.cursor()
    tech = input("Enter technology (python/mysql): ").strip()
    ques = input("Enter question: ")
    options = [input(f"Option {i+1}: ") for i in range(4)]
    ans = int(input("Enter correct option (1-4): "))

    query = """
        INSERT INTO questions (technology, question, option1, option2, option3, option4, answer) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (tech, ques, options[0], options[1], options[2], options[3], ans))
    conn.commit()
    conn.close()
    print("✅ Question added successfully!")


def modify_question():
    conn = get_connection()
    cursor = conn.cursor()
    qid = int(input("Enter question ID to modify: "))

    new_question = input("Enter new question: ")
    new_options = [input(f"New Option {i+1}: ") for i in range(4)]
    new_ans = int(input("Enter new correct option (1-4): "))

    query = """
        UPDATE questions 
        SET question=%s, option1=%s, option2=%s, option3=%s, option4=%s, answer=%s 
        WHERE id=%s
    """
    cursor.execute(query, (new_question, new_options[0], new_options[1], new_options[2], new_options[3], new_ans, qid))
    conn.commit()
    conn.close()
    print("✅ Question updated successfully!")


def delete_question():
    conn = get_connection()
    cursor = conn.cursor()
    qid = int(input("Enter question ID to delete: "))
    cursor.execute("DELETE FROM questions WHERE id=%s", (qid,))
    conn.commit()
    conn.close()
    print("✅ Question deleted successfully!")


def view_all_questions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    conn.close()

    print("\n📋 All Questions:")
    for row in rows:
        print(f"\nID: {row[0]} | Technology: {row[1]}")
        print(f"Q: {row[2]}")
        print(f"1. {row[3]}")
        print(f"2. {row[4]}")
        print(f"3. {row[5]}")
        print(f"4. {row[6]}")
        print(f"✅ Correct Answer: {row[7]}")


def view_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    print("\n👥 All Users:")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Mobile: {row[2]} | Score: {row[3]} | Time: {row[4]}")
