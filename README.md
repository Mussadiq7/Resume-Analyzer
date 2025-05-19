# Resume Analyzer

A Streamlit web application that analyzes resumes, extracts key information, and provides insights and improvement suggestions.

## Features

- **Resume Parsing**: Upload and parse resumes in PDF, DOCX, or TXT formats
- **Information Extraction**: Automatically extract contact details, education, experience, and skills
- **Skills Analysis**: Identify technical and soft skills present in the resume
- **Content Analysis**: Analyze word frequency and readability metrics
- **Job Description Comparison**: Compare your resume with job descriptions for better targeting
- **Improvement Suggestions**: Get actionable suggestions to enhance your resume
- **Visualizations**: Interactive charts and graphs to visualize the analysis

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download NLTK data (optional, will be done automatically on first run):

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Open your web browser and navigate to http://localhost:8501
3. Upload your resume (PDF, DOCX, or TXT format)
4. Optionally paste a job description for comparison
5. Click "Analyze Resume" to process your document
6. Explore the analysis across different tabs

## Project Structure

```
resume-analyzer/
├── app.py                # Main Streamlit application
├── requirements.txt      # Dependencies
├── utils/               # Utility modules
│   ├── __init__.py      # Package initializer
│   ├── analyzer.py      # Text analysis functionality
│   ├── groq_analyzer.py # AI-powered analysis using Groq API
│   ├── parser.py        # Resume parsing functionality
│   └── visualizer.py    # Data visualization components
├── .gitignore          # Git ignore file
├── assets/               # CSS, images, etc. (if needed)
└── README.md           # Project documentation
```

## Groq API Integration

This application integrates with the Groq API to provide AI-powered resume analysis:

- **Advanced AI Analysis**: Get detailed feedback on your resume using state-of-the-art language models
- **Job Match Assessment**: AI-based comparison between your resume and job descriptions
- **Specific Improvement Suggestions**: Receive tailored recommendations to enhance your resume
- **Demo Mode**: The application works in demo mode without requiring an API key

### Setting up the API Key

1. Create a `.env` file in the root directory based on the provided `.env.example`
2. Add your Groq API key to the file:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
3. The application will automatically use this key when available
4. If no API key is provided, the application will run in demo mode with simulated responses

## Dependencies

- streamlit: Web application framework
- pandas & numpy: Data manipulation
- PyPDF2 & python-docx: Document parsing
- spaCy & NLTK: Natural language processing
- matplotlib & plotly: Data visualization
- wordcloud: Word cloud generation
- textstat: Readability metrics

## Future Improvements

- Add machine learning-based resume scoring
- Implement more advanced NLP for entity recognition
- Add support for more file formats
- Enhance job matching algorithms
- Implement user accounts to save analysis history

## License

MIT
