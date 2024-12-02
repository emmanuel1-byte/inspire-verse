# InspireVerse

**InspireVerse** is a FastAPI-based application designed to inspire and uplift users through Bible stories, quotes, and verses tailored to their preferences. This project leverages the **Google Gemini AI model** to generate content dynamically and employs a rate-limiting strategy to ensure fair usage.

## Features

- **Dynamic Content Generation**: AI-powered Bible stories, quotes, and verses based on user input.
- **Audio Support**: Convert generated text into audio files uploaded to Cloudinary for easy access.
- **Rate Limiting**: Prevents abuse with a defined limit of 5 requests per minute per user.
- **Conditions**: Get Bible verses tailored to specific emotional conditions.
- **Random Quotes**: Retrieve random inspirational Bible quotes to uplift your day.

## Technologies

- **FastAPI**: Framework for building fast, reliable APIs.
- **Google Gemini**: For generative AI content.
- **Cloudinary**: For storing and accessing audio files.
- **Rate Limiting**: Ensured using custom utilities.

## Documentation

Detailed API documentation is available via Swagger.  
**https://inspire-verse.onrender.com/docs**

---
