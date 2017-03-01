CREATE TABLE IF NOT EXISTS status (
    id INT PRIMARY KEY,
    description TEXT
);

INSERT INTO status VALUES (0, 'new') ON CONFLICT DO NOTHING ;
INSERT INTO status VALUES (1, 'fetching') ON CONFLICT DO NOTHING;
INSERT INTO status VALUES (2, 'processing') ON CONFLICT DO NOTHING;
INSERT INTO status VALUES (3, 'processed') ON CONFLICT DO NOTHING;
INSERT INTO status VALUES (4, 'fetching failed') ON CONFLICT DO NOTHING;
INSERT INTO status VALUES (5, 'processing failed') ON CONFLICT DO NOTHING);

CREATE TABLE IF NOT EXISTS category (
    id INT PRIMARY KEY,
    description TEXT
);

INSERT INTO category VALUES (0, 'other') ON CONFLICT DO NOTHING ;
INSERT INTO category VALUES (1, 'disaster') ON CONFLICT DO NOTHING;
INSERT INTO category VALUES (2, 'conflict') ON CONFLICT DO NOTHING;

CREATE TABLE article (
    id SERIAL PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    domain TEXT,
    status INT REFERENCES status,
    title TEXT,
    publication_date TIMESTAMP,
    authors TEXT,
    language CHAR(2),
    relevance BOOL,
    reliability DECIMAL
);

CREATE TABLE content (
    article INT PRIMARY KEY REFERENCES article ON DELETE CASCADE,
    retrieval_date TIMESTAMP,
    content TEXT,
    content_type TEXT
);

CREATE TABLE article_category (
    article INT REFERENCES article ON DELETE CASCADE,
    category INT REFERENCES category ON DELETE CASCADE,
    PRIMARY KEY (article, category)
);

CREATE TABLE country (
    code CHAR(2) PRIMARY KEY
);

CREATE TABLE country_term (
    term TEXT PRIMARY KEY,
    country CHAR(2) REFERENCES country ON DELETE CASCADE
);

CREATE TABLE location (
    id SERIAL PRIMARY KEY,
    description TEXT,
    country CHAR(2),
    latlong TEXT
);


CREATE TABLE report (
    id SERIAL PRIMARY KEY,
    article INT REFERENCES article ON DELETE CASCADE,
    event_term TEXT,
    subject_term TEXT,
    quantity INT,
    tag_locations JSON,
    accuracy DECIMAL,
    analyzer TEXT,
    analysis_date TIMESTAMP WITH TIME ZONE
);

CREATE TABLE report_location (
    report INT REFERENCES report ON DELETE CASCADE,
    location INT REFERENCES location ON DELETE CASCADE,
    PRIMARY KEY (report, location)
);

CREATE TABLE report_datespan (
    id INT PRIMARY KEY,
    report INT REFERENCES report ON DELETE CASCADE,
    start TIMESTAMP,
    finish TIMESTAMP
);


