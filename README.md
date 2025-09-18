LXD Assistant Evaluator

A prototype Streamlit web app that allows users to:

Submit prompts to an LLM (OpenAI’s Responses API).

Compare the base response vs an agent response (with role & context).

Enter manual evaluations of responses.

Save test cases (prompt, responses, evaluation, timestamp) into a JSON file.

The project is designed as an evaluation framework for AI learning experience design (LXD).

🚀 Features

Prompt input and LLM response display (side-by-side).

Persistent session state using st.session_state.

Unique test case IDs using incremental serial numbers.

Save results into Outputs.json.

Configurable LLM model selection from Config.json.

Encrypted environment file (.env.enc) to protect API keys.

🛠️ Setup
1. Clone the repo
git clone https://github.com/<your-username>/LXD_Assistant_Evaluator.git
cd LXD_Assistant_Evaluator

2. Create a virtual environment
python -m venv venv
# Activate it
# On Windows (PowerShell)
venv\Scripts\Activate.ps1
# On Linux/macOS
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Decrypt environment file

You’ll receive a Fernet key from the project owner.
Set it as an environment variable before running the app:

Windows (PowerShell):

$env:FERNET_KEY="your-fernet-key"


Linux/macOS:

export FERNET_KEY="your-fernet-key"

▶️ Run the app
streamlit run app.py

📂 Project Structure
LXD_Assistant_Evaluator/
│── app.py              # Main Streamlit app
│── Functions.py        # Helper functions (LLM calls, instructions)
│── Config.json         # Config (API model, settings)
│── Outputs.json        # Saved test cases (ignored if private)
│── Prompts.json        # Optional test input store
│── .env.enc            # Encrypted environment secrets (safe to commit)
│── requirements.txt    # Python dependencies
│── .gitignore          # Ignored files
│── README.md           # Project description (this file)

🔒 Security Notes

Do not commit .env (it contains raw API keys).

.env.enc is safe to share — reviewers need the Fernet key privately.

Rotate/revoke API keys if compromised.

✨ Future Improvements

Automated evaluation metrics.

Multi-tab Streamlit interface (for test cases, analytics).

Integration with LangChain for complex prompt composition