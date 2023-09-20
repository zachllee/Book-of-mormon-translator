

## Flask Web Application for OpenAI Query

### Prerequisites

- Python
- pip (Python package installer)

### Setup & Running the App

1. **Install Required Packages**:

   To install the required Python packages, open your macOS terminal and run:

   ```bash
   pip install Flask openai
   ```

2. **Save the Flask Code**:

   Save the Flask code to a file named `main.py`.

3. **Set Up HTML Template**:

   - Create a directory named `templates` alongside `main.py`.
   - Inside the `templates` directory, save the provided `index.html` content.

4. **Set Flask Environment Variables**:

   In your terminal, set the `FLASK_APP` environment variable:

   ```bash
   export FLASK_APP=main.py
   ```

5. **Run the App**:

   Start the Flask development server with:

   ```bash
   flask run
   ```

   You should see output indicating the server is running. The output will provide a local URL (usually `http://127.0.0.1:5000/`).

6. **Access the Web Application**:

   Open a web browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

7. **Shutdown**:

   To stop the Flask server, return to your terminal and press `Ctrl+C`.

### Notes:

- Make sure to replace `'YOUR_OPENAI_API_KEY'` in the `main.py` file with your actual OpenAI API key.
- This setup is meant for local development. For production deployment, consider a more robust server setup.

---
