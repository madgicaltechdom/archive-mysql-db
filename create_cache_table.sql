CREATE TABLE `cache` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `counter` int NOT NULL DEFAULT '1',
  `model_name` varchar(45) NOT NULL,
  `request` varchar(2000) NOT NULL,
  `response` longblob NOT NULL,
  `engine` varchar(45) NOT NULL,
  `lang` varchar(45) DEFAULT NULL,
  `other_prop` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `request_string` (`request`(1024)),
  KEY `counter` (`counter`),
  KEY `created_at` (`created_at`),
  FULLTEXT KEY `search_query` (`request`,`model_name`,`engine`,`lang`,`other_prop`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb3;