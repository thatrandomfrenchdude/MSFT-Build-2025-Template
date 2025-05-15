# Microsoft Build Edge AI Workshop Template

This repository contains a template for my Microsoft Build Edge AI Workshop on 21 May 2025 at 9:00am.

It is designed to help you set up and run the workshop with ease. The template includes all the necessary files and instructions to get started quickly.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Important Notes](#important-notes)
- [License](#license)

## Prerequisites
- Python 3.8 or later
- AnythingLLM
- LM Studio

## Getting Started
1. Clone the repository:
   ```bash
    git clone https://github.com/thatrandomfrenchdude/MSFT-Build-2025-Template.git

    cd MSFT-Build-2025-Template
    ```
2. Setup a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    pip install -r requirements.txt
    ```
3. Create a `config.yaml` file in the base directory and add the following content:
    ```yaml
    ANYTHING_LLM_API_KEY: "YOUR API KEY"
    ANYTHING_LLM_BASE_URL: "http://localhost:3001/api/v1"
    ANYTHING_LLM_WORKSPACE_SLUG: "YOUR WORKSPACE SLUG"
    LM_STUDIO_API_KEY: "lm-studio"
    LM_STUDIO_URL: "http://localhost:1234/v1"
    MODEL: "hugging-quants/llama-3.2-3b-instruct"
    ```
4. During the workshop, replace the `pass` statements in `src/chatbot_src/chatbot.py` and `src/agent_main.py` with code for the chat loop and agent loop respectively. You can reference the complete code with no changes needed here:
    - [Simple NPU Chatbot](https://github.com/thatrandomfrenchdude/simple-npu-chatbot)
    - [Local Agent](https://github.com/thatrandomfrenchdude/local-agent)

## Usage
- To run the chatbot, execute the following command:
    ```bash
    python src/chatbot_src/chatbot.py
    ```
- To run the local agent, execute the following command:
    ```bash
    python src/agent_main.py
    ```

## Important Notes
- It is recommended that you choose a simple, lowercase name for the AnythingLLM workspace slug for ease of use. Special characters and spaces may cause issues. Should you prefer to use a more complex name, you can confirm the slug using `src/chatbot_src/anything_llm_tools/workspaces.py`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
