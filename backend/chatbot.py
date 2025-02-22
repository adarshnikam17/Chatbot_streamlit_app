import openai
import sqlite3

# Set up OpenAI API key
openai.api_key = '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'

# Function to create the database and insert FAQ data if the table does not exist
def create_table():
    conn = sqlite3.connect('faqs.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS faqs (
        question TEXT,
        answer TEXT
    )
    ''')
    cursor.execute('''
    INSERT INTO faqs (question, answer)
    VALUES 
    ("What are your operating hours?", "We are open from 9 AM to 9 PM daily."),
    ("How can I track my order?", "You can track your order using the tracking link sent via email.")
    ''')
    conn.commit()
    conn.close()

# Function to find the answer from the database based on the query
def find_answer(query):
    conn = sqlite3.connect('faqs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faqs WHERE question LIKE ?", ('%' + query + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Function to get a response from OpenAI's GPT
def ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use different models if needed
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Ensure the table is created and populated
create_table()

# Example user query
user_query = "How can I track my order?"

# Try fetching the answer from the database first
response = find_answer(user_query)
if response:
    print(f"Database answer: {response}")
else:
    # If not found in the database, use AI to generate a response
    print(f"AI answer: {ai_response(user_query)}")
