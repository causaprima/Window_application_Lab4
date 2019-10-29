import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('PRAGMA foreign_keys = 1')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
              (id INTEGER PRIMARY KEY, FIO text, email text)''')

users_data = [(1, 'Иванов Д.С.', 'ivanov@gmail.com'),
              (2, 'Гутов Н.И.', 'sobha@gmail.com')]

cursor.executemany('INSERT OR IGNORE INTO users VALUES (?, ?, ?)', users_data)
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS characters
              (character_id INTEGER PRIMARY KEY, nickname text, server text, time_played_in_hours integer, 
              user_id INTEGER NOT NULL,
              FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE)''')

characters_data = [(1, 'DarkGunner', 'Russia', 15, 1),
                   (2, 'Sobha', 'China', 10, 2)]

cursor.executemany('INSERT OR IGNORE INTO characters VALUES (?, ?, ?, ?, ?)', characters_data)
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS achievements
              (achievement_id INTEGER PRIMARY KEY, name text, description text)''')

achievements_data = [(1, 'Добро пожаловать!', 'Создайте персонажа'),
                     (2, 'Тёпленькая пошла', 'Искупайтесь в горячем источнике')]

cursor.executemany('INSERT OR IGNORE INTO achievements VALUES (?, ?, ?)', achievements_data)
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS locations
              (location_id INTEGER PRIMARY KEY, name text, mobs text)''')

locations_data = [(1, 'Штомград', 'Крысы, гоблины'),
                  (2, 'Ущелье Холодных Ветров', 'Гарпии, волки')]

cursor.executemany('INSERT OR IGNORE INTO locations VALUES (?, ?, ?)', locations_data)
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS general_statistic
              (day INTEGER PRIMARY KEY, mobs_killed integer, gold_earned integer)''')

statistic_data = [(1, 13, 1340),
                  (2, 45, 3127),
                  (3, 33, 2988)]

cursor.executemany('INSERT OR IGNORE INTO general_statistic VALUES (?, ?, ?)', statistic_data)
conn.commit()

print('Database successfully updated')

cursor.execute('SELECT time_played_in_hours from characters')

cursor.close()
conn.close()
