CREATE DATABASE `fileinfo`;

CREATE TABLE `files` (
  `path_hash` varchar(512) NOT NULL PRIMARY KEY,
  `path` varchar(4096) NOT NULL,
  `file_name` varchar(2048) NOT NULL,
  `file_hash` varchar(512) NOT NULL
);