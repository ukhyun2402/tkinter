CREATE TABLE IF NOT EXISTS MEMBER(
    IDX INT(10) unsigned AUTO_INCREMENT PRIMARY KEY,
    ID VARCHAR(20) NOT NULL,
    PASSKEY VARCHAR(100) NOT NULL,
    PHONE VARCHAR(14) NOT NULL DEFAULT '',
    EMAIL VARCHAR(50) NOT NULL DEFAULT ''
);

--- MODIFY ---
ALTER TABLE MEMBER ADD COLUMN PHOTO VARCHAR(100) DEFAULT 'default';

--- Data ---
INSERT INTO MEMBER(ID,PASSKEY,PHONE,EMAIL) VALUES('ukhyun','1234','01024021051','hyun4911@gmail.com'),('ukhyun1','1234','01024021051','hyun4911@gmail.com'),('ukhyun2','1234','01024021051','hyun4911@gmail.com'),('ukhyun','1234','01024021051','hyun4911@gmail.com'),('ukhyun3','1234','01024021051','hyun4911@gmail.com')