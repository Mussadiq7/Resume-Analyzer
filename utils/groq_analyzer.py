import os
import json
from typing import Dict, List, Optional, Any, Union
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

class DummyGroqClient:
    """A dummy Groq client for demonstration without a real API key"""
    
    class ChatCompletions:
        def create(self, **kwargs):
            messages = kwargs.get('messages', [])
            user_message = next((m['content'] for m in messages if m['role'] == 'user'), '')
            has_job_description = 'JOB DESCRIPTION' in user_message
            dummy_response = {
                "overall_assessment": "This is a dummy analysis generated for demonstration purposes. To get real AI-powered analysis, replace the API key in the code with a valid Groq API key.",
                "key_strengths": [
                    "Strong structure and organization",
                    "Good use of action verbs",
                    "Clear presentation of experience"
                ],
                "improvement_areas": [
                    "Add more quantifiable achievements",
                    "Enhance skills section",
                    "Tailor content to target roles"
                ],
                "specific_suggestions": [
                    "Include metrics and specific outcomes for your achievements",
                    "Add a strong professional summary at the top",
                    "Use more industry-specific keywords",
                    "Ensure consistent formatting throughout"
                ],
                "structure_feedback": "The resume has a clear structure with defined sections, making it easy to navigate. Consider using more bullet points for better readability.",
                "language_feedback": "The language is professional and concise. You've used some good action verbs, but could incorporate more powerful verbs like 'spearheaded', 'orchestrated', or 'transformed'.",
                "red_flags": [
                    "Some job descriptions are too generic",
                    "Skills section could be more comprehensive"
                ]
            }
            
            # Add job comparison if job description was provided
            if has_job_description:
                dummy_response["job_match"] = {
                    "match_assessment": "This is a dummy job match assessment. To get a real analysis, please provide a valid Groq API key.",
                    "missing_keywords": [
                        "project management", 
                        "agile", 
                        "scrum", 
                        "stakeholder communication", 
                        "budget planning"
                    ],
                    "alignment_score": 65,
                    "recommendations": [
                        "Add more keywords from the job description",
                        "Emphasize relevant experience more prominently",
                        "Highlight specific skills requested in the job posting"
                    ]
                }
            
            # Create the response object
            response_obj = type('DummyResponse', (), {})()
            choice_obj = type('DummyChoice', (), {})()
            message_obj = type('DummyMessage', (), {})()
            
            message_obj.content = json.dumps(dummy_response)
            choice_obj.message = message_obj
            response_obj.choices = [choice_obj]
            
            return response_obj
    
    def __init__(self):
        """Initialize the dummy client"""
        self.chat = self.ChatCompletions()

# Get API key from environment variable, or None if not set
DEFAULT_API_KEY = os.getenv('GROQ_API_KEY')

# This will be initialized when an API key is provided
groq_client = None

