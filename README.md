# Prompt-Debugger

## Overview
**Prompt Debugger** is a Streamlit application designed to enhance your prompt engineering skills. It provides two primary features:
1. **Debug Prompt**: Rewrites your prompt to help you achieve the expected output using Gemini.
2. **Refine Prompt**: Refines poorly written prompts based on best practices for prompt engineering.

## Features
- **Debug Prompt** 🔍:
  - Identify and correct errors in your prompts to align with the expected output.
  - Utilizes the Gemini model for prompt generation and debugging.
- **Refine Prompt** ✨:
  - Refines prompts by adhering to prompt engineering best practices.
  - Ensures that prompts are structured, clear, and concise.

## Installation

### Prerequisites
- 🐍 Python 3.11 or higher
- 🐳 Docker (if using Docker for deployment)

### Clone the Repository
```sh
git clone https://github.com/bhav09/Prompt-Debugger.git
cd Drompt-Debugger
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Configuration
Create a `credentials.json` file in the root directory of the project and add your Gemini API key:
```json
{
  "key": "YOUR_GEMINI_API_KEY"
}
```

## Usage

### Running Locally
```sh
streamlit run main.py
```
Open your browser and navigate to `http://localhost:8501`.

### Running with Docker

#### Build Docker Image
```sh
docker build -t prompt-debugger .
```

#### Run Docker Container
```sh
docker run -p 8502:8501 prompt-debugger
```

Open your browser and navigate to `http://localhost:8502`.

## How to Use the Application

### Debug Prompt

1. Navigate to the "Debug Prompt" tab.
2. Enter your input prompt, test case, current output, and expected output.
3. Click the "Debug Prompt" button.
4. The application will attempt to rewrite the prompt to achieve the expected output.

### Refine Prompt

1. Navigate to the "Refine Prompt" tab.
2. Enter your input prompt.
3. Click the "Refine Prompt" button.
4. The application will refine your prompt based on best practices for prompt engineering.

## Contributing

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`git checkout -b feature-branch`).
3. ✏️ Make your changes.
4. ✅ Commit your changes (`git commit -am 'Add some feature'`).
5. 📤 Push to the branch (`git push origin feature-branch`).
6. 🛠️ Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Streamlit 🖥️
- Google Gemini API 🔮

Feel free to reach out if you have any questions or feedback. Happy debugging and refining! 🎉
