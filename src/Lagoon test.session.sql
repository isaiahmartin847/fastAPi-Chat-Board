-- INSERT INTO users (username, name, password)
-- VALUES ('jodie', 'jodie bittic', 'jodieB');

-- SELECT * FROM users



-- CREATE TABLE messages (
--     message_id INT PRIMARY KEY AUTO_INCREMENT,
--     text TEXT, 
--     user_id INT,
--     FOREIGN KEY (user_id) REFERENCES users(id)
-- ); 

--@BLOCk
SHOW TABLES;

--@BLOCK
 INSERT INTO users (username, name, password)
 VALUES ("admin", "isaiah", "fake_password");


--@BLOCk
 INSERT INTO messages (text, user_id)
 VALUES ('first message', 23);


--@block
DELETE FROM messages WHERE message_id = 1;

--@BLOCK 
SELECT * FROM messages

--@BLOCK 
SELECT * FROM users

--@BLOCK
SELECT users.username, messages.text
FROM messages
JOIN users ON messages.user_id = users.id;



--@block 
SELECT messages.message_id, messages.text, users.username
FROM messages
JOIN users ON messages.user_id = users.id
ORDER BY messages.message_id;


--@block 
TRUNCATE TABLE messages


--@block
TRUNCATE TABLE users


--@block
DELETE FROM users;


--@block 
SELECT users.password, user.id
FROM users 
Where username = "admin"
