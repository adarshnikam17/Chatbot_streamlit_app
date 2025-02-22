import sqlite3

conn = sqlite3.connect('faqs.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS faqs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

cursor.executemany('''
INSERT INTO faqs (question, answer)
VALUES
    (?, ?)
''', [
    ('What are your hours of operation?', 'We are open from 9 AM to 9 PM daily.'),
    ('How can I track my order?', 'You can track your order using the tracking link sent via email.'),
    ('How can I contact support?', 'You can contact support by emailing support@company.com.'),
    ('What is your refund policy?', 'You can return items within 30 days.'),
    ('Do you ship internationally?', 'Yes, we offer international shipping to most countries.'),
    ('What payment methods do you accept?', 'We accept credit/debit cards, PayPal, and net banking.'),
    ('Can I change my delivery address after placing an order?', 'Yes, you can change your address within 24 hours of placing the order.'),
    ('How long does shipping take?', 'Standard shipping takes 3-7 business days, and express shipping takes 1-3 business days.'),
    ('Is there a warranty on your products?', 'Yes, our products come with a 1-year warranty.'),
    ('Do you have a mobile app?', 'Yes, our mobile app is available on both iOS and Android.'),
    ('How do I reset my account password?', 'Click "Forgot Password" on the login page and follow the instructions.'),
])

conn.commit()
conn.close()

print("Database setup complete.")
