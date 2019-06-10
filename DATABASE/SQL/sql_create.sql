CREATE TABLE AlertRequest(
    RequestId SERIAL PRIMARY KEY,
    Processed BIT,
    Match BIT,
    Alerted BIT,
    UrlPhoto VARCHAR,
    BlobImg VARCHAR,
    Latitude REAL,
    Longitude REAL,
    ResquestDate DATE,
    IdPhoto INTEGER,
    NumBus INTEGER
)