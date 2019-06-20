CREATE TABLE AlertRequest(
    RequestId SERIAL PRIMARY KEY,
    Processed BOOLEAN,
    Match BOOLEAN,
    Alerted BOOLEAN,
    UrlPhoto VARCHAR,
    BlobImg VARCHAR,
    Latitude REAL,
    Longitude REAL,
    ResquestDate DATE,
    IdPhoto INTEGER,
    NumBus INTEGER
)