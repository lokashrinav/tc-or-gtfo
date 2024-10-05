# Blind TC Automation Script AKA TC or GTFO!

This Python script uses Selenium WebDriver to automate interaction with posts on [TeamBlind](https://www.teamblind.com). It logs in, gathers links from the feed, and comments "TC or GTFO" on posts that do not mention "tc".

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver
- OpenAI API key

## Installation

1. Install the required Python packages:

   ```bash
   pip install selenium openai
   ```

2. Download Chrome WebDriver and add it to your system path.

## Usage

1. Clone the repository and open the project directory.
2. Edit the Python script to replace the placeholders:

   ```python
   openai.api_key = "OPENAI-KEY-REPLACE"
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
4. For each post, it checks the content using OpenAI's GPT-4 model to determine if it's sensitive information.
5. If the content is not sensitive and doesn't mention "tc", it comments "TC or GTFO".
6. After processing, the script navigates back to the feed and moves to the next post.

## Customization

You can change the number of posts the script scrapes by modifying this line:

```python
for i in range(20): # Change 20 to any number of posts
```

## Notes

- Ensure you replace `OPENAI-KEY-REPLACE`, `EMAIL-REPLACE`, and `PASSWORD-REPLACE` with your actual details.
- This script uses `time.sleep()` for waiting between actions. Consider using `WebDriverWait` for better performance.
- The script is set up to handle the first 20 posts but can be easily modified to process more.

## OpenAI Integration

The script uses OpenAI's GPT-4 model to analyze post content for sensitivity. It only comments on posts that are not deemed sensitive by the AI model.

## Disclaimer

This script is for educational purposes only. Be aware of the website's terms of service and avoid using automation in ways that violate these terms. Excessive use may result in account suspension.

## License

This project is licensed under the MIT License.
