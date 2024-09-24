# Selenium Automation Project

## Overview
This project automates the testing of a frontend web application that communicates with a backend service. The test ensures that the greeting message from the backend is displayed correctly on the homepage.

### Tools Used
- **Selenium**: For browser automation
- **TestNG**: Test framework for managing and running the tests
- **Maven**: Dependency management and build tool

## Prerequisites
1. Install **Java** (JDK 8 or later)
2. Install **Maven** for managing dependencies.
3. Install **Google Chrome** browser.
4. Download the **ChromeDriver** compatible with your version of Chrome and update its path in `Config.java`.

## Setup
1. Clone the repository.
git clone <repository_url>

2. Navigate to the project directory:
cd <repository_name>

3. If using Maven, download the dependencies:
mvn clean install

## Running the Application
1. Start the backend and frontend services:
- Run `server.js` on port 3000.
- Run `app.js` on port 8080.
2. Execute the tests:
mvn test

or

Right-click on testng.xml and run it as a TestNG suite.

## Test Output
The tests will verify if the homepage displays the correct greeting message ("Hello from the Backend!") received from the backend.

## Troubleshooting
- Ensure that both backend and frontend services are running before running the test.
- If you encounter issues with ChromeDriver, check if the version of ChromeDriver match