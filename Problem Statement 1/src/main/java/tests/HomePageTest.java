package tests;

import org.testng.Assert;
import org.testng.annotations.Test;
import pages.HomePage;

public class HomePageTest extends BaseTest {

    @Test
    public void testGreetingMessage() {
       
        WebElement greetingElement = driver.findElement(By.tagName("h1"));
        
        // Check if the greeting message is as expected
        String expectedGreeting = "Hello from the Backend!";
        String actualGreeting = greetingElement.getText();
        
        Assert.assertEquals(actualGreeting, expectedGreeting, "Greeting message should match backend response.");
    }

    @Test
    public void testFallbackMessage() {
        
        WebElement fallbackMessageElement = driver.findElement(By.tagName("h1"));
        
        // Check if the fallback message is displayed correctly
        String expectedFallback = "Hello, World!";
        String actualFallback = fallbackMessageElement.getText();
        
        Assert.assertEquals(actualFallback, expectedFallback, "Fallback message should appear if backend is down.");
    }
}