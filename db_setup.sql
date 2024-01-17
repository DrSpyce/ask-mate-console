SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';

SET default_with_oids = false;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS answers;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS answers (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    question_id INTEGER REFERENCES questions(id),
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password_hash) VALUES ('user1', 'hashed_password1');
INSERT INTO users (username, password_hash) VALUES ('user2', 'hashed_password2');

INSERT INTO questions (title, content, user_id) VALUES ('Question 1', 'What is Python?', 1);
INSERT INTO questions (title, content, user_id) VALUES ('Question 2', 'How to use loops in Java?', 2);

INSERT INTO answers (content, question_id, user_id) VALUES ('Python is a high-level language.', 1, 1);
INSERT INTO answers (content, question_id, user_id) VALUES ('In Java, use for, while, or do-while loops.', 2, 2);
