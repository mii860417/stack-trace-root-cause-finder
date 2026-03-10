import re
import streamlit as st


TOOL_NAME = "Stack Trace Root Cause Finder"
TOOL_ICON = "🔎"
TOOL_DESCRIPTION = (
    "Paste a stack trace and try to identify the first app-level frame "
    "that may represent the root cause."
)


EXAMPLE_INPUT = """java.lang.NullPointerException
    at android.view.View.performClick(View.java:7125)
    at android.view.View.performClickInternal(View.java:7102)
    at com.example.app.ui.LoginFragment.onLoginClicked(LoginFragment.kt:87)
    at com.example.app.ui.LoginFragment.onViewCreated(LoginFragment.kt:65)
"""


SYSTEM_PREFIXES = (
    "at android.",
    "at androidx.",
    "at java.",
    "at javax.",
    "at kotlin.",
    "at sun.",
    "at dalvik.",
    "at com.android.",
    "at org.jetbrains.",
)


def extract_exception(text):
    match = re.search(r"([A-Za-z0-9_.]+Exception)", text)
    if match:
        return match.group(1)
    return "Unknown"


def extract_frames(text):
    frames = []

    for line in text.splitlines():
        line = line.strip()
        if line.startswith("at "):
            frames.append(line)

    return frames


def is_system_frame(frame):
    return frame.startswith(SYSTEM_PREFIXES)


def find_root_cause(frames):

    for frame in frames:
        if not is_system_frame(frame):
            return frame

    return "Not found"


def extract_file_line(frame):

    match = re.search(r"\(([^()]+:\d+)\)", frame)
    if match:
        return match.group(1)

    return "Unknown"


def analyze_stack_trace(text):

    exception = extract_exception(text)

    frames = extract_frames(text)

    root_frame = find_root_cause(frames)

    file_line = extract_file_line(root_frame)

    return {
        "exception": exception,
        "total_frames": len(frames),
        "root_frame": root_frame,
        "file_line": file_line,
    }


st.set_page_config(
    page_title=TOOL_NAME,
    page_icon=TOOL_ICON,
    layout="centered",
)

st.title(f"{TOOL_ICON} {TOOL_NAME}")
st.caption(TOOL_DESCRIPTION)

with st.expander("Example stack trace"):
    st.code(EXAMPLE_INPUT, language="text")


stack_trace = st.text_area(
    "Stack Trace",
    height=320,
    placeholder="Paste your stack trace here...",
)

col1, col2 = st.columns([1, 1])

with col1:
    analyze_clicked = st.button("Find Root Cause", use_container_width=True)

with col2:
    clear_clicked = st.button("Clear", use_container_width=True)

if clear_clicked:
    st.rerun()

if analyze_clicked:

    if not stack_trace.strip():
        st.warning("Please paste a stack trace first.")

    else:

        result = analyze_stack_trace(stack_trace)

        st.subheader("Analysis Result")

        st.markdown(f"**Exception:** `{result['exception']}`")

        st.markdown(f"**Total Frames:** {result['total_frames']}")

        st.markdown("### Root Cause Candidate")

        st.code(result["root_frame"], language="text")

        st.markdown(f"**File / Line:** `{result['file_line']}`")

st.caption("If this tool helped you, please ⭐ the GitHub repo.")
