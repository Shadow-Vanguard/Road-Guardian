-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 20, 2024 at 08:01 PM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `new_roadside_assistance`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Custom User', 6, 'add_customuser'),
(22, 'Can change Custom User', 6, 'change_customuser'),
(23, 'Can delete Custom User', 6, 'delete_customuser'),
(24, 'Can view Custom User', 6, 'view_customuser'),
(25, 'Can add service type', 7, 'add_servicetype'),
(26, 'Can change service type', 7, 'change_servicetype'),
(27, 'Can delete service type', 7, 'delete_servicetype'),
(28, 'Can view service type', 7, 'view_servicetype'),
(29, 'Can add service provider', 8, 'add_serviceprovider'),
(30, 'Can change service provider', 8, 'change_serviceprovider'),
(31, 'Can delete service provider', 8, 'delete_serviceprovider'),
(32, 'Can view service provider', 8, 'view_serviceprovider'),
(33, 'Can add workshop service', 9, 'add_workshopservice'),
(34, 'Can change workshop service', 9, 'change_workshopservice'),
(35, 'Can delete workshop service', 9, 'delete_workshopservice'),
(36, 'Can view workshop service', 9, 'view_workshopservice'),
(37, 'Can add fuel type', 10, 'add_fueltype'),
(38, 'Can change fuel type', 10, 'change_fueltype'),
(39, 'Can delete fuel type', 10, 'delete_fueltype'),
(40, 'Can view fuel type', 10, 'view_fueltype'),
(41, 'Can add ambulance type', 11, 'add_ambulancetype'),
(42, 'Can change ambulance type', 11, 'change_ambulancetype'),
(43, 'Can delete ambulance type', 11, 'delete_ambulancetype'),
(44, 'Can view ambulance type', 11, 'view_ambulancetype'),
(45, 'Can add towing service', 12, 'add_towingservice'),
(46, 'Can change towing service', 12, 'change_towingservice'),
(47, 'Can delete towing service', 12, 'delete_towingservice'),
(48, 'Can view towing service', 12, 'view_towingservice'),
(49, 'Can add ambulance service', 13, 'add_ambulanceservice'),
(50, 'Can change ambulance service', 13, 'change_ambulanceservice'),
(51, 'Can delete ambulance service', 13, 'delete_ambulanceservice'),
(52, 'Can view ambulance service', 13, 'view_ambulanceservice'),
(53, 'Can add towing type', 14, 'add_towingtype'),
(54, 'Can change towing type', 14, 'change_towingtype'),
(55, 'Can delete towing type', 14, 'delete_towingtype'),
(56, 'Can view towing type', 14, 'view_towingtype'),
(57, 'Can add workshop service provider', 15, 'add_workshopserviceprovider'),
(58, 'Can change workshop service provider', 15, 'change_workshopserviceprovider'),
(59, 'Can delete workshop service provider', 15, 'delete_workshopserviceprovider'),
(60, 'Can view workshop service provider', 15, 'view_workshopserviceprovider'),
(61, 'Can add vehicle', 16, 'add_vehicle'),
(62, 'Can change vehicle', 16, 'change_vehicle'),
(63, 'Can delete vehicle', 16, 'delete_vehicle'),
(64, 'Can view vehicle', 16, 'view_vehicle'),
(65, 'Can add petrol bunk service', 17, 'add_petrolbunkservice'),
(66, 'Can change petrol bunk service', 17, 'change_petrolbunkservice'),
(67, 'Can delete petrol bunk service', 17, 'delete_petrolbunkservice'),
(68, 'Can view petrol bunk service', 17, 'view_petrolbunkservice'),
(69, 'Can add service type category', 18, 'add_servicetypecategory'),
(70, 'Can change service type category', 18, 'change_servicetypecategory'),
(71, 'Can delete service type category', 18, 'delete_servicetypecategory'),
(72, 'Can view service type category', 18, 'view_servicetypecategory'),
(73, 'Can add booking', 19, 'add_booking'),
(74, 'Can change booking', 19, 'change_booking'),
(75, 'Can delete booking', 19, 'delete_booking'),
(76, 'Can view booking', 19, 'view_booking'),
(77, 'Can add feedback', 20, 'add_feedback'),
(78, 'Can change feedback', 20, 'change_feedback'),
(79, 'Can delete feedback', 20, 'delete_feedback'),
(80, 'Can view feedback', 20, 'view_feedback');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'roadside_app', 'customuser'),
(7, 'roadside_app', 'servicetype'),
(8, 'roadside_app', 'serviceprovider'),
(9, 'roadside_app', 'workshopservice'),
(10, 'roadside_app', 'fueltype'),
(11, 'roadside_app', 'ambulancetype'),
(12, 'roadside_app', 'towingservice'),
(13, 'roadside_app', 'ambulanceservice'),
(14, 'roadside_app', 'towingtype'),
(15, 'roadside_app', 'workshopserviceprovider'),
(16, 'roadside_app', 'vehicle'),
(17, 'roadside_app', 'petrolbunkservice'),
(18, 'roadside_app', 'servicetypecategory'),
(19, 'roadside_app', 'booking'),
(20, 'roadside_app', 'feedback');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-19 05:16:59.461646'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-10-19 05:16:59.511436'),
(3, 'auth', '0001_initial', '2024-10-19 05:16:59.657444'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-10-19 05:16:59.680984'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-10-19 05:16:59.691868'),
(6, 'auth', '0004_alter_user_username_opts', '2024-10-19 05:16:59.695709'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-10-19 05:16:59.699089'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-10-19 05:16:59.700608'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-10-19 05:16:59.706598'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-10-19 05:16:59.710064'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-10-19 05:16:59.714676'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-10-19 05:16:59.737003'),
(13, 'auth', '0011_update_proxy_permissions', '2024-10-19 05:16:59.741985'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-10-19 05:16:59.745982'),
(15, 'roadside_app', '0001_initial', '2024-10-19 05:16:59.916203'),
(16, 'admin', '0001_initial', '2024-10-19 05:17:00.080438'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-10-19 05:17:00.089603'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-19 05:17:00.093453'),
(19, 'roadside_app', '0002_servicetype_alter_customuser_email_and_more', '2024-10-19 05:17:00.224422'),
(20, 'sessions', '0001_initial', '2024-10-19 05:17:00.257200'),
(21, 'roadside_app', '0003_ambulancetype_fueltype_towingtype_vehicle_and_more', '2024-10-19 06:14:41.504425'),
(22, 'roadside_app', '0004_remove_ambulanceservice_ambulance_types_and_more', '2024-10-19 07:27:16.011849'),
(23, 'roadside_app', '0005_alter_servicetype_image', '2024-10-19 07:43:46.021669'),
(24, 'roadside_app', '0006_alter_servicetype_image', '2024-10-19 07:43:46.063268'),
(25, 'roadside_app', '0007_alter_servicetype_image', '2024-10-19 07:43:46.091270'),
(26, 'roadside_app', '0008_alter_servicetype_image', '2024-10-19 12:20:04.774430'),
(27, 'roadside_app', '0009_servicetypecategory', '2024-10-20 13:06:44.227723'),
(28, 'roadside_app', '0010_remove_servicetypecategory_price', '2024-10-20 13:57:30.676793'),
(29, 'roadside_app', '0011_booking', '2024-10-20 14:34:21.268456'),
(30, 'roadside_app', '0012_alter_booking_description_alter_booking_location', '2024-10-20 14:45:46.914581'),
(31, 'roadside_app', '0013_booking_status', '2024-10-20 17:40:35.899942'),
(32, 'roadside_app', '0014_alter_booking_status_feedback', '2024-10-20 19:02:00.762187'),
(33, 'roadside_app', '0015_delete_feedback', '2024-10-20 19:17:31.060251'),
(34, 'roadside_app', '0016_feedback', '2024-10-20 19:18:19.079355');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('jglf8c4pmiwyun8v2gwvk8t2r2hyupd1', '.eJxVjsEKwjAQRP8lZwnZZNs0Hr37DWWz2ZqqpNC0J_HfbaGIngZm3gzzUj2tS-7XKnM_JnVWoE6_XiR-SNmDdKdymzRPZZnHqHdEH2nV1ynJ83KwfwOZat7axBjBIAAMTedQrHOUvJXGhUCtkWYTBgcQbItdMt52hpn9gEgRfdhGvx_h_QFmGDqd:1t28a6:5V7oi0faPPDwiEbyQQedWhXvrBS0Renhrd4MecA_3QU', '2024-11-02 12:29:18.398253'),
('2qgx3bwv3ylv6xsetusn5kvy2l7xn0jz', '.eJxVjsEKwjAQRP8lZwnZZNs0Hr37DWWz2ZqqpNC0J_HfbaGIngZm3gzzUj2tS-7XKnM_JnVWoE6_XiR-SNmDdKdymzRPZZnHqHdEH2nV1ynJ83KwfwOZat7axBjBIAAMTedQrHOUvJXGhUCtkWYTBgcQbItdMt52hpn9gEgRfdhGvx_h_QFmGDqd:1t2UcB:Ya0sMhAnFQSGgFPHBIKjZiXkcXNiD-eNanX2JJRQlew', '2024-11-03 12:00:55.560911'),
('3ora0nzhez88r29tuyhaomj0ltr6jdaq', '.eJxVjs0KwjAQhN8lZwntNj-NR-8-Q0h2N6YqKTTtSXx3Uyii1_lmPuYlfNjW7LfKi59InIUWp98sBnxw2QHdQ7nNEueyLlOUe0UetMrrTPy8HN0_QQ41tzXrmHDQ0CWMmEhZRQpMb6N1jhg5Qs9gTTcq49BAsmQYNLuh4dERNOn3o35_ALtvO_U:1t2bcm:o3D1ob4QFenStPhuULHK7zKB85OVbqMcyryNSBlltJo', '2024-11-03 19:30:00.101855');

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_booking`
--

DROP TABLE IF EXISTS `roadside_app_booking`;
CREATE TABLE IF NOT EXISTS `roadside_app_booking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `location` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `service_provider_id` bigint NOT NULL,
  `service_type_category_id` int NOT NULL,
  `user_id` bigint NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roadside_app_booking_service_provider_id_1fbcf5d8` (`service_provider_id`),
  KEY `roadside_app_booking_service_type_category_id_dfd6476f` (`service_type_category_id`),
  KEY `roadside_app_booking_user_id_cca9bcac` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roadside_app_booking`
--

INSERT INTO `roadside_app_booking` (`id`, `location`, `description`, `created_at`, `service_provider_id`, `service_type_category_id`, `user_id`, `status`) VALUES
(1, 'Pampady', 'I need Tow service come fast', '2024-10-20 15:30:39.762623', 1, 1, 1, 'completed'),
(2, 'Pampady', 'I need Tow service come fast', '2024-10-20 15:33:20.584819', 1, 1, 1, 'completed'),
(3, 'kottayam', 'i need help', '2024-10-20 15:45:38.153263', 1, 2, 1, 'completed'),
(4, 'mukkada', 'help', '2024-10-20 15:47:22.215872', 1, 2, 1, 'completed'),
(5, 'Kovallam', 'i need 2 liters of petrol', '2024-10-20 19:23:16.887223', 3, 3, 1, 'completed');

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_customuser`
--

DROP TABLE IF EXISTS `roadside_app_customuser`;
CREATE TABLE IF NOT EXISTS `roadside_app_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `name` varchar(200) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(150) NOT NULL,
  `role` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `roadside_app_customuser_email_ceaf13e6` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roadside_app_customuser`
--

INSERT INTO `roadside_app_customuser` (`id`, `last_login`, `is_superuser`, `username`, `name`, `phone`, `address`, `email`, `role`, `password`, `is_active`, `is_staff`) VALUES
(1, '2024-10-20 19:24:41.585519', 0, 'rosh', 'Roshan Varghese', '9061855716', 'Valiyaveettil Mukkada', 'roshanv334@gmail.com', 'user', 'pbkdf2_sha256$870000$gJBQ4i4TwRukfSmqwWdjOG$vMv7XmJTQMik0bsRs/u3I8g8LGR3wKjb+8/diEqkhGg=', 1, 0),
(2, '2024-10-20 17:41:05.086690', 1, 'admin', 'Admin', '9874563215', 'Wizz', 'admin123@gmail.com', 'Admin', 'pbkdf2_sha256$870000$QlCkSmS6qThrKh8uSxochS$mVtcaVAx31g5wrXFHlHoyNCSxEgAR1mww3HaIzqgHC0=', 1, 0),
(3, '2024-10-20 19:20:37.316939', 0, 'ashu', 'Ashu Towing Service', '9874563212', 'Melayil Kottayam', 'ashu123@gmail.com', 'service_provider', 'pbkdf2_sha256$870000$xtdI5ZZ2JpCWhjMz5E5JTX$Ass2mUScu7UAgTmqj1MaLz+bljBa723TyR6ip+7TQJ0=', 1, 0),
(4, NULL, 0, 'marvel', 'Marvel Towing Service', '9874563215', 'Thaikudom', 'marveltowing@gmail.com', 'service_provider', 'pbkdf2_sha256$870000$syG1aIYpDQyyfYDxWALYHX$cxelOEtnAxRvHUjZ+J21PLVMqecFqSyDT6zg1ABz1f8=', 1, 0),
(5, '2024-10-20 19:30:00.100845', 0, 'bharath', 'Bharath Petroleum', '9856321236', 'Paruvanikal', 'bharathpetroleum123@gmail.com', 'service_provider', 'pbkdf2_sha256$870000$zXFG0WUGwNU3qJXlfGetNk$3FJ/MY5Y6Eo0YEw6PrUrA/3gTU4kxRddpjssXcVZcZ4=', 1, 0),
(6, NULL, 0, 'k&k', 'K And K Automobiles', '9856547859', 'Paruvanikal', 'kandkauto123@gmail.com', 'service_provider', 'pbkdf2_sha256$870000$FwurAY1TDnwXC2SYBtRuTV$j1vQTgvPLLFbK/0ATDET5QIbjWAZc9MunBGyhjKF6tk=', 1, 0),
(7, NULL, 0, 'mythri', 'Mythri Ambulance', '9874563233', 'Kallor kollam', 'Mythri123@gmail.com', 'service_provider', 'pbkdf2_sha256$870000$5nUpJ079gleqp6gjF1lPga$ioSesYu/RkBjsreemkAzJjqGhc/mq8BrPzu5qNgrTX8=', 1, 0),
(8, NULL, 0, 'jeevani', 'Jeevani Ambulance service', '9856321457', 'Thaikudom', 'jeevaniambulance123@gmail.com', 'service_provider', 'pbkdf2_sha256$870000$8ybdf9Twhz2lj7IUrm9wfn$PwLbcojXzDwv9PbFXIeDnD6c/2UC1cGc6CAJ0Tzj3Uo=', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_customuser_groups`
--

DROP TABLE IF EXISTS `roadside_app_customuser_groups`;
CREATE TABLE IF NOT EXISTS `roadside_app_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roadside_app_customuser__customuser_id_group_id_aa2c88ca_uniq` (`customuser_id`,`group_id`),
  KEY `roadside_app_customuser_groups_customuser_id_b5a47e79` (`customuser_id`),
  KEY `roadside_app_customuser_groups_group_id_ff521eb7` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_customuser_user_permissions`
--

DROP TABLE IF EXISTS `roadside_app_customuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `roadside_app_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `roadside_app_customuser__customuser_id_permission_8197d229_uniq` (`customuser_id`,`permission_id`),
  KEY `roadside_app_customuser_user_permissions_customuser_id_0172d06b` (`customuser_id`),
  KEY `roadside_app_customuser_user_permissions_permission_id_0e6972db` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_feedback`
--

DROP TABLE IF EXISTS `roadside_app_feedback`;
CREATE TABLE IF NOT EXISTS `roadside_app_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback_text` longtext NOT NULL,
  `rating` int NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `booking_id` bigint NOT NULL,
  `service_provider_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `roadside_app_feedback_booking_id_0aec163f` (`booking_id`),
  KEY `roadside_app_feedback_service_provider_id_afecfd69` (`service_provider_id`),
  KEY `roadside_app_feedback_user_id_f1f75e84` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roadside_app_feedback`
--

INSERT INTO `roadside_app_feedback` (`id`, `feedback_text`, `rating`, `timestamp`, `booking_id`, `service_provider_id`, `user_id`) VALUES
(1, 'There service was very good', 5, '2024-10-20 19:29:20.419800', 5, 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_serviceprovider`
--

DROP TABLE IF EXISTS `roadside_app_serviceprovider`;
CREATE TABLE IF NOT EXISTS `roadside_app_serviceprovider` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `certificate` varchar(100) NOT NULL,
  `area_of_service` varchar(255) NOT NULL,
  `location` longtext NOT NULL,
  `availability_status` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  `service_type_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `roadside_app_serviceprovider_service_type_id_1d74015c` (`service_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roadside_app_serviceprovider`
--

INSERT INTO `roadside_app_serviceprovider` (`id`, `certificate`, `area_of_service`, `location`, `availability_status`, `user_id`, `service_type_id`) VALUES
(1, 'certificates/class_diagram_jYluUKj.png', 'Kottayam', 'Pampady', 1, 3, 1),
(2, 'certificates/State_chart_Diagram.png', 'Ernakulam', 'Vyttila', 1, 4, 1),
(3, 'certificates/Sequence_Diagram_Vkfkt7d.png', 'Trivandrum', 'Kovallam', 1, 5, 2),
(4, 'certificates/Object_Diagram.png', 'Kollam', 'Adoor', 1, 6, 5),
(5, 'certificates/Object_Diagram_kkCBakG.png', 'Kollam', 'Kottarakara', 1, 7, 3),
(6, 'certificates/Sequence_Diagram_J5XAU6Q.png', 'Ernakulam', 'Aluva', 1, 8, 3);

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_servicetype`
--

DROP TABLE IF EXISTS `roadside_app_servicetype`;
CREATE TABLE IF NOT EXISTS `roadside_app_servicetype` (
  `servicetype_id` int NOT NULL AUTO_INCREMENT,
  `servicetype_name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`servicetype_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roadside_app_servicetype`
--

INSERT INTO `roadside_app_servicetype` (`servicetype_id`, `servicetype_name`, `description`, `image`) VALUES
(1, 'Towing Service', 'Need your vehicle towed? We\'re here 24/7!', 'service_types/towing-vehicle.png'),
(2, 'Petrol Bunk Service', 'Out of fuel? We can deliver petrol/diesel to you.', 'service_types/gas-station_Ptsbkbu.png'),
(3, 'Ambulance Service', 'Emergency medical assistance on the go.', 'service_types/ambulace1.jpg'),
(5, 'Workshop Service', 'Need vehicle repairs? Find the nearest workshops', 'service_types/repair-shop.png');

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_servicetypecategory`
--

DROP TABLE IF EXISTS `roadside_app_servicetypecategory`;
CREATE TABLE IF NOT EXISTS `roadside_app_servicetypecategory` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  `charge` varchar(50) DEFAULT NULL,
  `service_type_id` int NOT NULL,
  PRIMARY KEY (`category_id`),
  KEY `roadside_app_servicetypecategory_service_type_id_6fe0f8e1` (`service_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roadside_app_servicetypecategory`
--

INSERT INTO `roadside_app_servicetypecategory` (`category_id`, `category_name`, `charge`, `service_type_id`) VALUES
(1, 'Flatbed Towing', '40 (Rs/Km)', 1),
(2, 'Integrated Tow Truck', '60 Rs/Km', 1),
(3, 'Petrol', '106.6 Rs/Lt', 2),
(4, 'Diesel', '95.5 Rs/Lt', 2),
(5, 'CNG', '85 Rs/Lt', 2),
(6, 'Basic Life Support Ambulance', '100 Rs/Km', 3),
(7, 'Advanced Life Support Ambulance', '180 Rs/Km', 3),
(8, 'Typre Punture', '50(Rs/Km)', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
