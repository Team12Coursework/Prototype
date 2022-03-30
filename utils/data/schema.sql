CREATE TABLE users_tab(
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    leaderboard_points INTEGER DEFAULT 0,
    username VARCHAR(255),
    password VARCHAR(255),
    email VARCHAR,
    PRIMARY KEY(id),
    UNIQUE(username),
    UNIQUE(email)
);

CREATE TABLE words_tab(
    word VARCHAR,
    definition VARCHAR,
    PRIMARY KEY(word)
);

CREATE TABLE themes_tab(
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    dictionary INTEGER,
    description VARCHAR,
    PRIMARY KEY(id)
);

CREATE TABLE dictionary_mapping_tab(
    word VARCHAR,
    theme_id INTEGER,
    FOREIGN KEY(word) REFERENCES words_tab(word),
    FOREIGN KEY(theme_id) REFERENCES themes_tab(id),
    PRIMARY KEY(word, theme_id)
);

INSERT INTO themes_tab(dictionary, description) VALUES(0, 'all');
INSERT INTO themes_tab(dictionary, description) VALUES(1, 'banned chat words');
INSERT INTO themes_tab(dictionary, description) VALUES(2, 'maths wordset');
INSERT INTO themes_tab(dictionary, description) VALUES(3, 'science wordset');