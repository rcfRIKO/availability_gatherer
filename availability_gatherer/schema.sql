DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS gatherer;
DROP TABLE IF EXISTS entry;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE gatherer (
    uuid TEXT PRIMARY KEY,
    creator_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    FOREIGN KEY  (creator_id) REFERENCES user (id)
);

CREATE TABLE entry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gatherer_id TEXT NOT NULL,
    email TEXT NOT NULL,
    key TEXT,
    date TEXT NOT NULL,
    only_if_necessary BOOLEAN NOT NULL,
    FOREIGN KEY (gatherer_id) REFERENCES gatherer (id)
);