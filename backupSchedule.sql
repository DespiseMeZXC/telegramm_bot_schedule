-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: schedule
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `infoschedule`
--

DROP TABLE IF EXISTS `infoschedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `infoschedule` (
  `kafter` varchar(20) DEFAULT NULL,
  `group_kafter` varchar(20) DEFAULT NULL,
  `course` int DEFAULT NULL,
  `schedule` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `infoschedule`
--

LOCK TABLES `infoschedule` WRITE;
/*!40000 ALTER TABLE `infoschedule` DISABLE KEYS */;
INSERT INTO `infoschedule` VALUES ('forest','ММ',1,'Очень важное ММ forest'),('build','ПГС',1,'Очень важное ПГС build'),('it','ЭБ',1,'Привет\nпока \nыыфвфыв'),('build','ПГС',2,'Расписание для 2 курса'),('it','ЭБ',2,'Привет\nпока \nыыфвфыв'),('forest','ММ',2,'Привет\nпока \nыыфвфыв'),('forest','САТ',1,'Привет\nпока \nыыфвфыв'),('it','ИСТ',4,'неделя 1\nпонедельник:\nфывфы\nВЫ\nнеделя 2 \nпонедельник \nпары'),('build','ПСК',3,'Исты расписание\n\n'),('it','ИВТ',3,'Крутое расписание ИВТ\n');
/*!40000 ALTER TABLE `infoschedule` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-03 13:44:44
