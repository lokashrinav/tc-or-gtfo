```markdown
# Blind TC Automation Script

This Python script uses Selenium WebDriver to automate interaction with posts on [TeamBlind](https://www.teamblind.com). It logs in, gathers links from the feed, and comments "TC or GTFO" on posts that do not mention "tc".

## Requirements

- **Python 3.x**
- **Selenium WebDriver**
- **Chrome WebDriver**

## Installation

1. Install the required Python packages:

   ```bash
   pip install selenium
   ```

2. Download Chrome WebDriver and add it to your system path.

## Usage

1. Clone the repository and open the project directory.
2. Edit the Python script to replace the email and password fields with your credentials:

   ```python
   username.send_keys("EMAIL-REPLACE")
   password.send_keys("PASSWORD-REPLACE")
   ```

3. Run the script:

   ```bash
   python script.py
   ```

## How It Works

1. The script opens TeamBlind using Chrome WebDriver.
2. It logs into the site with the provided username and password.
3. It scrapes the first 20 posts from the feed and collects their URLs.
4. For each post, it checks if "tc" is mentioned. If not, it comments "TC or GTFO".
5. After posting, the script navigates back to the feed and processes the next post.

## Customization

* You can change the number of posts the script scrapes by modifying this line in the script:

  ```python
  for i in range(20): # Change 20 to any number of posts
  ```

## Notes

* Ensure you replace `EMAIL-REPLACE` and `PASSWORD-REPLACE` with your actual login details.
* This script uses `time.sleep()` to control the waiting between actions. You can replace it with more robust options such as `WebDriverWait` for better performance.
* The script is set up to handle the first 20 posts but can be easily modified to process more.

## Disclaimer

This script is for educational purposes only. Be aware of the website's terms of service and avoid using automation in ways that violate these terms. Excessive use may result in account suspension.

## License

This project is licensed under the MIT License.
```
