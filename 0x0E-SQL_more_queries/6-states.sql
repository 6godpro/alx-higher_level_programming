-- Creates the database hbtn_0d_usa and the table states
   -- with attributes id and name.
  CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
  USE hbtn_0d_usa;
  CREATE TABLE
  IF NOT EXISTS states (
     	 	`id` INT NOT NULL AUTO INCREMENT,
		`name` VARCHAR(256) NOT NULL,
		PRIMARY KEY(`id`)
);
