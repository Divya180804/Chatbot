import sqlite3
import re
from datetime import datetime

class Chatbot:
    def __init__(self):
        pass

    def generate_response(self, user_query):
        # Check if the query is asking for a specific sensor reading with a timestamp
        match = re.search(r'(\btemperature\b|\bhumidity\b).*?(\d{2}:\d{2}:\d{2}) on (\d{4}-\d{2}-\d{2})', user_query, re.IGNORECASE)
        if match:
            sensor_type = match.group(1).lower()
            time_str = match.group(2)
            date_str = match.group(3)
            timestamp_str = f"{date_str} {time_str}"

            # Convert the timestamp string to a datetime object for consistency
            try:
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                return self.get_sensor_data_at_timestamp(sensor_type, timestamp_str)
            except ValueError:
                return "Invalid date or time format. Please use 'YYYY-MM-DD HH:MM:SS'."

        # If no specific timestamp, respond with the latest reading
        elif "temperature" in user_query.lower():
            return self.get_latest_sensor_data("temperature")
        elif "humidity" in user_query.lower():
            return self.get_latest_sensor_data("humidity")
        else:
            # Default response
            return "I'm sorry, I don't understand the query."

    def get_sensor_data_at_timestamp(self, sensor_type, timestamp):
        # Connect to the database and fetch the data for the given timestamp
        conn = sqlite3.connect('sensor_data.db')
        cursor = conn.cursor()

        # Adjust the query based on the sensor type
        if sensor_type == "temperature":
            query = "SELECT temperature FROM sensor_data WHERE timestamp = ?"
        elif sensor_type == "humidity":
            query = "SELECT humidity FROM sensor_data WHERE timestamp = ?"
        else:
            return "Invalid sensor type. Please specify either 'temperature' or 'humidity'."

        # Execute the query
        cursor.execute(query, (timestamp,))
        data = cursor.fetchone()

        # Close the connection
        conn.close()

        # Return the result if found, otherwise indicate no data
        if data:
            return f"The {sensor_type} reading at {timestamp} was {data[0]}."
        else:
            return "No data found for the specified time and sensor type."

    def get_latest_sensor_data(self, sensor_type):
        # Connect to the database and fetch the latest data for the sensor type
        conn = sqlite3.connect('sensor_data.db')
        cursor = conn.cursor()

        # Adjust the query based on the sensor type
        if sensor_type == "temperature":
            query = "SELECT temperature, timestamp FROM sensor_data ORDER BY timestamp DESC LIMIT 1"
        elif sensor_type == "humidity":
            query = "SELECT humidity, timestamp FROM sensor_data ORDER BY timestamp DESC LIMIT 1"
        else:
            return "Invalid sensor type. Please specify either 'temperature' or 'humidity'."

        # Execute the query
        cursor.execute(query)
        data = cursor.fetchone()

        # Close the connection
        conn.close()

        # Return the result if found, otherwise indicate no data
        if data:
            value, timestamp = data
            return f"The latest {sensor_type} reading is {value} at {timestamp}."
        else:
            return "No sensor data found."
