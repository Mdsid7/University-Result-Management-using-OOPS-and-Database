-- MariaDB dump 10.17  Distrib 10.5.5-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: result
-- ------------------------------------------------------
-- Server version	10.5.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `A_section`
--

DROP TABLE IF EXISTS `A_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `A_section` (
  `Name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `USN` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Class` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT '5thsem',
  `Section` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DBMS` int(11) DEFAULT NULL,
  `ADA` int(11) DEFAULT NULL,
  `OOP` int(11) DEFAULT NULL,
  `DSA` int(11) DEFAULT NULL,
  `OS` int(11) DEFAULT NULL,
  `SE` int(11) DEFAULT NULL,
  `Average` int(11) DEFAULT NULL,
  `Grade` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SGPA` float DEFAULT NULL,
  PRIMARY KEY (`USN`),
  UNIQUE KEY `USN` (`USN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `A_section`
--

LOCK TABLES `A_section` WRITE;
/*!40000 ALTER TABLE `A_section` DISABLE KEYS */;
INSERT INTO `A_section` VALUES ('Sid','ENG18CS0171','5thsem','CSE A',99,94,96,88,90,88,94,'O',9.1),('Shahabaaz','ENG18CS0172','5thsem','CSE A',98,92,93,96,95,90,96,'O',9.6),('Sudarshan','ENG18CS0173','5thsem','CSE A',91,87,98,85,92,81,93,'O',9.2);
/*!40000 ALTER TABLE `A_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `B_section`
--

DROP TABLE IF EXISTS `B_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `B_section` (
  `Name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `USN` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Class` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT '5thsem',
  `Section` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DBMS` int(11) DEFAULT NULL,
  `ADA` int(11) DEFAULT NULL,
  `OOP` int(11) DEFAULT NULL,
  `DSA` int(11) DEFAULT NULL,
  `OS` int(11) DEFAULT NULL,
  `SE` int(11) DEFAULT NULL,
  `Average` int(11) DEFAULT NULL,
  `Grade` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SGPA` float DEFAULT NULL,
  UNIQUE KEY `USN` (`USN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `B_section`
--

LOCK TABLES `B_section` WRITE;
/*!40000 ALTER TABLE `B_section` DISABLE KEYS */;
INSERT INTO `B_section` VALUES ('Kashif','ENG18CS0271','5thsem','CSE B',75,80,85,90,82,93,83,'A+',8.2),('Usman','ENG18CS0272','5thsem','CSE B',65,83,59,81,92,66,79,'A',7.9),('Mubarak','ENG18CS0273','5thsem','CSE B',59,63,72,86,77,62,68,'B+',6.8);
/*!40000 ALTER TABLE `B_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `C_section`
--

DROP TABLE IF EXISTS `C_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `C_section` (
  `Name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `USN` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Class` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT '5thsem',
  `Section` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `DBMS` int(11) DEFAULT NULL,
  `ADA` int(11) DEFAULT NULL,
  `OOP` int(11) DEFAULT NULL,
  `DSA` int(11) DEFAULT NULL,
  `OS` int(11) DEFAULT NULL,
  `SE` int(11) DEFAULT NULL,
  `Average` int(11) DEFAULT NULL,
  `Grade` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `SGPA` float DEFAULT NULL,
  UNIQUE KEY `USN` (`USN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `C_section`
--

LOCK TABLES `C_section` WRITE;
/*!40000 ALTER TABLE `C_section` DISABLE KEYS */;
INSERT INTO `C_section` VALUES ('Saquib','ENG18CS0371','5thsem','CSE C',90,93,89,99,93,94,93,'O',9.3),('Sabir','ENG18CS0372','5thsem','CSE C',90,85,84,90,73,76,80,'A+',8),('Maaz','ENG18CS0373','5thsem','CSE C',54,38,34,40,22,42,55,'E',5.5);
/*!40000 ALTER TABLE `C_section` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-05 11:56:35
