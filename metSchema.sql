DROP TABLE IF EXISTS metTable;

CREATE TABLE metTable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity TEXT NOT NULL,
    intensity TEXT NOT NULL,
    met FLOAT NOT NULL
);

INSERT INTO metTable (activity, intensity, met)
VALUES ("walking", "low", 2.8 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("walking", "moderate", 3.5 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("walking", "high", 4.3 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("lifting", "low", 3.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("lifting", "moderate", 5.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("lifting", "high", 7.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("hiit", "low", 5.5 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("hiit", "moderate", 8.5 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("hiit", "high", 11.6 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("running", "low", 8.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("running", "moderate", 11.5 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("running", "high", 23.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("yoga", "low", 2.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("yoga", "moderate", 4.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("yoga", "high", 6.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("swimming", "low", 5.8 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("swimming", "moderate", 8.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("swimming", "high", 11.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("cycling", "low", 6.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("cycling", "moderate", 10.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("cycling", "high", 12.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("tennis", "singles", 9.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("tennis", "doubles", 5.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("basketball", "casual", 6.5 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("basketball", "competitive", 8.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("soccer", "casual", 7.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("soccer", "competitive", 10.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("volleyball", "casual", 3.0 );
INSERT INTO metTable (activity, intensity, met)
VALUES ("volleyball", "competitive", 8.0 );

