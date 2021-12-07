CREATE TABLE users_tab(
    id SERIAL,
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
    id SERIAL,
    dictionary INT,
    description VARCHAR,
    PRIMARY KEY(id)
);

CREATE TABLE dictionary_mapping_tab(
    word VARCHAR,
    theme_id INT,
    FOREIGN KEY(word) REFERENCES words_tab(word),
    FOREIGN KEY(theme_id) REFERENCES themes_tab(id),
    PRIMARY KEY(word, theme_id)
);