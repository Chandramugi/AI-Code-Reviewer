# 🤖 AI Code Reviewer

### Intelligent Python Code Analysis and Automated Code Correction using Generative AI

An AI-powered Python code review application built using **Streamlit, Groq LLM, Abstract Syntax Tree (AST), and Pylint**. The application analyzes Python source code, identifies potential errors, explains coding issues, classifies their severity, and generates corrected Python code using Generative AI.

---

## 📌 Project Overview

AI Code Reviewer is designed to assist developers in identifying and resolving issues in Python programs.

Users can submit Python code through an interactive web interface. The application performs static code analysis and uses a Large Language Model (LLM) to generate detailed code reviews and improvement suggestions.

It aims to improve code quality, readability, reliability, and maintainability through automated analysis and AI-powered recommendations.

## ✨ Key Features

- **Syntax Error Detection:** Identifies Python syntax errors using AST.
- **Code Structure Analysis:** Extracts functions, classes, imports, and lines of code.
- **Static Code Analysis:** Uses Pylint to identify code-quality issues.
- **AI-Powered Code Review:** Uses Groq LLM to analyze submitted Python code.
- **Bug Detection:** Identifies potential runtime errors and logical issues.
- **Severity Classification:** Categorizes identified issues as Critical, High, Medium, or Low.
- **Detailed Error Explanation:** Explains what went wrong, why it happened, and how to fix it.
- **Corrected Code Generation:** Generates an improved version of the submitted Python program.
- **Apply Corrected Code:** Allows users to replace the original editor content with AI-generated corrections.
- **Code Download:** Downloads the corrected Python program as a `.py` file.
- **Test Case Suggestions:** Generates recommended test cases for the reviewed program.
- **Token Usage Monitoring:** Displays input, output, and total token consumption.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Groq API | AI-powered code review |
| GPT-OSS 120B | Large Language Model |
| AST | Python syntax and structure analysis |
| Pylint | Static code-quality analysis |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control and project hosting |

## 🏗️ Project Architecture

The application follows a modular architecture that separates the user interface, code analysis, AI processing, and utility functions.

```text
AI-Code-Reviewer/
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── reviewer/
│   ├── __init__.py
│   ├── code_analyzer.py
│   ├── llm_reviewer.py
│   └── prompts.py
│
├── utils/
│   ├── __init__.py
│   └── token_tracker.py
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

### 📂 Module Description

**1. app.py**

Main Streamlit application responsible for:
- User interface and Python code input.
- Displaying static analysis results.
- Integrating the AI review engine.
- Displaying corrected code and token usage.
- Downloading and applying corrected code.

**2. config/settings.py**

Manages:
- Groq API key configuration.
- AI model selection.
- Application name and version.
- Environment variable validation.

**3. reviewer/code_analyzer.py**

Performs static code analysis using:
- Python AST for syntax validation and structural analysis.
- Pylint for code-quality checks.
- Pylint score extraction.

**4. reviewer/llm_reviewer.py**

Connects the application to the Groq API and:
- Sends Python source code for review.
- Processes AI-generated responses.
- Retrieves token consumption information.

**5. reviewer/prompts.py**

Contains system instructions and prompt-generation logic that guide the AI reviewer in identifying errors and generating corrected code.

**6. utils/token_tracker.py**

Calculates and formats token consumption statistics.

## 🔄 Application Workflow

1. User enters Python source code in the Streamlit editor.
2. The application performs syntax validation using AST.
3. AST extracts structural information such as functions, classes, and imports.
4. Pylint analyzes code quality and identifies potential issues.
5. Static analysis results and submitted code are passed to Groq.
6. The AI reviews the program and generates explanations and recommendations.
7. The application extracts and displays corrected Python code.
8. Users can download or apply the corrected code.
9. Token consumption and model information are displayed.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- VS Code or another Python IDE
- Groq API key

### 1. Clone the Repository

```bash
git clone https://github.com/Chandramugi/AI-Code-Reviewer.git
```

### 2. Navigate to the Project Directory

```bash
cd AI-Code-Reviewer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Groq API Key

Create a `.env` file in the project root directory.

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your actual Groq API key.

Obtain an API key from:

https://console.groq.com/keys

The application uses the following Groq model:

```text
openai/gpt-oss-120b
```

**Important:** Never upload your `.env` file or expose your API key publicly.

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 💻 How to Use

1. Launch the application.
2. Enter or paste Python source code into the editor.
3. Click **Analyze & Review Code**.
4. View syntax and static analysis results.
5. Read AI-generated error explanations and severity classifications.
6. Review the suggested improvements.
7. View the corrected Python program.
8. Download the corrected code or apply it directly to the editor.
9. Review token consumption and model information.

## 📊 Example Use Case

**Submitted Python Code:**

```python
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

marks = [85, 90, 78, 92, 88]

print(calculate_averge(marks))
```

**Potential Issues:**

- Misspelled function name: `calculate_averge`.
- Undefined function call resulting in a `NameError`.
- Missing handling for an empty marks list.
- Missing input validation.

**Expected AI Recommendations:**

- Correct the function call.
- Handle empty input.
- Improve documentation and code robustness.
- Generate a corrected Python implementation and recommended test cases.

## 🔐 Security and Limitations

- API credentials are stored in environment variables.
- `.env` is excluded from Git using `.gitignore`.
- AI-generated corrections are suggestions and should be reviewed before use.
- Pylint and AST perform static analysis; they do not prove runtime correctness.
- The application does not execute submitted code as part of its review workflow.
- AI-generated code should be independently tested before production use.

## 🚀 Future Enhancements

- Support for multiple programming languages.
- Interactive line-by-line error highlighting.
- Structured JSON-based review reports.
- Automated unit-test generation and execution in a sandbox.
- Code complexity and maintainability metrics.
- Review history and report export.
- Advanced security vulnerability analysis.
- Integration with GitHub repositories and pull requests.

## 👩‍💻 Author

**Chandramugi P S**

B.Tech – Artificial Intelligence and Data Science

GitHub: https://github.com/Chandramugi

## 📄 License

This project is currently available for educational and portfolio purposes. A formal open-source license can be added separately.

---

⭐ If you find this project useful, consider giving the repository a star!
