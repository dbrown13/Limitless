DROP TABLE IF EXISTS goals;

CREATE TABLE goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    goal TEXT NOT NULL
);