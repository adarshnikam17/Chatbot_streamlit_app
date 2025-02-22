import streamlit as st
import openai
import sqlite3
import os

openai.api_key = os.getenv("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")

def find_answer(query):
    try:
        conn = sqlite3.connect(r'C:\Users\ADARSH\Desktop\AIPoweredChatBot\chatbot_project\backend\faqs.db')
        cursor = conn.cursor()

        cursor.execute("SELECT answer FROM faqs WHERE question LIKE ?", ('%' + query + '%',))
        result = cursor.fetchone()

        conn.close()


        return result[0] if result else None
    except sqlite3.OperationalError as e:
        print("Database error:", e)
        return None


def ai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error fetching AI response: {e}"

st.title("AI-Powered Customer Support Chatbot")

user_input = st.text_input("You:")

if user_input:

    response = find_answer(user_input)

    if response:
        st.write(f"Bot: {response}")
    else:
        ai_bot_response = ai_response(user_input)
        st.write(f"Bot: {ai_bot_response}")

