from db import get_connection
from datetime import datetime

def take_quiz(username, mobile):
    conn = get_connection()
    cursor = conn.cursor()

    tech = input("Select technology (python/mysql): ").strip()

    cursor.execute("SELECT * FROM questions WHERE technology=%s", (tech,))
    questions = cursor.fetchall()

    if not questions:
        print("❌ No questions available for this technology.")
        conn.close()
        return

    score = 0
    for q in questions:
        print(f"\n{q[2]}")  # question text
        print(f"1. {q[3]}")
        print(f"2. {q[4]}")
        print(f"3. {q[5]}")
        print(f"4. {q[6]}")

        ans = input("Your answer (1-4): ")

        if ans.isdigit() and 1 <= int(ans) <= 4:
            if int(ans) == q[7]:
                print("✅ Correct!")
                score += 1
            else:
                # show correct answer text
                correct_option = q[2 + q[7]]  # q[3]=opt1, q[4]=opt2, etc.
                print(f"❌ Wrong! Correct answer: {q[7]}. {correct_option}")
        else:
            print("⚠️ Invalid choice! Skipping this question.")

    quiz_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        "INSERT INTO users (name, mobile, score, quiz_time) VALUES (%s, %s, %s, %s)",
        (username, mobile, score, quiz_time)
    )
    conn.commit()
    conn.close()

    print(f"\n🏁 Quiz finished! Your score: {score}/{len(questions)}")


def highest_scores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, score, quiz_time FROM users ORDER BY score DESC LIMIT 3")
    rows = cursor.fetchall()
    conn.close()

    print("\n🏆 Highest Scores:")
    if not rows:
        print("No scores available yet.")
    else:
        for idx, row in enumerate(rows, start=1):
            print(f"{idx}. {row[0]} | {row[1]} points | {row[2]}")
