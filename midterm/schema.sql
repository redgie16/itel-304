CREATE TABLE users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    password text NOT NULL,
    admin boolean NOT NULL DEFAULT '0'
    );

CREATE TABLE emp (
    empid INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    email text,
    phone INTEGER,
    address text,
    joining_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_projects INTEGER DEFAULT 1,
    total_test_case INTEGER DEFAULT 1,
    total_defects_found INTEGER DEFAULT 1,
    total_defects_pending INTEGER DEFAULT 1
);