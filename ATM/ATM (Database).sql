-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 20, 2022 at 05:00 AM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atm`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_transactions`
--

DROP TABLE IF EXISTS `account_transactions`;
CREATE TABLE IF NOT EXISTS `account_transactions` (
  `account_no` varchar(50) NOT NULL,
  `account_balance` float NOT NULL,
  PRIMARY KEY (`account_no`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `account_transactions`
--

INSERT INTO `account_transactions` (`account_no`, `account_balance`) VALUES
('9944141880', 0),
('12345', 200),
('1234567890', 1);

-- --------------------------------------------------------

--
-- Table structure for table `account_users`
--

DROP TABLE IF EXISTS `account_users`;
CREATE TABLE IF NOT EXISTS `account_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account_no` varchar(50) NOT NULL,
  `account_holder_name` varchar(255) NOT NULL,
  `account_pin` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `account_users`
--

INSERT INTO `account_users` (`id`, `account_no`, `account_holder_name`, `account_pin`) VALUES
(18, '9944141880', 'KOKILA K', '123'),
(17, '12345', 'MOHAN K', '12345');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
