CREATE DATABASE `fileinfo`;

CREATE TABLE `files` (
  `id` bigint NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `path_hash` varchar(2048) NOT NULL,
  `path` varchar(2048) NOT NULL,
  `file_name` varchar(2048) NOT NULL,
  `file_hash` varchar(2048) NOT NULL
);