class GroqAnalyzer:
    """Interface with Groq API for resume analysis"""
    
    def __init__(self, api_key: Optional[str] = None):
        # Use provided key, or environment variable, or None
        self.api_key = api_key if api_key else DEFAULT_API_KEY
        self.client = None
        
        # Only attempt to initialize real client if we have an API key
        if self.api_key:
            self.initialize_client()
        
        # If no API key or initialization failed, use dummy client
        if self.client is None:
            self.client = DummyGroqClient()
            print("Using demo mode with dummy responses. Set GROQ_API_KEY in .env file for real analysis.")
    
    def initialize_client(self):
        try:
            import groq
            self.client = groq.Client(api_key=self.api_key)
            return True
        except ImportError:
            self.client = DummyGroqClient()
            return "Error: Groq package not installed. Using dummy client."
        except Exception as e:
            self.client = DummyGroqClient()
            return f"Warning: Using dummy Groq client for demonstration. Error: {str(e)}"
    
    def analyze_resume(self, resume_text: str, job_description: Optional[str] = None) -> Dict[str, Any]:
        """Analyze resume text using Groq API"""
        if self.client is None:
            self.client = DummyGroqClient()
            
        try:
            # Create prompt for resume analysis
            prompt = f"""You are an expert resume analyzer and career coach. Analyze the following resume and provide detailed feedback.
            
            RESUME TEXT:
            {resume_text}
            
            Provide a comprehensive analysis including:
            1. Overall assessment of the resume's strengths and weaknesses
            2. Clear, specific improvement suggestions prioritized by importance
            3. Assessment of the resume's organization and structure
            4. Evaluation of the language, action verbs, and achievement descriptions
            5. Any red flags or issues that might concern employers
            
            IMPORTANT: Your response MUST be a valid JSON object with EXACTLY this structure:
            {{
              "overall_assessment": "text",
              "key_strengths": ["strength1", "strength2", "strength3"],
              "improvement_areas": ["area1", "area2", "area3"],
              "specific_suggestions": ["suggestion1", "suggestion2", "suggestion3"],
              "structure_feedback": "text",
              "language_feedback": "text",
              "red_flags": ["flag1", "flag2"]
            }}
            """
            
            # Add job description comparison if provided
            if job_description:
                prompt += f"""
                
                ADDITIONAL ANALYSIS - JOB DESCRIPTION COMPARISON:
                Compare the resume to the following job description and add a 'job_match' section to your response:
                
                JOB DESCRIPTION:
                {job_description}
                
                Add this EXACT structure to your JSON:
                {{
                  "job_match": {{
                    "match_assessment": "text",
                    "missing_keywords": ["keyword1", "keyword2", "keyword3"],
                    "alignment_score": 75,
                    "recommendations": ["rec1", "rec2", "rec3"]
                  }}
                }}
                
                IMPORTANT: Ensure the final JSON is valid and properly formatted with all closing braces and brackets.
                """
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are an expert resume analyzer that provides detailed, professional feedback in JSON format."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=4096,
                response_format={"type": "json_object"}
            )
            
            analysis_text = response.choices[0].message.content
            return {
                'analysis': analysis_text,
                'error': None
            }
            
        except Exception as e:
            return {
                'analysis': None,
                'error': f"Error analyzing resume with Groq: {str(e)}"
            }
    
    def generate_ai_suggestions(self, resume_text: str) -> List[str]:
        """Generate specific improvement suggestions for the resume
        
        Args:
            resume_text: The extracted text from the resume
            
        Returns:
            List of improvement suggestions
        """
        if not self.client:
            return ["Error: Groq API key not provided. Please enter your API key to get AI-powered suggestions."]
        
        try:
            prompt = f"""You are an expert resume coach. Based on the following resume, provide 5-7 specific, actionable suggestions for improvement. Focus on clarity, impact, and marketability.
            
            RESUME TEXT:
            {resume_text}
            
            Provide ONLY a list of specific suggestions, each 1-2 sentences long.
            """
            
            # Call Groq API
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",  # Using smaller model for faster response
                messages=[
                    {"role": "system", "content": "You are a resume improvement expert that provides concise, actionable suggestions."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=1024
            )
            
            # Extract suggestions and split into list
            suggestions_text = response.choices[0].message.content
            
            # Simple parsing: split by newlines and filter out empty lines
            # Could be improved with more robust parsing if needed
            suggestions = [line.strip().strip('- ') for line in suggestions_text.split('\n') if line.strip()]
            
            if not suggestions:
                suggestions = ["Unable to generate suggestions. Please try again."]
                
            return suggestions[:7]  # Limit to 7 suggestions max
            
        except Exception as e:
            return [f"Error generating suggestions: {str(e)}"]
    
    def extract_structured_information(self, resume_text: str) -> Dict[str, Any]:
        """Extract structured information from the resume text using Groq AI
        
        Args:
            resume_text: The raw text extracted from the resume
            
        Returns:
            Dictionary with structured information (contact info, sections, etc.)
        """
        if not resume_text or len(resume_text.strip()) < 100:
            return {
                "error": "Resume text is too short or empty",
                "contact_info": {},
                "sections": {}
            }
            
        try:
            prompt = f"""You are an expert resume parser. Extract structured information from the following resume text. Identify the contact information and major sections.

            RESUME TEXT:
            {resume_text}

            Your response MUST be a well-formed JSON with EXACTLY this structure:
            {{
              "contact_info": {{
                "name": "John Doe",
                "email": "johndoe@example.com",
                "phone": "123-456-7890",
                "linkedin": "linkedin.com/in/johndoe",
                "github": "github.com/johndoe",
                "website": "johndoe.com"
              }},
              "sections": {{
                "summary": "Text from summary section",
                "experience": "Text from experience section",
                "education": "Text from education section",
                "skills": "Text from skills section",
                "projects": "Text from projects section",
                "certifications": "Text from certifications section"
              }}
            }}

            IMPORTANT: If a field is not found in the resume, use an empty string for text fields or empty object ({{}} ) for objects. Ensure all fields exist even if empty.
            """
            
            # Call Groq API with the larger model for comprehensive analysis
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[
                    {"role": "system", "content": "You are an expert resume parser that extracts structured information in JSON format."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,  # Lower temperature for more consistent parsing
                max_tokens=4000,
                response_format={"type": "json_object"}
            )
            
            # Parse the JSON response
            parsed_data = json.loads(response.choices[0].message.content)
            
            # Ensure expected structure exists
            if 'contact_info' not in parsed_data:
                parsed_data['contact_info'] = {}
            if 'sections' not in parsed_data:
                parsed_data['sections'] = {}
                
            return parsed_data
        
        except Exception as e:
            return {
                "error": f"Error extracting structured information: {str(e)}",
                "contact_info": {},
                "sections": {}
            }
