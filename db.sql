-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2024 at 06:47 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `snappfood`
--

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client`
(
  `ID`            int(11)      NOT NULL,
  `Name`          varchar(255) NOT NULL,
  `Phone`         varchar(255) DEFAULT NULL,
  `Address`       varchar(255) DEFAULT NULL,
  `creation_date` date         DEFAULT NULL,
  `password`      varchar(255) DEFAULT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`ID`, `Name`, `Phone`, `Address`, `creation_date`, `password`)
VALUES (1, 'Pouyan Hessabi', '123-456-7890', '123 Elm St, Springfield', '2023-09-01', ''),
       (2, 'Parham', '987-654-3210', '456 Oak St, Shelbyville', '2023-09-02', ''),
       (3, 'Ali Azizi', '555-123-4567', '789 Maple Ave, Capital City', '2023-09-03', ''),
       (4, 'Sara', '111-222-3333', '101 Birch Rd, Ogdenville', '2023-09-04', ''),
       (5, 'Reza', '222-333-4444', '202 Cedar Ln, North Haverbrook', '2023-09-05', ''),
       (6, 'Omid', '333-444-5555', '303 Pine St, Springfield', '2023-09-06', ''),
       (7, 'Ata', '444-555-6666', '404 Spruce St, Shelbyville', '2023-09-07', ''),
       (8, 'Zahra', '555-666-7777', '505 Fir St, Capital City', '2023-09-08', ''),
       (9, 'Azita', '666-777-8888', '606 Redwood Blvd, Ogdenville', '2023-09-09', ''),
       (10, 'Bahar', '777-888-9999', '707 Chestnut St, North Haverbrook', '2023-09-10', ''),
       (11, 'Mahtaj', '888-999-0000', '808 Sycamore Ln, Springfield', '2023-09-11', ''),
       (12, 'Mahdi', '999-000-1111', '909 Willow Rd, Shelbyville', '2023-09-12', ''),
       (13, 'Babak', '000-111-2222', '1010 Aspen St, Capital City', '2023-09-13', ''),
       (14, 'Ehsan', '111-222-3333', '1111 Cypress St, Ogdenville', '2023-09-14', ''),
       (15, 'Nazi', '222-333-4444', '1212 Palm St, North Haverbrook', '2023-09-15', ''),
       (16, 'Simin', '333-444-5555', '1313 Magnolia Blvd, Springfield', '2023-09-16', ''),
       (17, 'Navid', '444-555-6666', '1414 Oakwood Ln, Shelbyville', '2023-09-17', ''),
       (18, 'Alireza', '555-666-7777', '1515 Highland St, Capital City', '2023-09-18', ''),
       (19, 'Hamid', '666-777-8888', '1616 Redwood Dr, Ogdenville', '2023-09-19', ''),
       (20, 'Javad', '777-888-9999', '1717 Dogwood Ave, North Haverbrook', '2023-09-20', ''),
       (26, 'pouyan.hessabi@gmail.com', '', '', '2024-09-30', '123'),
       (27, 'zccxx', '', '', '2024-09-30', '123'),
       (28, 'test', '', '', '2024-10-01', '');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket`
(
  `ID`            int(11) NOT NULL,
  `description`   varchar(255) DEFAULT NULL,
  `type`          varchar(255) DEFAULT NULL,
  `is_active`     tinyint(1)   DEFAULT NULL,
  `client_id`     int(11) NOT NULL,
  `creation_date` date         DEFAULT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`ID`, `description`, `type`, `is_active`, `client_id`, `creation_date`)
VALUES (1, 'Issue with login', 'bug', 1, 1, '2023-09-01'),
       (2, 'Request for password reset', 'support', 1, 2, '2023-09-02'),
       (3, 'Feature request for new dashboard', 'feature', 0, 3, '2023-09-03'),
       (4, 'Unable to access account', 'bug', 1, 4, '2023-09-04'),
       (5, 'Inquiry about pricing plans', 'support', 1, 5, '2023-09-05'),
       (6, 'Data sync problem', 'bug', 0, 6, '2023-09-06'),
       (7, 'Request for user account deletion', 'support', 1, 7, '2023-09-07'),
       (8, 'Suggestion for improving UI', 'feature', 0, 8, '2023-09-08'),
       (9, 'Application crash on load', 'bug', 1, 9, '2023-09-09'),
       (10, 'Problem with data export', 'bug', 1, 10, '2023-09-10'),
       (14, 'Inquiry about API limits', 'support', 0, 14, '2023-09-14'),
       (15, 'Feature request for notifications', 'feature', 0, 15, '2023-09-15'),
       (16, 'Login timeout error', 'bug', 0, 16, '2023-09-16'),
       (17, 'Issue with report generation', 'bug', 0, 17, '2023-09-17'),
       (18, 'Request for additional storage', 'support', 0, 18, '2023-09-18'),
       (19, 'Feedback on performance improvements', 'feature', 0, 19, '2023-09-19'),
       (20, 'Support request for account recovery', 'support', 0, 20, '2023-09-20'),
       (29, 'jczx', 'support', 1, 3, '2024-09-30'),
       (31, 'czxc', 'support', 1, 6, '2024-09-30'),
       (40, 'dxg', 'support', 0, 26, '2024-10-01'),
       (50, 'zc', 'support', 1, 28, '2024-10-01'),
       (51, 'My bug Ticket', 'bug', 1, 26, '2024-10-01'),
       (52, 'My New Ticket for Hamid', 'feature', 1, 19, '2024-10-02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `FK_client` (`client_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT,
  AUTO_INCREMENT = 29;

--
-- AUTO_INCREMENT for table `ticket`
--
ALTER TABLE `ticket`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT,
  AUTO_INCREMENT = 53;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `FK_client` FOREIGN KEY (`client_id`) REFERENCES `client` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
