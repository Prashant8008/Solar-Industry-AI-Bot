# Solar Industry AI Bot

SolarAI is an advanced AI-powered chatbot designed to provide expert insights into solar energy, installation processes, and market trends. Built using Streamlit and integrated with Google's Gemini API, SolarAI ensures accurate and context-aware responses for both technical and non-technical queries.

## Features

- **AI-Powered Insights**: Delivers tailored responses to solar-related inquiries.
- **Intelligent Query Classification**: Differentiates between technical and general questions.
- **User-Friendly Interface**: Provides an interactive chat experience through Streamlit.
- **Modern UI Design**: Features avatars and a dark-mode-inspired chat interface for enhanced user experience.

## Technologies Used

- **Python**: Backend logic and API integration.
- **Streamlit**: Web-based chatbot interface.
- **Google Gemini API**: AI-powered query resolution.
- **Requests**: Facilitates API interactions.
- **Regular Expressions (re)**: Filters and processes relevant queries.
- **Logging**: Enables debugging and error handling.

## Installation

### Clone the Repository

```sh
git clone https://github.com/your-repo/solar-ai-chatbot.git
cd solar-ai-chatbot
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Set Up API Credentials

1. Obtain a valid **Gemini API Key**.
2. Securely store the API key using environment variables (recommended) or replace `GEMINI_API_KEY` in `chatbot.py`.

### Run the Application

```sh
streamlit run app.py
```

## Project Structure

```
solar-ai-chatbot/
│── Filter.py        # Manage query classification
│── Config.py        # Manages API Key. 
│── app.py           # Streamlit frontend for the chatbot
│── requirements.txt # List of required dependencies
│── README.md        # Documentation
```

## Usage

1. Start the chatbot by running `streamlit run app.py`.
2. Enter a solar energy-related question in the chat interface.
3. Receive intelligent, AI-generated responses.
4. Continue the conversation as needed.

## Example Queries

- **How efficient are monocrystalline solar panels?**
- **What are the advantages of net metering?**
- **How do solar inverters function?**
- **What are the latest trends in the solar energy market?**

## Security Best Practices

- **Protect API Credentials**: Never expose the API key in a public repository.
- **Use Environment Variables**: Store sensitive credentials securely.
- **Input Validation**: Prevent malicious queries by sanitizing user input.

## License

This project is released under the **MIT License**.

