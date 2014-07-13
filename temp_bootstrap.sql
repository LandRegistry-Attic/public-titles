--get rid of this v soon indeed and maybe use factory boy for creating test data?
DELETE FROM title;
INSERT INTO title (title_number, address, post_code) VALUES ('TN1234567', '1 High Street, SomePlace', 'ABC 123');
INSERT INTO title (title_number, address, post_code) VALUES ('TN7654321', '2 High Street, SomePlace', 'ABC 123');
INSERT INTO title (title_number, address, post_code) VALUES ('AB1234567', '12 Low Street, SomeOtherPlace', 'XYZ 981');
INSERT INTO title (title_number, address, post_code) VALUES ('YZ7654321', '35 Low Street, SomeOtherPlace', 'XYZ 981');
