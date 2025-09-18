from openai import OpenAI
import json
#from Functions import response_func, build_instructions
import Functions
from datetime import datetime


#streamlit app config
import streamlit as st

st.set_page_config(page_title="LXD Assistant Evaluation App", layout="wide") 
st.title("LXD Assistant Evaluation App")

#load variable from Config
with open("Config.json", "r") as f:
    config = json.load(f)

#Define variable and LMM apply api key
llm = OpenAI(api_key = config["OPENAI_API_KEY"])
role = "You are a Kashida AI LXD"
context = ["Context item 1","Context Item 2"]
reasoning_summary = "detailed"


for key in ["prompt", "agent_resp", "base_resp", "base_resp_text", "agent_resp_text", "LXD_eval"]:
    if key not in st.session_state:
        st.session_state[key] = ""

#set app to have 3 tabs
tab1, tab2, tab3 = st.tabs(["Test Cases", "Create Prompt", "History"])
with tab1:

    #Split view into 2 columns
    col_left, col_right = st.columns([1, 2])

    with col_left: #user inputs column
    
        st.write("## Inputs")

        st.write("### Config")
        # Select LLM Model to use
        model = st.selectbox(
        "Choose Base LLM Model:",
        config["llmmodel"]
        )
        reasoning_effort = st.selectbox("Choose Reasoning Effort:",
        config["reasoning_effort"]
        )
        
        # Prompt Input
        st.write("### Prompt")
        with st.form(key="prompt_input"):
            prompt = st.text_input("Enter Prompt")
            submit_prompt = st.form_submit_button("Submit Prompt")
        if submit_prompt:
            st.success(f"You submitted this prompt: {prompt}")
            st.session_state.prompt = prompt
            #Build Instructions
            base_instructions = ""
            agent_instructions = Functions.build_instructions(role, context)
           #Generate Responses
            base_resp = Functions.response_func(llm, model, prompt, base_instructions, reasoning_effort, reasoning_summary)
            agent_resp = Functions.response_func(llm, model, prompt, agent_instructions, reasoning_effort, reasoning_summary)
            st.session_state.base_resp_text = base_resp.output[1].content[0].text
            st.session_state.agent_resp_text = agent_resp.output[1].content[0].text
            st.session_state.base_resp = base_resp
            st.session_state.agent_resp = agent_resp

        # Evaluation Input       
        with st.form(key="eval_input"):
            st.session_state.LXD_eval = st.text_input("Enter Evaluation")
            submit_eval = st.form_submit_button("Submit Evaluation")
        if submit_eval:
            st.success(f"You submitted this Evaluation: {st.session_state.LXD_eval}")

        save = st.button("Save Results")        

    with col_right: #Outputs column - Test Case Information
        st.write("## Test Case")
        st.write("### Responses")

        col_RespBase, col_RespAgent = st.columns([1, 1])

        with col_RespBase:
            st.write("**Base LLM Response**")
            st.write(st.session_state.base_resp_text)
            st.write(st.session_state.base_resp)
        with col_RespAgent:
            st.write("**Agent Response**")
            st.write(st.session_state.agent_resp_text)
            st.write(st.session_state.agent_resp)
        
    # Save test case outputs to outputs.json            
    if save:
        if st.session_state.base_resp_text and st.session_state.agent_resp_text:
            testcase = {
                "prompt": st.session_state.prompt,
                "base_resp_text": st.session_state.base_resp_text,
                "agent_resp_text": st.session_state.agent_resp_text,
                "evaluation": st.session_state.LXD_eval,
                "timestamp": datetime.now().isoformat()
            }

            with open("Outputs.json", "r+", encoding="utf-8") as g:
                data = json.load(g)
                data.append(testcase)
                g.seek(0)
                json.dump(data, g, indent=4, ensure_ascii=False)
                g.truncate()
        else:
            st.error("No responses available to save. Please submit a prompt first.")

with tab2:
    st.write("## Create New Prompt")
    col_t2_1, col_t2_2 = st.columns([3,1])
    with col_t2_1:
        with st.form(key="new_prompt"):
            st.session_state.user_input = st.text_input("Enter User Prompt")
            create_prompt = st.form_submit_button("Create Prompt")

    with col_t2_2:
        st.text_input("Prompt ID", key = "prompt_id_disp",value = "", disabled=True)
    if create_prompt:
        st.session_state.prompt_id = Functions.get_next_serial("Prompts.json")
        if st.session_state.user_input and st.session_state.prompt_id:
            prompt_obj = {
                "prompt": st.session_state.user_input,
                "id": st.session_state.prompt_id,
                "category": "",
                "timestamp": datetime.now().isoformat()
            }
            with open("Prompts.json", "r+", encoding="utf-8") as e:
                data = json.load(e)
                data.append(prompt_obj)
                e.seek(0)
                json.dump(data, e, indent=4, ensure_ascii=False)
                e.truncate()
            st.toast("Prompt Created")
        else:
            st.error("Prompt was not created")