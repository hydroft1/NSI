-- create a table
CREATE TABLE elevesNSI (
    id INTEGER PRIMARY KEY,
    prenom TEXT NOT NULL,
    nom TEXT NOT NULL,
    moisNais INTEGER 
);
-- insert some values
INSERT INTO elevesNSI VALUES (1, 'Raphaël', 'RB', 06);
INSERT INTO elevesNSI VALUES (2, 'Adam', 'AC', 02);
INSERT INTO elevesNSI VALUES (3, 'Valentin', 'VCB', 08);
INSERT INTO elevesNSI VALUES (4, 'Nicolas', 'ND', 03);
INSERT INTO elevesNSI VALUES (5, 'Maxence', 'MG', 09);
INSERT INTO elevesNSI VALUES (6, 'Thomas', 'TH', 02);
INSERT INTO elevesNSI VALUES (7, 'Alexandre', 'AM', 05);
INSERT INTO elevesNSI VALUES (8, 'Maxime', 'MM', 09);
INSERT INTO elevesNSI VALUES (9, 'Noe', 'NN', 05);
INSERT INTO elevesNSI VALUES (10, 'Mathys', 'MP', 09);
INSERT INTO elevesNSI VALUES (11, 'Hicham', 'HV', 07);
INSERT INTO elevesNSI VALUES (12, 'Kurt', 'KYB', NULL);


-- fetch some values
-- SELECT * FROM elevesNSI WHERE nom = 'MM';
-- SELECT nom, prenom FROM elevesNSI WHERE moisNais = 8;
-- SELECT prenom FROM elevesNSI WHERE prenom LIKE 'R%';
-- SELECT count(*) FROM elevesNSI WHERE moisNais = 4;
-- SELECT prenom FROM elevesNSI WHERE moisNais = 9 AND prenom LIKE 'M%';
-- SELECT prenom FROM elevesNSI ORDER by prenom ASC;
-- SELECT prenom FROM elevesNSI ORDER by nom ASC;
