import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;
import org.junit.After;

public class Login {
    private WebDriver driver;
    private WebDriverWait wait;

    @Given("browser is open")
    public void browser_is_open() {
        driver = new FirefoxDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        driver.manage().window().maximize();
    }

    @When("user enters username and password")
    public void user_enters_username_and_password() {
        try {
            // Wait for element to be present before interacting
            WebElement usernameField = wait.until(
                ExpectedConditions.presenceOfElementLocated(By.id("username"))
            );
            usernameField.sendKeys("your-username");
            
            WebElement passwordField = wait.until(
                ExpectedConditions.presenceOfElementLocated(By.id("password"))
            );
            passwordField.sendKeys("your-password");
        } catch (Exception e) {
            // Add proper error handling
            driver.quit();
            throw e;
        }
    }

    @Given("user is on login page")
    public void user_is_on_login_page() {
        try {
            driver.get("your-login-url");
            wait.until(ExpectedConditions.urlContains("login"));
        } catch (Exception e) {
            System.out.println("Failed to load login page: " + e.getMessage());
            throw e;
        }
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
} 