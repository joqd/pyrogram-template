# pyrogram-template

This is a template for building Telegram bots using the Pyrogram library. It includes a basic project structure with sample files to get you started quickly.

## Features

- Organized project structure with separate folders for plugins and models.
- Sample plugin files (`ping.py`) to demonstrate how to handle messages using Pyrogram.
- A sample models file (`models.py`) to demonstrate how to define custom models using Peewee for database operations.
- `auth.ini` file for storing API credentials and other configuration settings.
- `requirements.txt` file to list the required Python packages for easy installation.

## Project Structure

The project structure is as follows:

```
.
├── auth.ini # Configuration file for storing API credentials
├── LICENSE # License file
├── main.py # Main entry point for your bot
├── plugins # Folder for storing plugin files
│   ├── models.py # Sample file for defining custom models
│   └── ping.py # Sample plugin file for handling messages
├── README.md # This README file
└── requirements.txt # File listing required Python packages
```


## Getting Started

1. Clone this repository to your local machine.
2. Install the required Python packages listed in `requirements.txt` using `pip`.
3. Update the `auth.ini` file with your API credentials and other configuration settings.
4. Write your bot's logic in the `main.py` file, or create additional plugin files in the `plugins` folder.
5. Run your bot using `python main.py` and start building your Telegram bot!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
