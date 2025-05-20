# Resume Analyzer

![Python](https://img.shields.io/badge/python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/streamlit-1.0%2B-orange) ![License](https://img.shields.io/badge/license-MIT-green)

A Streamlit web application that analyzes resumes, extracts key information, and provides insights and improvement suggestions using AI technology powered by Groq's language models.

## Features

- **Resume Parsing**: Upload and parse resumes in PDF, DOCX, or TXT formats
- **Information Extraction**: Automatically extract contact details, education, experience, and skills
- **Skills Analysis**: Identify technical and soft skills present in the resume
- **Content Analysis**: Analyze word frequency and readability metrics
- **Job Description Comparison**: Compare your resume with job descriptions for better targeting
- **Improvement Suggestions**: Get actionable suggestions to enhance your resume
- **Visualizations**: Interactive charts and graphs to visualize the analysis

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mussadiq7/Resume-Analyzer.git
   cd Resume-Analyzer
   ```

2. Set up a virtual environment (recommended):
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
   # Ensure Groq package is installed
   pip install groq
   ```

## Usage

1. Set up your Groq API key (required for AI-powered analysis):
   - Create a `.env` file in the root directory of the project
   - Add your Groq API key to the file in the following format:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
   - You can obtain a Groq API key by signing up at [groq.com](https://console.groq.com/keys)
   - Without a valid API key, the application will run in demo mode with simulated responses

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to http://localhost:8501
4. Upload your resume (PDF, DOCX, or TXT format)
5. Optionally paste a job description for comparison
6. Click "Analyze Resume" to process your document
7. Explore the analysis across different tabs

## Project Structure

```
resume-analyzer/
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (API keys)
├── utils/               # Utility modules
│   ├── __init__.py      # Package initializer
│   ├── analyzer.py      # Text analysis functionality
│   ├── groq_analyzer.py # AI-powered analysis using Groq API
│   ├── parser.py        # Resume parsing functionality
│   └── visualizer.py    # Data visualization components
├── .gitignore          # Git ignore file
├── assets/             # CSS, images, and static files
│   └── styles.css      # Custom CSS styling
└── README.md           # Project documentation
```

### Key Components

- **app.py**: The main entry point of the application, containing the Streamlit UI code and application flow
- **utils/parser.py**: Handles resume document parsing (PDF, DOCX, TXT)
- **utils/analyzer.py**: Contains text analysis logic for resume content
- **utils/groq_analyzer.py**: Manages the Groq API integration for AI-powered analysis
- **utils/visualizer.py**: Provides data visualization functionality for the analysis results
- **.env**: Contains your Groq API key (not committed to version control)

## Groq API Integration

This application integrates with the Groq API to provide AI-powered resume analysis using large language models:

- **Advanced AI Analysis**: Get detailed feedback on your resume using state-of-the-art language models (Llama 3)
- **Job Match Assessment**: AI-based comparison between your resume and job descriptions
- **Specific Improvement Suggestions**: Receive tailored recommendations to enhance your resume
- **Demo Mode**: The application works in demo mode without requiring an API key

The application uses two different Groq models:
- `llama3-70b-8192`: For comprehensive resume analysis and job matching
- `llama3-8b-8192`: For generating quick improvement suggestions

### Setting up the API Key

1. Create a `.env` file in the root directory of the project
2. Add your Groq API key to the file:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
3. You can obtain a Groq API key by signing up at [groq.com](https://console.groq.com/keys)
4. The application will automatically use this key when available
5. If no API key is provided, the application will run in demo mode with simulated responses

## Dependencies

The application relies on the following key libraries:

- **Web Application**:
  - streamlit: Web application framework

- **Data Processing**:
  - pandas & numpy: Data manipulation and analysis
  - PyPDF2 & python-docx: PDF and DOCX document parsing

- **Natural Language Processing**:
  - spaCy & NLTK: Text analysis and language processing
  - textstat: Readability metrics and text statistics

- **Visualization**:
  - matplotlib & plotly: Interactive data visualization
  - wordcloud: Word cloud generation for text analysis

- **AI Integration**:
  - groq: Client for accessing Groq's language models
  - python-dotenv: Environment variable management for API keys

## Troubleshooting

### Common Issues

1. **Groq API Key Issues**
   - **Error**: `Error with Groq analysis: Error analyzing resume with Groq: ...`
   - **Solution**: Verify your Groq API key is correctly set in the `.env` file and that you have installed the `groq` package with `pip install groq`
   - **Note**: API method structure is `self.client.chat.completions.create()`

2. **PDF Parsing Issues**
   - **Error**: Issues extracting text from certain PDF formats
   - **Solution**: Try converting your PDF to another format or use the TXT upload option

3. **Library Import Errors**
   - **Error**: Missing module errors
   - **Solution**: Ensure all dependencies are installed with `pip install -r requirements.txt`

4. **Application Not Starting**
   - **Error**: Streamlit fails to start
   - **Solution**: Check Python version (3.8+ recommended) and ensure Streamlit is installed correctly

5. **Demo Mode Active Despite API Key**
   - **Issue**: Application shows "Using demo mode with dummy responses" even with API key set
   - **Solution**: Ensure the `.env` file is in the root directory and the API key format is correct (no quotes around the key)

## Future Improvements

- Add machine learning-based resume scoring
- Implement more advanced NLP for entity recognition
- Add support for more file formats
- Enhance job matching algorithms
- Implement user accounts to save analysis history
