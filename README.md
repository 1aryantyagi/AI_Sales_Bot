# Mindware Solutions - AI Sales Assistant

## Overview
Mindware Solutions AI Sales Assistant is a web-based AI-powered chatbot designed to streamline the sales process by engaging potential customers, analyzing their needs, and providing tailored product recommendations. It leverages OpenAI's GPT-4 for conversational AI and integrates with Stripe for seamless payment processing.

## Features
- **AI-Powered Conversations:** Uses OpenAI's GPT-4 to interact with users and guide them through the sales funnel.
- **Sales Stage Automation:** The AI follows a structured sales process, from introduction to closing the deal.
- **Product Recommendations:** Retrieves product information from a catalog and provides personalized suggestions.
- **Stripe Payment Integration:** Generates secure payment links for transactions.
- **Chat History Management:** Maintains a conversation history for contextual awareness.
- **Responsive Web Interface:** Provides a user-friendly chat interface.

## Project Structure
```
├── app.py                # Main Flask application
├── sales_agent.py        # AI Sales Agent with conversation handling
├── sales_tools.py        # Utility functions for product info, payments, and compatibility checks
├── save_products.py      # Saves product catalog as a JSON file
├── templates
│   ├── index.html        # Frontend UI
├── static
│   ├── styles.css        # Styles for the UI
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Flask
- OpenAI API Key
- Stripe API Key
- Required Python libraries (see below)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/mindware-sales-bot.git
   cd mindware-sales-bot
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API keys:**
   - Open `app.py` and replace the placeholders for OpenAI and Stripe API keys.
   ```python
   stripe.api_key = ""
   os.environ["OPENAI_API_KEY"] = ""
   ```
4. **Run the Flask application:**
   ```bash
   python app.py
   ```
5. **Access the application:**
   - Open a web browser and go to `http://127.0.0.1:5000/`

## Usage
- Start the chatbot and engage in a conversation.
- The AI will ask qualifying questions and recommend products.
- Once a purchase decision is made, the bot generates a Stripe payment link.
- Users can complete the payment via Stripe's secure gateway.

## API Endpoints
| Endpoint       | Method | Description  |
|---------------|--------|--------------|
| `/`           | GET    | Renders the chatbot UI |
| `/process`    | POST   | Processes user input and returns AI response |

## Technologies Used
- **Backend:** Flask, LangChain, OpenAI API
- **Frontend:** HTML, CSS, JavaScript
- **Payments:** Stripe API
- **Data Processing:** JSON, Python utilities

## Future Enhancements
- Integration with CRM for lead tracking
- Multi-language support
- Voice-based interaction
- Advanced analytics and user insights

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## Contact
For any queries, reach out to 1aryantyagi@gmail.com
