-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: car_showroom
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

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
-- Table structure for table `car_name`
--

DROP TABLE IF EXISTS `car_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_name` (
  `car_name` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  `model_type` int NOT NULL,
  `car_price` int DEFAULT NULL,
  `sell_price` int DEFAULT NULL,
  `car_no` int NOT NULL,
  PRIMARY KEY (`car_no`),
  UNIQUE KEY `car_name` (`car_name`),
  KEY `model_type` (`model_type`),
  CONSTRAINT `car_name_ibfk_1` FOREIGN KEY (`model_type`) REFERENCES `car_type` (`carcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_name`
--

LOCK TABLES `car_name` WRITE;
/*!40000 ALTER TABLE `car_name` DISABLE KEYS */;
/*!40000 ALTER TABLE `car_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_type`
--

DROP TABLE IF EXISTS `car_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_type` (
  `carcode` int NOT NULL,
  `carname` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`carcode`),
  UNIQUE KEY `carname` (`carname`),
  CONSTRAINT `car_type_chk_1` CHECK (((`carcode` % 100) = 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_type`
--

LOCK TABLES `car_type` WRITE;
/*!40000 ALTER TABLE `car_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `car_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cust_no` int NOT NULL,
  `cust_name` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  `phone_no` bigint NOT NULL,
  `adderess` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cust_no`),
  UNIQUE KEY `phone_no` (`phone_no`),
  CONSTRAINT `customer_chk_1` CHECK ((`phone_no` > 6000000000))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_no` int NOT NULL AUTO_INCREMENT,
  `emp_name` varchar(30) COLLATE utf8mb3_unicode_ci NOT NULL,
  `dob` date DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `job_code` int DEFAULT NULL,
  `user_id` varchar(10) COLLATE utf8mb3_unicode_ci NOT NULL,
  `passwd` varchar(10) COLLATE utf8mb3_unicode_ci NOT NULL,
  `role` varchar(10) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`emp_no`),
  KEY `job_code` (`job_code`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`job_code`) REFERENCES `job` (`job_code`)
) ENGINE=InnoDB AUTO_INCREMENT=1004 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `job_code` int NOT NULL,
  `job_name` varchar(15) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`job_code`),
  CONSTRAINT `job_chk_1` CHECK ((`salary` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profit_loss`
--

DROP TABLE IF EXISTS `profit_loss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profit_loss` (
  `total_profit` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profit_loss`
--

LOCK TABLES `profit_loss` WRITE;
/*!40000 ALTER TABLE `profit_loss` DISABLE KEYS */;
/*!40000 ALTER TABLE `profit_loss` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sell2`
--

DROP TABLE IF EXISTS `sell2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sell2` (
  `statecode` varchar(2) COLLATE utf8mb3_unicode_ci NOT NULL,
  `districtcode` int NOT NULL,
  `serialcode` varchar(2) COLLATE utf8mb3_unicode_ci NOT NULL,
  `serialno` int NOT NULL,
  `car_no` int NOT NULL,
  `cust_no` int NOT NULL,
  `sell_date` date NOT NULL,
  PRIMARY KEY (`statecode`,`districtcode`,`serialcode`,`serialno`),
  KEY `car_no` (`car_no`),
  KEY `cust_no` (`cust_no`),
  CONSTRAINT `sell2_ibfk_1` FOREIGN KEY (`car_no`) REFERENCES `car_name` (`car_no`),
  CONSTRAINT `sell2_ibfk_2` FOREIGN KEY (`cust_no`) REFERENCES `customer` (`cust_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sell2`
--

LOCK TABLES `sell2` WRITE;
/*!40000 ALTER TABLE `sell2` DISABLE KEYS */;
/*!40000 ALTER TABLE `sell2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock`
--

DROP TABLE IF EXISTS `stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `car_no` int NOT NULL,
  `stock_left` int DEFAULT NULL,
  PRIMARY KEY (`sno`),
  UNIQUE KEY `sno` (`sno`),
  KEY `car_no` (`car_no`),
  CONSTRAINT `stock_ibfk_1` FOREIGN KEY (`car_no`) REFERENCES `car_name` (`car_no`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock`
--

LOCK TABLES `stock` WRITE;
/*!40000 ALTER TABLE `stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-03 21:12:15
