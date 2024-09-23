-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 21, 2024 at 04:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `roadside_assistance`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(24, 'Can view Custom User', 6, 'view_customuser');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'roadside_app', 'customuser'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-09-18 08:16:03.668335'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-09-18 08:16:03.757658'),
(3, 'auth', '0001_initial', '2024-09-18 08:16:03.997775'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-09-18 08:16:04.059964'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-09-18 08:16:04.070969'),
(6, 'auth', '0004_alter_user_username_opts', '2024-09-18 08:16:04.089957'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-09-18 08:16:04.098975'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-09-18 08:16:04.102956'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-09-18 08:16:04.113015'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-09-18 08:16:04.121989'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-09-18 08:16:04.132536'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-09-18 08:16:04.147534'),
(13, 'auth', '0011_update_proxy_permissions', '2024-09-18 08:16:04.160551'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-09-18 08:16:04.168551'),
(15, 'roadside_app', '0001_initial', '2024-09-18 08:16:04.409234'),
(16, 'admin', '0001_initial', '2024-09-18 08:16:04.499068'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-09-18 08:16:04.507190'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-09-18 08:16:04.513215'),
(19, 'sessions', '0001_initial', '2024-09-18 08:16:04.537073');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('akhfrp81bq8gcv0i0roqtaxgix680mqg', '.eJxVjDsOwjAQRO_iGllef_Cakp4zWOsfDiBbipMKcXcSKQV0o3lv5s08rUv168iznxK7MGCn3y5QfOa2g_Sgdu889rbMU-C7wg86-K2n_Loe7t9BpVG3tQFJShOAyI4KKqNBokNnihVORbBSOGnzORSNOYEyKAIElE6hLltkny-n1jZU:1sqpsm:O_2cp_rF0dOY80PI2GoGkxyrHGbw9clyQVoEV-VlpkA', '2024-10-02 08:17:52.419596');

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_customuser`
--

CREATE TABLE `roadside_app_customuser` (
  `id` bigint(20) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(255) NOT NULL,
  `role` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roadside_app_customuser`
--

INSERT INTO `roadside_app_customuser` (`id`, `last_login`, `is_superuser`, `username`, `name`, `phone`, `address`, `role`, `password`, `is_active`, `is_staff`) VALUES
(1, '2024-09-18 08:17:52.413590', 0, 'Rosh', 'Roshan', '9061855716', 'Valiyaveettill(H)Mukkada', 'user', 'pbkdf2_sha256$720000$Xif2wQe7lDWsQ2TDVC4kd0$1MMLvNmz0pwHXTLontuWupFBl+YKdEBy6KHr8LTqdjQ=', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_customuser_groups`
--

CREATE TABLE `roadside_app_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roadside_app_customuser_user_permissions`
--

CREATE TABLE `roadside_app_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_roadside_app_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `roadside_app_customuser`
--
ALTER TABLE `roadside_app_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `roadside_app_customuser_groups`
--
ALTER TABLE `roadside_app_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roadside_app_customuser__customuser_id_group_id_aa2c88ca_uniq` (`customuser_id`,`group_id`),
  ADD KEY `roadside_app_customu_group_id_ff521eb7_fk_auth_grou` (`group_id`);

--
-- Indexes for table `roadside_app_customuser_user_permissions`
--
ALTER TABLE `roadside_app_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `roadside_app_customuser__customuser_id_permission_8197d229_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `roadside_app_customu_permission_id_0e6972db_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `roadside_app_customuser`
--
ALTER TABLE `roadside_app_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `roadside_app_customuser_groups`
--
ALTER TABLE `roadside_app_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `roadside_app_customuser_user_permissions`
--
ALTER TABLE `roadside_app_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_roadside_app_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `roadside_app_customuser` (`id`);

--
-- Constraints for table `roadside_app_customuser_groups`
--
ALTER TABLE `roadside_app_customuser_groups`
  ADD CONSTRAINT `roadside_app_customu_customuser_id_b5a47e79_fk_roadside_` FOREIGN KEY (`customuser_id`) REFERENCES `roadside_app_customuser` (`id`),
  ADD CONSTRAINT `roadside_app_customu_group_id_ff521eb7_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `roadside_app_customuser_user_permissions`
--
ALTER TABLE `roadside_app_customuser_user_permissions`
  ADD CONSTRAINT `roadside_app_customu_customuser_id_0172d06b_fk_roadside_` FOREIGN KEY (`customuser_id`) REFERENCES `roadside_app_customuser` (`id`),
  ADD CONSTRAINT `roadside_app_customu_permission_id_0e6972db_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
