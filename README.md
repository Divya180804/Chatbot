# AI-Powered IOT Hub


This project explores the integration of Internet of Things (IoT) devices with conversational AI to create a system that allows users to query real-time environmental data through a simple chat interface.

# Key Features:

- **Real**-Time Data Integration: Continuously captures live temperature and humidity data using a DHT11 sensor connected to an Arduino.
- **Conversational AI**: Utilizes the Langchain framework and OpenAI's API to understand natural language queries, maintain context, and generate intelligent, human-like responses.
- **Dynamic Query Handling**: Supports dynamic questions about live conditions ("What's the temperature now?") and historical data ("What was the average humidity in the last hour?").
- **Data Logging**: Stores sensor readings in a local database or file, enabling historical analysis and trend identification.
- **Interactive UI**: Built with Streamlit to provide a clean, accessible, and user-friendly web interface for interacting with the chatbot.

# Worlflow:

- Ensure you have the required dependencies installed.
- Start the Arduino and sensor system to begin data collection.
- Run the Streamlit application script to launch the chatbot UI.
- In the web interface, users can ask questions about the environmental data. The chatbot processes the query, retrieves the necessary data (live or historical), and displays the answer.

# Future Enhancements

- Expand the system by integrating additional sensors (e.g., gas, motion, light) for more comprehensive environmental monitoring.
- Migrate data storage and processing to a cloud platform (like AWS or Azure) for better scalability and accessibility.
- Implement machine learning models for predictive analytics, such as forecasting future temperature or humidity trends.
- Develop a voice-controlled interface or a dedicated mobile application to make the system more accessible.
- Enable integration with smart home ecosystems like Amazon Alexa or Google Home for seamless cross-platform control.





