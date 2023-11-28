-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.1.2-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for lentokentat
CREATE DATABASE IF NOT EXISTS `lentokentat` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;
USE `lentokentat`;

-- Dumping structure for table lentokentat.airport
CREATE TABLE IF NOT EXISTS `airport` (
  `ident` varchar(40) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `iso_country` varchar(40) DEFAULT NULL,
  `level_image` mediumblob DEFAULT NULL,
  PRIMARY KEY (`ident`),
  KEY `iso_country` (`iso_country`),
  CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`iso_country`) REFERENCES `country` (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table lentokentat.airport: ~4 rows (approximately)
INSERT INTO `airport` (`ident`, `name`, `iso_country`, `level_image`) VALUES
	('BIKF', 'Keflavik International Airport', 'IS', NULL),
	('EFHK', 'Helsinki Vantaa Airport', 'FI', NULL),
	('EKCH', 'Copenhagen Kastrup Airport', 'DK', NULL),
	('ENGM', 'Oslo Airport, Gardermoen', 'NO', NULL);

-- Dumping structure for table lentokentat.country
CREATE TABLE IF NOT EXISTS `country` (
  `iso_country` varchar(40) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table lentokentat.country: ~4 rows (approximately)
INSERT INTO `country` (`iso_country`, `name`, `continent`) VALUES
	('DK', 'Denmark', 'EU'),
	('FI', 'Finland', 'EU'),
	('IS', 'Iceland', 'EU'),
	('NO', 'Norway', 'EU');

-- Dumping structure for table lentokentat.leaderboard
CREATE TABLE IF NOT EXISTS `leaderboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table lentokentat.leaderboard: ~1 rows (approximately)
INSERT INTO `leaderboard` (`id`, `username`, `score`) VALUES
	(1, 'player1', 100);

-- Dumping structure for table lentokentat.player_profiles
CREATE TABLE IF NOT EXISTS `player_profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `score` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table lentokentat.player_profiles: ~1 rows (approximately)
INSERT INTO `player_profiles` (`id`, `username`, `score`) VALUES
	(1, 'player1', 100);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
