# Selenium Docker Example

This project demonstrates running a Selenium test in a Docker container using Python and Chrome in headless mode. The test script opens Google, prints the page title, and saves a screenshot.

## Project Structure

- `test.py`: Selenium test script.
- `Dockerfile`: Builds the Docker image with Chrome, ChromeDriver, and Python dependencies.
- `requirements.txt`: Python dependencies.
- `.vscode/tasks.json`: VS Code tasks for building and running the Docker container.
- `.env`: Environment variables for the container.
- `/screenshots`: Directory for storing screenshots (created automatically).

## Prerequisites

- [Docker](https://www.docker.com/) installed
- [Visual Studio Code](https://code.visualstudio.com/) (optional, for integrated tasks)

## Usage

### Build the Docker Image

```sh
docker build --pull --no-cache -t selenium-app .
```

### Prepare Screenshots Folder

```sh
mkdir -p ./screenshots && chmod 777 ./screenshots
```

### Run the Selenium Test

```sh
docker run --rm -v $(pwd)/screenshots:/screenshots --env-file .env selenium-app
```

Alternatively, use VS Code tasks:

- **Docker Build**: Builds the image.
- **Prepare Screenshots Folder**: Creates and sets permissions for the screenshots directory.
- **Docker Run**: Runs the test and saves the screenshot to `./screenshots/google.png`.

## Output

- The script prints the page title to the console.
- Screenshot is saved to `./screenshots/google.png`.

## Customization

- Modify `test.py` to change the test logic or target URL.
- Add environment variables to `.env` as needed.