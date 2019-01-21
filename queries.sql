CREATE DATABASE UserInfo;
use UserInfo;
CREATE TABLE userDetails(
  `id` int(10) UNSIGNED NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `country`varchar(255) DEFAULT NULL,
  `age` int(10) UNSIGNED NOT NULL,
  `highest_education`varchar(255) DEFAULT NULL
  );

ALTER TABLE `userDetails` ADD PRIMARY KEY(`id`);
ALTER TABLE `userDetails` CHANGE `id` `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT;
