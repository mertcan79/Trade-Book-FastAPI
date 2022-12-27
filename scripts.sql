CREATE TABLE trade_history(
    instrument_id VARCHAR(20) PRIMARY KEY,
    position INTEGER NOT NULL,
    timestamp TIMESTAMP,
    price REAL NOT NULL
);

CREATE TABLE positions (
    instrument_id VARCHAR(20) PRIMARY KEY,
    position INTEGER NOT NULL
);

CREATE TABLE prices (
    instrument_id VARCHAR(20) PRIMARY KEY,
    price REAL NOT NULL
);

CREATE TABLE transaction_costs (
    instrument_id VARCHAR(20) PRIMARY KEY,
    cost REAL NOT NULL
);

CREATE TABLE risk_aversion (
    risk_aversion REAL NOT NULL
);

CREATE TABLE volatilities (
    instrument_id VARCHAR(20) PRIMARY KEY,
    volatility REAL NOT NULL
);


INSERT INTO positions (instrument_id, position) VALUES ('ABC', 100), ('AAPL', 50), ('GOOG', 200);
INSERT INTO prices (instrument_id, price) VALUES ('ABC', 100), ('AAPL', 50), ('GOOG', 200);
INSERT INTO transaction_costs (instrument_id, cost) VALUES ('ABC', 0.1), ('AAPL', 0.1), ('GOOG', 0.1);
INSERT INTO risk_aversion (risk_aversion) VALUES (0.5);
INSERT INTO volatilities (instrument_id, volatility) VALUES ('ABC', 0.1), ('AAPL', 0.2), ('GOOG', 0.3);
