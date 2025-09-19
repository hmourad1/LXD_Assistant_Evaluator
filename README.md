# LXD AI Assistant Evaluation Tool

### Summary
This prototype Streamlit web app is created as the Capstone project for the AISA Course. 

The prototype is intended to be further developed into an evaluation tool that is essential for the Kashida AI LXD initiative that we are working on at my company, [Kashida](https://kashida-learning.com/). 

The main objective of this app is to allow us to run test cases where a prompt is sent to both a base LLM and to our custom GPT (Kashida AI LXD) using OpenAI's Responses API and then use the data generated to gain insight on further training the custom GPT. 

### Features and Workflows
**Create Prompts:**
Fill "create promts" form >> new prompt is added to the prompts store with a unique id (currently a JSON file)

✨Future Improvements: Add metadata to prompts such as "category" to enhance the insight we can gather when analyzing the data.

**Diplay Prompts**
Feature not yet developed. 

Display the created prompts in an easy to read table inside the app to serve as an accessible reference. 

**Run Text Cases**
Configure test case settings such as LLM model to be used and the reasoning effort >> select prompt from list of predefined prompts >> submit the promt >> display response text from the base LLM and the agent >> Enter human evaluations of responses >>Save test cases (prompt, responses, evaluation, timestamp) into a the outputs store (currently a JSON file).

✨Future Improvements: 

Human evaluation is currently just a text input, this will evolve into a rating metrix aligned with the AI evaluation metrics we develop further down the line. See more below about AI Evaluation. 

Utilizing LangChain or similar for complex prompt composition and testing multiple prompt chains for improved results. 

**Run AI Evaluation**
Feature not yet developed. 

Utilize an LLM evaluation framework such as OpenAI Evals, DeepEval etc to evaluate the responses against metrics we specify. 

**Data analysis further usage**
The datasets generated from the evaluations will be analyzed to gain insight on the improvements to be made on the custom GPT and evidence based decisions on whether to include a RAG system or any other extensions that would improve the results. 


🚀**Additional code Features**

Prompt input and LLM response display (side-by-side).

Persistent session state using st.session_state.

Unique test case IDs using incremental serial numbers.

Save results into Outputs.json.

Configurable LLM model selection from Config.json.

Encrypted environment file (.env.enc) to protect API keys.

### Setup 

1. Clone the repo
git clone https://github.com/<your-username>/LXD_Assistant_Evaluator.git
cd LXD_Assistant_Evaluator

2. Create a virtual environment
python -m venv venv
**Activate it**
**On Windows (PowerShell)**
venv\Scripts\Activate.ps1
**On Linux/macOS**
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

### Project Structure
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
