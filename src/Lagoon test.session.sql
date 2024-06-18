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
 INSERT INTO messages (text, user_id)
 VALUES ('jodies message', 2);


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
SELECT messages.text, users.name
FROM messages
JOIN users ON messages.user_id = users.id
ORDER BY messages.message_id;