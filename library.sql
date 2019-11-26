-- MySQL dump 10.13  Distrib 8.0.18, for osx10.13 (x86_64)
--
-- Host: localhost    Database: LIBRARY
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `LIBRARY`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `LIBRARY` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `LIBRARY`;

--
-- Table structure for table `AUTHORIZATION_SYSTEM`
--

DROP TABLE IF EXISTS `AUTHORIZATION_SYSTEM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AUTHORIZATION_SYSTEM` (
  `EmployeeID` char(2) NOT NULL,
  `Username` varchar(15) NOT NULL,
  `Password` varchar(15) NOT NULL,
  PRIMARY KEY (`EmployeeID`,`Username`),
  CONSTRAINT `authorization_system_ibfk_1` FOREIGN KEY (`EmployeeID`) REFERENCES `employee_information` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AUTHORIZATION_SYSTEM`
--

LOCK TABLES `AUTHORIZATION_SYSTEM` WRITE;
/*!40000 ALTER TABLE `AUTHORIZATION_SYSTEM` DISABLE KEYS */;
INSERT INTO `AUTHORIZATION_SYSTEM` VALUES ('E1','ankit11','pa$$word'),('E2','sahilK','SahiL123'),('E3','um@ng','umangpwd');
/*!40000 ALTER TABLE `AUTHORIZATION_SYSTEM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BOOK_INFORMATION`
--

DROP TABLE IF EXISTS `BOOK_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BOOK_INFORMATION` (
  `BookID` varchar(10) NOT NULL,
  `BookTitle` varchar(15) NOT NULL,
  `Author` varchar(15) NOT NULL,
  PRIMARY KEY (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BOOK_INFORMATION`
--

LOCK TABLES `BOOK_INFORMATION` WRITE;
/*!40000 ALTER TABLE `BOOK_INFORMATION` DISABLE KEYS */;
INSERT INTO `BOOK_INFORMATION` VALUES ('1','Life','Paul'),('2','Honesty','Joey'),('3','Fun','Karp');
/*!40000 ALTER TABLE `BOOK_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BRANCH_INFORMATION`
--

DROP TABLE IF EXISTS `BRANCH_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BRANCH_INFORMATION` (
  `BranchID` varchar(2) NOT NULL,
  `Address` varchar(30) NOT NULL,
  PRIMARY KEY (`BranchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BRANCH_INFORMATION`
--

LOCK TABLES `BRANCH_INFORMATION` WRITE;
/*!40000 ALTER TABLE `BRANCH_INFORMATION` DISABLE KEYS */;
INSERT INTO `BRANCH_INFORMATION` VALUES ('B1','ghj'),('B2','abx'),('B3','xyz');
/*!40000 ALTER TABLE `BRANCH_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CONTACT_INFORMATION`
--

DROP TABLE IF EXISTS `CONTACT_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CONTACT_INFORMATION` (
  `RollNumber` char(10) NOT NULL,
  `ContactNumber` char(10) NOT NULL,
  PRIMARY KEY (`ContactNumber`,`RollNumber`),
  KEY `RollNumber` (`RollNumber`),
  CONSTRAINT `contact_information_ibfk_1` FOREIGN KEY (`RollNumber`) REFERENCES `student_information` (`RollNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CONTACT_INFORMATION`
--

LOCK TABLES `CONTACT_INFORMATION` WRITE;
/*!40000 ALTER TABLE `CONTACT_INFORMATION` DISABLE KEYS */;
INSERT INTO `CONTACT_INFORMATION` VALUES ('2019101001','9567541256'),('2019101001','9876578765'),('2019101002','9437987613'),('2019101003','9640098112');
/*!40000 ALTER TABLE `CONTACT_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COPIES_IN`
--

DROP TABLE IF EXISTS `COPIES_IN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COPIES_IN` (
  `BookID` varchar(10) NOT NULL,
  `BranchID` char(2) NOT NULL,
  `TotalCopies` int(10) NOT NULL,
  `AvailableCopies` int(10) NOT NULL,
  PRIMARY KEY (`BookID`,`BranchID`),
  KEY `BranchID` (`BranchID`),
  CONSTRAINT `copies_in_ibfk_1` FOREIGN KEY (`BookID`) REFERENCES `book_information` (`BookID`),
  CONSTRAINT `copies_in_ibfk_2` FOREIGN KEY (`BranchID`) REFERENCES `branch_information` (`BranchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COPIES_IN`
--

LOCK TABLES `COPIES_IN` WRITE;
/*!40000 ALTER TABLE `COPIES_IN` DISABLE KEYS */;
INSERT INTO `COPIES_IN` VALUES ('1','B1',5,5),('1','B2',9,9),('2','B2',3,3);
/*!40000 ALTER TABLE `COPIES_IN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMPLOYEE_INFORMATION`
--

DROP TABLE IF EXISTS `EMPLOYEE_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EMPLOYEE_INFORMATION` (
  `Name` varchar(15) NOT NULL,
  `StaffID` char(2) NOT NULL,
  `BranchID` char(2) NOT NULL,
  PRIMARY KEY (`StaffID`),
  KEY `BranchID` (`BranchID`),
  CONSTRAINT `employee_information_ibfk_1` FOREIGN KEY (`BranchID`) REFERENCES `branch_information` (`BranchID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE_INFORMATION`
--

LOCK TABLES `EMPLOYEE_INFORMATION` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE_INFORMATION` DISABLE KEYS */;
INSERT INTO `EMPLOYEE_INFORMATION` VALUES ('Ankit','E1','B1'),('Sahil','E2','B1'),('Umang','E3','B2');
/*!40000 ALTER TABLE `EMPLOYEE_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ISSUE`
--

DROP TABLE IF EXISTS `ISSUE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ISSUE` (
  `RollNumber` char(10) NOT NULL,
  `StaffID` char(2) NOT NULL,
  `BranchID` char(2) NOT NULL,
  `BookID` varchar(10) NOT NULL,
  `IssueTime` datetime NOT NULL,
  PRIMARY KEY (`IssueTime`,`RollNumber`,`StaffID`,`BranchID`,`BookID`),
  KEY `RollNumber` (`RollNumber`),
  KEY `StaffID` (`StaffID`),
  KEY `BranchID` (`BranchID`),
  KEY `BookID` (`BookID`),
  CONSTRAINT `issue_ibfk_1` FOREIGN KEY (`RollNumber`) REFERENCES `student_information` (`RollNumber`),
  CONSTRAINT `issue_ibfk_2` FOREIGN KEY (`StaffID`) REFERENCES `employee_information` (`StaffID`),
  CONSTRAINT `issue_ibfk_3` FOREIGN KEY (`BranchID`) REFERENCES `branch_information` (`BranchID`),
  CONSTRAINT `issue_ibfk_4` FOREIGN KEY (`BookID`) REFERENCES `book_information` (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ISSUE`
--

LOCK TABLES `ISSUE` WRITE;
/*!40000 ALTER TABLE `ISSUE` DISABLE KEYS */;
INSERT INTO `ISSUE` VALUES ('2019101001','E1','B1','1','2019-10-10 13:00:00'),('2019101002','E2','B1','1','2019-10-10 00:00:00'),('2019101003','E3','B2','1','2019-10-10 20:00:00');
/*!40000 ALTER TABLE `ISSUE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MAINTAINER_INFORMATION`
--

DROP TABLE IF EXISTS `MAINTAINER_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MAINTAINER_INFORMATION` (
  `Name` varchar(15) NOT NULL,
  `StaffID` char(2) NOT NULL,
  PRIMARY KEY (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MAINTAINER_INFORMATION`
--

LOCK TABLES `MAINTAINER_INFORMATION` WRITE;
/*!40000 ALTER TABLE `MAINTAINER_INFORMATION` DISABLE KEYS */;
INSERT INTO `MAINTAINER_INFORMATION` VALUES ('Paras','M1'),('Akshat','M2'),('Manas','M3');
/*!40000 ALTER TABLE `MAINTAINER_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PARENT_INFORMATION`
--

DROP TABLE IF EXISTS `PARENT_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PARENT_INFORMATION` (
  `SRollNumber` char(10) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `ContactNumber` char(10) NOT NULL,
  `Gender` char(1) NOT NULL,
  PRIMARY KEY (`SRollNumber`,`Name`),
  CONSTRAINT `parent_information_ibfk_1` FOREIGN KEY (`SRollNumber`) REFERENCES `student_information` (`RollNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PARENT_INFORMATION`
--

LOCK TABLES `PARENT_INFORMATION` WRITE;
/*!40000 ALTER TABLE `PARENT_INFORMATION` DISABLE KEYS */;
INSERT INTO `PARENT_INFORMATION` VALUES ('2019101001','Rakesh','1234567890','M'),('2019101002','Manish','1243567809','M'),('2019101003','Ajay','9087654312','M');
/*!40000 ALTER TABLE `PARENT_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RETURN`
--

DROP TABLE IF EXISTS `RETURN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RETURN` (
  `RollNumber` char(15) NOT NULL,
  `StaffID` char(2) NOT NULL,
  `BranchID` char(2) NOT NULL,
  `BookID` varchar(10) NOT NULL,
  `ReturnTime` datetime NOT NULL,
  PRIMARY KEY (`ReturnTime`,`RollNumber`,`StaffID`,`BranchID`,`BookID`),
  KEY `RollNumber` (`RollNumber`),
  KEY `StaffID` (`StaffID`),
  KEY `BranchID` (`BranchID`),
  KEY `BookID` (`BookID`),
  CONSTRAINT `return_ibfk_1` FOREIGN KEY (`RollNumber`) REFERENCES `student_information` (`RollNumber`),
  CONSTRAINT `return_ibfk_2` FOREIGN KEY (`StaffID`) REFERENCES `employee_information` (`StaffID`),
  CONSTRAINT `return_ibfk_3` FOREIGN KEY (`BranchID`) REFERENCES `branch_information` (`BranchID`),
  CONSTRAINT `return_ibfk_4` FOREIGN KEY (`BookID`) REFERENCES `book_information` (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RETURN`
--

LOCK TABLES `RETURN` WRITE;
/*!40000 ALTER TABLE `RETURN` DISABLE KEYS */;
INSERT INTO `RETURN` VALUES ('2019101001','E1','B1','1','2019-10-10 12:00:00'),('2019101002','E2','B1','1','2019-10-10 08:00:00'),('2019101003','E3','B2','1','2019-10-10 10:00:00');
/*!40000 ALTER TABLE `RETURN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STUDENT_INFORMATION`
--

DROP TABLE IF EXISTS `STUDENT_INFORMATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STUDENT_INFORMATION` (
  `FirstName` varchar(15) NOT NULL,
  `LastName` varchar(15) NOT NULL,
  `EmailID` varchar(30) NOT NULL,
  `RollNumber` char(10) NOT NULL,
  PRIMARY KEY (`RollNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STUDENT_INFORMATION`
--

LOCK TABLES `STUDENT_INFORMATION` WRITE;
/*!40000 ALTER TABLE `STUDENT_INFORMATION` DISABLE KEYS */;
INSERT INTO `STUDENT_INFORMATION` VALUES ('Karan','Sharma','karan.sharma@gmail.com','2019101001'),('Arvind','Kumar','arvind.kumar@gmail.com','2019101002'),('Shefali','Singh','shefali.singh@gmail.com','2019101003');
/*!40000 ALTER TABLE `STUDENT_INFORMATION` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-13  9:33:46
