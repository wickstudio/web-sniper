```markdown
# Web-Sniper

Web-Sniper is a versatile command-line tool for web scraping and code analysis. It allows you to easily retrieve HTML, CSS, and JavaScript code from websites, download images, and perform basic code analysis. Whether you're a developer looking to examine the code of a web page or need to collect assets for a project, Web-Sniper has got you covered.

![Web-Sniper Logo](https://media.discordapp.net/attachments/1051148413749706782/1159194048809140244/image.png?ex=65302296&is=651dad96&hm=c52ef05959efd1ebe141b27228ff9a2a6eb40f9288e98515f98ba2d93b680290&=&width=961&height=675)

## Features

- Retrieve HTML, CSS, and JavaScript code from a specified website.
- Download images from a webpage.
- Perform basic code analysis, including line count, for HTML, CSS, and JavaScript.
- User-friendly command-line interface.
- Cross-platform support (Linux, macOS, and Windows).

## Installation

### Prerequisites

Before using Web-Sniper, make sure you have Python 3 installed on your system.

### Installation Steps

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Wickdev077/web-sniper.git
   ```

2. Change to the project directory:

   ```bash
   cd web-sniper
   ```

3. Install the required Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Web-Sniper provides several options for collecting web-related information. Simply run the tool and choose from the available options:

```bash
python main.py
```

You will be prompted to enter a website URL and select an action:

1. Get HTML code.
2. Get CSS code.
3. Get JavaScript code.
4. Download Images.
5. Exit.

## Examples

### Get HTML Code

To retrieve and save the HTML code of a website:

```bash
python main.py
# Choose option 1, enter the website URL, and the HTML code will be saved in the 'html_codes' folder.
```

### Download Images

To download images from a webpage:

```bash
python main.py
# Choose option 4, enter the website URL, and images will be saved in the 'images' folder.
```

### Code Analysis

Web-Sniper also provides basic code analysis for HTML, CSS, and JavaScript:

```bash
python main.py
# After selecting an option (1, 2, or 3), code analysis will be displayed, including the line count.
```

## Contributing

Contributions are welcome! If you have any ideas for improvements or find any issues, please open an issue or submit a pull request.

## Contact

Feel free to reach out for questions, suggestions, or collaboration opportunities.

1. **Website:** [https://www.wickdev.xyz](https://wickdev.xyz/)
2. **GitHub:** [https://github.com/Wickdev077](https://github.com/Wickdev077)
3. **Instagram:** [https://www.instagram.com/mik__subhi](https://www.instagram.com/mik__subhi/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.