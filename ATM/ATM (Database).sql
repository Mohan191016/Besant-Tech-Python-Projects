-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 24, 2022 at 03:06 PM
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
-- Table structure for table `account_transactions_history`
--

DROP TABLE IF EXISTS `account_transactions_history`;
CREATE TABLE IF NOT EXISTS `account_transactions_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `account_no` varchar(50) NOT NULL,
  `transactions_date_time` varchar(255) NOT NULL,
  `transactions_type` varchar(50) NOT NULL,
  `transactions_amount` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `account_transactions_history`
--

INSERT INTO `account_transactions_history` (`id`, `account_no`, `transactions_date_time`, `transactions_type`, `transactions_amount`) VALUES
(17, '0123456789', '24-09-2022 08:23:10 PM', 'Deposit', 100),
(18, '0123456789', '24-09-2022 08:23:23 PM', 'Deposit', 456),
(19, '0123456789', '24-09-2022 08:23:37 PM', 'Withdrawal', 308);

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
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `account_users`
--

INSERT INTO `account_users` (`id`, `account_no`, `account_holder_name`, `account_pin`) VALUES
(22, '0123456789', 'MOHAN K', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
