-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2021 at 11:03 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blood`
--

-- --------------------------------------------------------

--
-- Table structure for table `blood_requester`
--

CREATE TABLE `blood_requester` (
  `fname` varchar(11) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `blood_group` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `BND` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `hospital` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blood_requester`
--

INSERT INTO `blood_requester` (`fname`, `lname`, `gender`, `blood_group`, `age`, `BND`, `contact`, `hospital`) VALUES
('E', 'F', 'Male', 'B+', '30', '12-04-2020', '01712345670', 'C'),
('A', 'B', 'Male', 'O+', '30', '12-04-2020', '01712345678', 'A'),
('C', 'D', 'Female', 'A+', '40', '12-04-2020', '01712345679', 'B');

-- --------------------------------------------------------

--
-- Table structure for table `donor_information`
--

CREATE TABLE `donor_information` (
  `fname` varchar(11) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `blood_group` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `ldd` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donor_information`
--

INSERT INTO `donor_information` (`fname`, `lname`, `gender`, `blood_group`, `age`, `ldd`, `contact`, `address`) VALUES
('Nafiz', 'Ahmed', 'Male', 'B+', '23', '27-12-2019', '01611234050', 'Dhanmondi\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
('Awlad', 'Hossen', 'Male', 'AB+', '24', '26-12-2019', '01611234070', 'Old Dhaka\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'),
('Kaniz', 'Fatema', 'Female', 'O-', '23', '28-12-2019', '01686125156', 'Savar\n'),
('Hafiz', 'Ahmed', 'Male', 'O+', '23', '27-12-2019', '01781189660', 'Mirpur\n'),
('Sharif', 'Ahmed', 'Male', 'A+', '23', '26-12-2019', '01852395428', 'Mirpur\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `donation_date` varchar(20) NOT NULL,
  `requester_contact_no` varchar(20) DEFAULT NULL,
  `donor_contact_no` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`donation_date`, `requester_contact_no`, `donor_contact_no`) VALUES
('15-04-2021', '01712345678', '01611234070');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blood_requester`
--
ALTER TABLE `blood_requester`
  ADD PRIMARY KEY (`contact`);

--
-- Indexes for table `donor_information`
--
ALTER TABLE `donor_information`
  ADD PRIMARY KEY (`contact`);

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`donation_date`),
  ADD KEY `requester_contact_no` (`requester_contact_no`),
  ADD KEY `donor_contact_no` (`donor_contact_no`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `record`
--
ALTER TABLE `record`
  ADD CONSTRAINT `record_ibfk_1` FOREIGN KEY (`requester_contact_no`) REFERENCES `blood_requester` (`contact`),
  ADD CONSTRAINT `record_ibfk_2` FOREIGN KEY (`donor_contact_no`) REFERENCES `donor_information` (`contact`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
