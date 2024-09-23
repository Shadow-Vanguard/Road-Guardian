<!-- login.php
<?php
session_start();
require 'db_connect.php'; // This file should contain your DB connection logic

$message = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Fetch user from the database
    $sql = "SELECT * FROM users WHERE username = ? AND password = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $username, $password);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        // Successful login
        $_SESSION['username'] = $username;
        header("Location: userhome.php"); // Redirect to user home after login
        exit;
    } else {
        // Failed login
        $message = "Invalid username or password.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="css/login.css">

    <style>
        body {
            background-image: url("images/home3.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
</head>
<body>
    <nav class="navbar-login">
        <div class="navbar-brand-login">
            <h1>ROAD GUARDIAN</h1>
        </div>
        <div class="navbar-links-login">
            <a href="home.php">Home</a>
            <a href="login.php">Login</a>
            <a href="register.php">Register</a>
        </div>
    </nav>

    <div class="login-container">
        <h2>Login</h2>
        <form method="post" id="loginForm" action="userhome.php">
            <div class="input-container">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-container">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <?php if(!empty($message)): ?>
                <div class="message"><?php echo $message; ?></div>
            <?php endif; ?>
            <label for="name">Not Registered Yet?</label>
            <a href="register.php" class="button">Create An Account</a>
            <div class="forgot-password">
                <a href="#">Forgot Password?</a>
            </div>
            <div class="button-container">
                <button type="submit">Login</button>
            </div>
        </form>
    </div>

    <footer class="footer-login">
        <p>© 2024 Roadside Assistance. All rights reserved.</p>
        <p>Contact us: info@roadsideassistance.com | +1 234 567 890</p>
    </footer>
</body>
</html> -->
