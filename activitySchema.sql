DROP TABLE IF EXISTS activities;

CREATE TABLE activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    activity TEXT NOT NULL,
    actNum FLOAT NOT NULL,
    calories FLOAT,
    water FLOAT
);