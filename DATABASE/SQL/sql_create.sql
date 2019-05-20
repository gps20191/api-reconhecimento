CREATE TABLE AlertRequest (
    RequestId SERIAL PRIMARY KEY,
    Processed BIT,
    Match BIT,
    urlPhoto VARCHAR,
    Location REAL ARRAY[2],
    RequestDate DATE
);

CREATE TABLE AlertNotified (
    NotifiedId SERIAL PRIMARY KEY,
    NotificationDate DATE,
    RequestId INTEGER REFERENCES AlertRequest(RequestId)
);

CREATE TABLE AlertArchive (
    ArchiveId SERIAL PRIMARY KEY,
    ArchiveDate DATE,
    RequestId INTEGER REFERENCES AlertRequest(RequestId)
);

CREATE TABLE Procurados (
    ProcuradoId SERIAL PRIMARY KEY,
    FaceData REAL ARRAY,
    Nome VARCHAR
);
 
