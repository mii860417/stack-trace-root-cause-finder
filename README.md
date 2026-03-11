# 🔎 Stack Trace Root Cause Finder

A lightweight developer tool that helps identify the likely **root cause from a stack trace**.

This tool analyzes stack traces and highlights the first **application-level stack frame**, which is often the most likely root cause of an exception.

Built with **Python + Streamlit**.

---

# 🚀 Demo

Try the tool online:

https://stack-trace-root-cause-finder.streamlit.app


---

# ❓ Why This Tool Exists

When debugging crashes, stack traces often contain many **framework and system calls**, such as:

- Android framework
- Java runtime
- Kotlin runtime
- AndroidX libraries

Example raw stack trace:

```text
java.lang.NullPointerException
    at android.view.View.performClick(View.java:7125)
    at android.view.View.performClickInternal(View.java:7102)
    at com.example.app.ui.LoginFragment.onLoginClicked(LoginFragment.kt:87)
    at com.example.app.ui.LoginFragment.onViewCreated(LoginFragment.kt:65)
```

The actual root cause is often hidden among many framework calls.

The most important line is usually:

```
com.example.app.ui.LoginFragment.onLoginClicked(LoginFragment.kt:87)
```

This tool automatically finds that line.

# 🧠 Example Output

```
Exception: NullPointerException

Root Cause Candidate:
com.example.app.ui.LoginFragment.onLoginClicked(LoginFragment.kt:87)

File / Line:
LoginFragment.kt:87
```

This helps developers quickly jump to the likely source of the crash.

# ✨ Features

- Detect exception type from stack trace

- Extract stack frames

- Filter framework and system frames

- Identify the most likely root cause frame

- Highlight file name and line number

- Simple and fast analysis

# 🔧 Supported Stack Trace Types

Currently optimized for:

- Android stack traces

- Java stack traces

- Kotlin stack traces

Example system frames automatically filtered:

- `android.*`

- `androidx.*`

- `java.*`

- `kotlin.*`

- `dalvik.*`

# ⚙️ How It Works

The analyzer uses a simple heuristic:

1. Extract exception type

2. Extract all stack frames

3. Filter out system/framework frames

4. Return the first remaining frame

In many real-world crashes, this frame is the best candidate for the root cause.

# 🖥 Run Locally

Install dependencies
```
pip install -r requirements.txt
```

Run the Streamlit app
```
streamlit run app.py
```

Then open your browser:
```
http://localhost:8501
```

# 📁 Project Structure
```
stack-trace-root-cause-finder
│
├── app.py
├── requirements.txt
└── README.md
```

# 🧪 Example Stack Trace
```
java.lang.IllegalStateException: Fragment not attached to a context.
    at androidx.fragment.app.Fragment.requireContext(Fragment.java:900)
    at com.example.app.ProfileFragment.loadProfile(ProfileFragment.kt:31)
    at com.example.app.ProfileFragment.onStart(ProfileFragment.kt:22)
    at android.app.Activity.performStart(Activity.java:8050)
    at java.lang.reflect.Method.invoke(Method.java:566)
```

Expected root cause candidate:

```
com.example.app.ProfileFragment.loadProfile(ProfileFragment.kt:31)
```

# 🔍 Audience

This project targets common developer searches such as:

- stack trace analyzer

- stack trace root cause finder

- android stack trace analyzer

- java stack trace parser

- debugging stack traces

- exception root cause analysis

# 🔗 Related Tools

You may also be interested in:

- Crash Log Analyzer : https://crash-log-analyzer.streamlit.app
- Logcat Error Filter : https://logcat-error-filter.streamlit.app

These tools help developers debug logs more efficiently.
