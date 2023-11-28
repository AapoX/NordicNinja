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

-- Dumping data for table lentokentat.airport: ~4 rows (approximately)
INSERT INTO `airport` (`ident`, `name`, `iso_country`, `level_image`) VALUES
	('BIKF', 'Keflavik International Airport', 'IS', NULL),
	('EFHK', 'Helsinki Vantaa Airport', 'FI', NULL),
	('EKCH', 'Copenhagen Kastrup Airport', 'DK', NULL),
	('ENGM', 'Oslo Airport, Gardermoen', 'NO', NULL);

-- Dumping data for table lentokentat.country: ~4 rows (approximately)
INSERT INTO `country` (`iso_country`, `name`, `continent`) VALUES
	('DK', 'Denmark', 'EU'),
	('FI', 'Finland', 'EU'),
	('IS', 'Iceland', 'EU'),
	('NO', 'Norway', 'EU');

-- Dumping data for table lentokentat.leaderboard: ~1 rows (approximately)
INSERT INTO `leaderboard` (`id`, `username`, `score`) VALUES
	(1, 'player1', 100);

-- Dumping data for table lentokentat.player_profiles: ~1 rows (approximately)
INSERT INTO `player_profiles` (`id`, `username`, `score`) VALUES
	(1, 'player1', 100);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
