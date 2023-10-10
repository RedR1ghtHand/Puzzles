CREATE TABLE users_test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    birthdate DATE
);

CREATE TABLE games_test_table (
    id SERIAL PRIMARY KEY,
    game_name VARCHAR(255),
    genre VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users_test_table (id)
);