# TradeIn - Smart Trading Bot

TradeIn is an intelligent trading bot powered by Deep Q-Learning, designed to analyze cryptocurrency trading patterns and execute trades on preferred platforms like Binance and Upstox. The bot has undergone 2,500,000 steps of training to enhance its trading strategies and decision-making capabilities.

## Features

- **Deep Q-Learning**: Utilizes advanced reinforcement learning techniques to learn effective trading strategies.
- **Trading Execution**: Executes trades on popular platforms such as Binance and Upstox.
- **Web Application Tools**:
  - **Crypto Dashboard**: Displays key metrics and trends for various cryptocurrencies.
  - **Analysis Tool**: Analyzes historical and real-time data to inform trading decisions.
  - **Pattern Visualization Tool**: Visualizes trading patterns to help formulate strategies.
  - **Financial Chatbot**: Provides insights and answers related to cryptocurrency trading.
  - **Alarm-Bot**: Notifies users of significant market changes and alerts set by them.

## Tools and Technologies Used

- **Python**: The primary programming language for development.
- **Streamlit**: Used for building the interactive web application interface.
- **TensorFlow**: Framework for developing and training the deep learning model.
- **Keras**: High-level API for building and training neural networks.
- **Binance API**: Integrates trading functionalities with the Binance platform.
- **Stable Baselines (A2C)**: Implements reinforcement learning algorithms to optimize trading strategies.
- **Gym AnyTrading**: A framework for developing and comparing trading algorithms.

## Getting Started

### Prerequisites

- Python 3.7+
- Libraries: TensorFlow, Keras, Streamlit, gym, stable-baselines3, and Binance API client.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/TradeIn.git
   
2.Navigate to the project directory:

3.Install the required libraries:
    pip install -r requirements.txt

4.Set up your environment variables for Binance API:
    export BINANCE_API_KEY=your_api_key
    export BINANCE_API_SECRET=your_api_secret
    ```
