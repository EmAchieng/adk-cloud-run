# GDG Cloud Zurich
# adk_cloud_run
A super trivial setup of the ADK (Google's Agent Development Kit), ready to be deployed to Cloud Run as a Docker container.

## Setup and Deployment Instructions

### Prerequisites

*   **Python:** [Download](https://www.python.org/downloads/)
*   **Git:** [Download](https://git-scm.com/downloads)
*   **gcloud CLI:** [Install](https://cloud.google.com/sdk/docs/install)

### Steps

1.  **Claim Google CLoud OnRamp credits** (if provided).
2.  Go to the **Google Cloud Console**: [console.cloud.google.com](https://console.cloud.google.com)
3.  **Create a new Google Cloud project.**
4.  **Authenticate and select your project:**
    ```bash
    gcloud auth login
    gcloud projects list
    gcloud config set project PROJECT_ID
    ```
5.  **Clone the repository:**
    ```bash
    git clone https://github.com/avedave/adk_cloud_run.git
    cd adk_cloud_run
    ```
6.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows CMD:
    # .venv\Scripts\activate.bat
    # On Windows PowerShell:
    # .venv\Scripts\Activate.ps1
    ```
7.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
8.  **Configure your API Key:**
    *   Get your Gemini API Key from [Google AI Studio](https://ai.dev).
    *   Copy `.env.sample` to a new file named `.env`.
    *   Add your `GOOGLE_API_KEY` to the `.env` file.
9.  **Run the agent locally:**
    *   **In the console:**
        ```bash
        adk run multi_tool_agent
        ```
    *   **On the web:**
        ```bash
        adk web
        ```
10. **Deploy to Cloud Run:**
    ```bash
    gcloud run deploy multi-tool-agent --source . --region europe-west1 --allow-unauthenticated --set-env-vars="GOOGLE_GENAI_USE_VERTEXAI=FALSE, GOOGLE_API_KEY="  --labels dev-tutorial=codelab-dos
    ```

Deployment documentation: https://google.github.io/adk-docs/deploy/cloud-run/#python---gcloud-cli
