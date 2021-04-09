-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 09, 2021 at 09:48 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

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
-- Table structure for table `donor`
--

CREATE TABLE `donor` (
  `did` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `bg` varchar(5) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `disease` varchar(5) DEFAULT NULL,
  `vac` varchar(5) DEFAULT NULL,
  `ldd` date DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donor`
--

INSERT INTO `donor` (`did`, `name`, `gender`, `bg`, `dob`, `phone`, `disease`, `vac`, `ldd`, `area`) VALUES
(3, 'Sharif Ahamed', 'Male', 'A+', '1998-09-03', '01852395428', 'No', 'No', '2020-12-24', 'Dhanmondi'),
(5, 'Awlad Hossain', 'Male', 'O+', '1998-12-23', '01485425545', 'No', 'Yes', '1900-01-01', 'Dhanmondi'),
(6, 'Nafiz Ahmed Emon', 'Male', 'A+', '1999-01-09', '0148554545', 'No', 'No', '2021-05-12', 'Dhanmondi'),
(8, 'Hafiz Ahmed Khan', 'Male', 'O+', '1998-12-16', '014854545478', 'No', 'No', '2019-12-11', 'Dhanmondi'),
(9, 'David', 'Male', 'A+', '1994-08-24', '01485425599', 'No', 'No', '2021-06-09', 'Dhanmondi'),
(11, 'Fakar Zaman', 'Male', 'AB-', '2001-08-30', '014854255460001', 'No', 'No', '1900-01-01', 'Khilgaon'),
(12, 'Ayesha', 'Female', 'O+', '2000-03-23', '01485400045', 'Yes', 'No', '1900-01-01', 'Dhanmondi'),
(15, 'Xavier', 'Male', 'A+', '1986-01-23', '0169696969', 'No', 'No', '1900-01-01', 'Dhanmondi'),
(16, 'Kaniz', 'Female', 'AB+', '1999-04-21', '0174584554', 'No', 'No', '1900-01-01', 'Khilkhet'),
(17, 'Jamal', 'Male', 'B+', '1985-01-29', '0147542845', 'No', 'No', '2020-10-21', 'Dhanmondi'),
(18, 'Erick', 'Male', 'O+', '2001-05-16', '014584254226', 'No', 'Yes', '1900-01-01', 'Khilkhet'),
(19, 'Kal El', 'Male', 'O-', '1981-05-20', '014562642214', 'No', 'No', '2008-01-23', 'Mirpur'),
(20, 'Rose', 'Female', 'A+', '2004-04-23', '01484564455', 'No', 'No', '1900-01-01', 'Dhanmondi'),
(21, 'Sanju Bhuiyan', 'Female', 'O+', '1999-02-10', '0148452456554', 'No', 'No', '1900-01-01', 'Uttora'),
(22, 'Santa Mariam', 'Female', 'AB+', '2000-05-31', '014895465884', 'Yes', 'No', '2020-10-22', 'Uttora'),
(23, 'Ashiqur Zaman', 'Male', 'A-', '1996-11-19', '0146546954787', 'No', 'No', '1900-01-01', 'Mirpur'),
(24, 'Maria', 'Female', 'O+', '2002-04-17', '016546546541', 'No', 'No', '1900-01-01', 'Uttora'),
(25, 'Fatema', 'Female', 'A+', '1998-06-17', '00154564245', 'No', 'No', '2019-12-18', 'Dhanmondi'),
(26, 'Maliha', 'Female', 'A+', '2000-11-29', '019546545621', 'No', 'No', '1900-01-01', 'Dhanmondi'),
(27, 'Zihan', 'Male', 'O+', '2000-01-01', '01845646545641', 'No', 'No', '1900-01-01', 'Uttora');

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `reid` int(11) NOT NULL,
  `rid` int(11) DEFAULT NULL,
  `did` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`reid`, `rid`, `did`) VALUES
(2, 3, 3),
(29, 29, 15),
(32, 32, 24),
(33, 33, 17),
(34, 34, 8);

-- --------------------------------------------------------

--
-- Table structure for table `requester`
--

CREATE TABLE `requester` (
  `rid` int(11) NOT NULL,
  `pname` varchar(50) DEFAULT NULL,
  `pbg` varchar(5) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `needed_blood_date` date DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `hospital` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `requester`
--

INSERT INTO `requester` (`rid`, `pname`, `pbg`, `phone`, `needed_blood_date`, `area`, `hospital`) VALUES
(3, 'Akil Khan', 'A+', '01752342542', '2021-04-12', 'Dhanmondi', 'United Hospital'),
(29, 'David', 'A+', '0169696969', '2035-01-24', 'Dhanmondi', 'Apollo Hospital'),
(30, 'Anis', 'O+', '01545454654', '2023-05-17', 'Khilgaon', 'United Hospital'),
(31, 'Awlad', 'O-', '0145424125', '2023-04-12', 'Khilgaon', 'Squire Hospital'),
(32, 'Rifat Islam', 'O+', '0189756454564', '2021-06-16', 'Uttora', 'Apollo Hospital'),
(33, 'Sifat', 'B+', '01654564654', '2021-08-03', 'Dhanmondi', 'United Hospital'),
(34, 'Liza', 'O+', '01654654565', '2021-08-04', 'Dhanmondi', 'Squire Hospital');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `donor`
--
ALTER TABLE `donor`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`reid`),
  ADD KEY `rid` (`rid`),
  ADD KEY `did` (`did`);

--
-- Indexes for table `requester`
--
ALTER TABLE `requester`
  ADD PRIMARY KEY (`rid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `donor`
--
ALTER TABLE `donor`
  MODIFY `did` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `record`
--
ALTER TABLE `record`
  MODIFY `reid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `requester`
--
ALTER TABLE `requester`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `record`
--
ALTER TABLE `record`
  ADD CONSTRAINT `record_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `requester` (`rid`),
  ADD CONSTRAINT `record_ibfk_2` FOREIGN KEY (`did`) REFERENCES `donor` (`did`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
