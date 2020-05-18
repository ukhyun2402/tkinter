CREATE TABLE IF NOT EXISTS MEMBER(
    IDX INT(10) unsigned AUTO_INCREMENT PRIMARY KEY,
    ID VARCHAR(20) NOT NULL,
    PASSKEY VARCHAR(100) NOT NULL,
    NAME VARCHAR(100) NOT NULL,
    PHONE VARCHAR(14) NOT NULL DEFAULT '',
    EMAIL VARCHAR(50) NOT NULL DEFAULT '',
    PHOTO VARCHAR(100) DEFAULT 'default.png'
)ENGINE = InnoDB DEFAULT CHARSET = utf8;

--- MODIFY ---

--- Data ---
INSERT INTO MEMBER(ID,PASSKEY,PHONE,EMAIL,name,PHOTO) VALUES
('ukhyun','1234','01024021051','hyun4911@gmail.com','하욱현','ukhyun.png'),
('ukhyun1','1234','01024021051','hyun4911@gmail.com','하욱현1','ukhyun1.png'),
('ukhyun2','1234','01024021051','hyun4911@gmail.com','Jail','jail.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png'),
('ukhyun','1234','01024021051','hyun4911@gmail.com','welcome','welcome.png'),
('ukhyun3','1234','01024021051','hyun4911@gmail.com','hello','hello.png')