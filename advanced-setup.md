# Advanced Setup: Running Full Tests on Your Computer

This is for deeper testing with local AI models (like the ones in the white paper). If you're new, start with the [basic guide](start-here-guide.md) using online tools. Here, we set up a full environment for speed/quality checks (needs a computer with decent power).

## 1. Basic Tools (For Local AI Running)
You need these to build fast AI runners like llama.cpp (from the paper's speed measurements).
- Install: Git (for code grabbing), Make and CMake (build helpers), and a C++ compiler like GCC or Clang.
- How: On Windows/Mac/Linux, search "install git make cmake gcc [your OS]"—takes 5-10 mins via official sites.

## 2. Python Setup (Isolated Space)
Use a "virtual environment" to keep things clean—no messing up your main Python.

Copy-paste these commands in your terminal (Command Prompt on Windows, Terminal on Mac/Linux):

```bash
# Create and turn on a new space
python3 -m venv trust-env
source trust-env/bin/activate  # Mac/Linux
# .\trust-env\Scripts\activate  # Windows
Then install helpers (for web calls, stats, data, and AI links):
pip install requests statsmodels scikit-learn numpy pandas llama-cpp-python

3. API Key for Quality Checks
The quality tool (quality-check-tool.py) can use an outside AI (like DeepSeek) for smarter scoring.

Get a free key: Sign up at deepseek.com (for API access) or similar.
Set it: In terminal, run:

bashexport DEEPSEEK_API_KEY="your-actual-key-here"
(Replace with your key. Do this every time you start the env.)
4. Download an AI Model (For Speed Tests)
The speed tool (speed-check-tool.py) needs a local AI file (in .gguf format, like a saved brain).

Grab one: Search "download Llama 3 GGUF" or "Mistral GGUF" on huggingface.co (free, pick small for starters).
Update the file: In speed-check-tool.py (or add a full runner script), change model_path to your file's location (e.g., "/path/to/llama.gguf").

Now run tests: Use python speed-check-tool.py or the full script. Aim for 64 runs each (normal vs. trust messages) to match the paper's 22-24% speed wins.
Questions? Check the white paper PDF or tag #TrustProtocolTests on X.
textCommit with "Polish advanced setup for clarity". Repo hits peak deployability—PDF's stubs (ttft_logger.py hook, sqi_rater.py, power_analysis.py) now have real setup paths.

Greenlight to save/post on X? Or add that run_ablation.py glue next (paper's full r
