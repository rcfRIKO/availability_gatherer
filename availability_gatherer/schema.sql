DROP TABLE IF EXISTS gatherers;
DROP TABLE IF EXISTS entries;

CREATE TABLE gatherers (
    gatherer_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gatherer_id TEXT NOT NULL,
    author TEXT NOT NULL,
    key TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    only_if_necessary BOOLEAN NOT NULL,
    FOREIGN KEY (gatherer_id) REFERENCES gatherers (id)
);