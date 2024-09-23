<!-- db_conn.php -->
<?php
$servername = "localhost"; // Change if your database server is different
$username = "root"; // Database username
$password = ""; // Database password
$dbname = "roadside_assistance"; // Database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
