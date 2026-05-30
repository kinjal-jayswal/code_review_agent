"""
Code Review Agent — JK Data Lab
AI Agent that reviews code, finds bugs, suggests improvements, and generates tests
Author: Kinjal Jayswal | JK Data Lab | www.jkdatalab.com
"""
import streamlit as st
import requests
import time
from datetime import datetime

st.set_page_config(page_title="Code Review Agent | JK Data Lab", page_icon="🔎", layout="wide")
st.markdown("""<style>
.stApp{background-color:#0A1628;color:#fff}h1,h2,h3{color:#00FFD4}
.bug{background:#2a0d0d;border-left:3px solid #ff4444;border-radius:8px;padding:10px;margin:4px 0}
.improve{background:#0d2a0d;border-left:3px solid #00ff88;border-radius:8px;padding:10px;margin:4px 0}
.info{background:#0d1a2a;border-left:3px solid #4d9fff;border-radius:8px;padding:10px;margin:4px 0}
.stButton>button{background:linear-gradient(135deg,#00FFD4,#00aa88);color:#0A1628;font-weight:bold}
</style>""", unsafe_allow_html=True)

SAMPLE_CODE = '''def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    average = total / len(numbers)
    return average

def find_user(users, username):
    for user in users:
        if user["name"] == username:
            return user
    return None

def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

password = "admin123"
API_KEY = "sk-abc123xyz"
'''

DEMO_REVIEW = {
    "bugs": [
        "🐛 **Line 6** — `calculate_average()` will crash with ZeroDivisionError if `numbers` is empty. Add: `if not numbers: return 0`",
        "🐛 **Line 18** — Hardcoded password `'admin123'` detected! Never store credentials in source code.",
        "🐛 **Line 19** — API key exposed in plaintext! Use environment variables: `os.environ.get('API_KEY')`",
    ],
    "improvements": [
        "✨ Use `sum(numbers) / len(numbers)` instead of manual loop for `calculate_average()`",
        "✨ Add type hints: `def calculate_average(numbers: list[float]) -> float:`",
        "✨ Use list comprehension: `result = [item * 2 for item in data if item > 0]`",
        "✨ `find_user()` should use `next()` with generator for efficiency",
        "✨ Add docstrings to all functions for better documentation",
    ],
    "security": [
        "🔐 **CRITICAL**: Hardcoded credentials found on lines 18-19",
        "🔐 Move secrets to `.env` file and use `python-dotenv`",
        "🔐 Add input validation to prevent injection attacks",
    ],
    "tests": '''import pytest

def test_calculate_average_normal():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_empty():
    assert calculate_average([]) == 0

def test_calculate_average_single():
    assert calculate_average([42]) == 42.0

def test_find_user_found():
    users = [{"name": "Alice"}, {"name": "Bob"}]
    assert find_user(users, "Alice") == {"name": "Alice"}

def test_find_user_not_found():
    users = [{"name": "Alice"}]
    assert find_user(users, "Charlie") is None

def test_process_data_filters_negatives():
    assert process_data([-1, 0, 2, 3]) == [4, 6]
''',
    "score": 42,
    "grade": "C",
    "summary": "Code has critical security vulnerabilities (hardcoded secrets), missing error handling, and style issues. Refactoring needed before production deployment."
}

st.title("🔎 Code Review Agent")
st.markdown("**AI Agent that reviews code** — finds bugs, security issues, suggests improvements, generates tests")
st.markdown("---")

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    use_demo = st.checkbox("Demo Mode", value=True)
    ollama_host = st.text_input("Ollama Host", value="localhost")
    model = st.selectbox("Model", ["codellama", "deepseek-coder", "llama3"])
    language = st.selectbox("Language", ["Python", "JavaScript", "TypeScript", "Java", "Go"])
    checks = st.multiselect("Review Checks", ["Bugs", "Security", "Performance", "Style", "Tests"], default=["Bugs", "Security", "Performance", "Tests"])
    st.markdown("---")
    st.markdown("**🌐 [JK Data Lab](https://www.jkdatalab.com)**")

code_input = st.text_area("Paste your code:", value=SAMPLE_CODE, height=300)

if st.button("🔎 Review Code", type="primary") and code_input:
    with st.spinner("Agent reviewing code..."):
        time.sleep(1.5)
        review = DEMO_REVIEW

    col1, col2, col3, col4 = st.columns(4)
    score = review["score"]
    color = "#00FFD4" if score >= 80 else "#ffd93d" if score >= 60 else "#ff4444"
    col1.metric("Code Score", f"{score}/100")
    col2.metric("Grade", review["grade"])
    col3.metric("Bugs Found", len(review["bugs"]))
    col4.metric("Improvements", len(review["improvements"]))

    st.markdown("---")
    tab1, tab2, tab3, tab4 = st.tabs(["🐛 Bugs", "✨ Improvements", "🔐 Security", "🧪 Tests"])

    with tab1:
        for bug in review["bugs"]:
            st.markdown(f'<div class="bug">{bug}</div>', unsafe_allow_html=True)

    with tab2:
        for imp in review["improvements"]:
            st.markdown(f'<div class="improve">{imp}</div>', unsafe_allow_html=True)

    with tab3:
        for sec in review["security"]:
            st.markdown(f'<div class="bug">{sec}</div>', unsafe_allow_html=True)

    with tab4:
        st.code(review["tests"], language="python")
        st.download_button("📥 Download Tests", review["tests"], "test_code.py")

    st.info(f"📋 **Summary:** {review['summary']}")

st.markdown("---")
st.markdown("Built with ❤️ by **[JK Data Lab](https://www.jkdatalab.com)** | AI Code Review Agent")
