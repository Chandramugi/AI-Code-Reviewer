
import re
import streamlit as st

from reviewer.code_analyzer import run_static_analysis
from reviewer.llm_reviewer import generate_review


# ==========================================
# HELPER FUNCTIONS
# ==========================================


def extract_corrected_code(review):
    """
    Extract Python code blocks from the AI response.
    """

    # Find all Python code blocks in the response
    matches = re.findall(
        r"```(?:python|py)\s*\n(.*?)```",
        review,
        re.IGNORECASE | re.DOTALL
    )

    if matches:
        # Return the last complete Python code block
        return matches[-1].strip()

    return None



def apply_corrected_code():
    """
    Apply AI-generated code to the editor.
    """

    corrected = st.session_state.get("corrected_code")

    if corrected:
        st.session_state["source_code"] = corrected


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# APPLICATION HEADER
# ==========================================

st.title("🤖 AI Code Reviewer")

st.markdown(
    "### Intelligent Python Code Analysis"
)

st.write(
    "Analyze, debug and improve your Python code "
    "using Artificial Intelligence."
)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("Project Information")

    st.write("AI Code Reviewer")

    st.caption("Version 1.0.0")

    st.divider()

    st.subheader("Features")

    st.write("✓ Syntax Analysis")
    st.write("✓ Bug Detection")
    st.write("✓ Code Quality Analysis")
    st.write("✓ AI Code Review")
    st.write("✓ Severity Classification")
    st.write("✓ Corrected Code Generation")
    st.write("✓ Test Case Suggestions")

    st.divider()

    st.caption("Powered by Groq AI and Streamlit")


# ==========================================
# PYTHON CODE EDITOR
# ==========================================

st.subheader("Enter Your Python Code")

code = st.text_area(
    "Python Code Editor",
    height=350,
    placeholder="def hello():\n    print('Hello World')",
    key="source_code"
)


# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button("Analyze & Review Code", type="primary"):

    if not code.strip():

        st.warning("Please enter Python code first.")

    else:

        try:

            # ----------------------------------
            # STEP 1: STATIC ANALYSIS
            # ----------------------------------

            with st.spinner("Running static analysis..."):

                analysis_results = run_static_analysis(code)

            st.divider()

            st.subheader("1. Static Analysis Results")

            syntax = analysis_results["syntax"]

            if syntax["valid"]:

                st.success("No syntax errors detected.")

            else:

                st.error("Python syntax error detected!")

                st.code(syntax["message"])

                st.write(
                    "Error Line:",
                    syntax.get("line", "Unknown")
                )

            # ----------------------------------
            # STEP 2: CODE STATISTICS
            # ----------------------------------

            if syntax["valid"]:

                structure = analysis_results["structure"]

                st.subheader("Code Statistics")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Lines of Code",
                    structure["lines"]
                )

                col2.metric(
                    "Functions",
                    len(structure["functions"])
                )

                col3.metric(
                    "Classes",
                    len(structure["classes"])
                )

                st.write(
                    "Functions:",
                    structure["functions"]
                )

                st.write(
                    "Classes:",
                    structure["classes"]
                )

                st.write(
                    "Imports:",
                    structure["imports"]
                )

                # Pylint results
                st.subheader("Pylint Analysis")

                st.code(
                    analysis_results["quality"]
                )

                score = analysis_results["pylint_score"]

                if score is not None:

                    st.metric(
                        "Pylint Score",
                        f"{score}/10"
                    )

            # ----------------------------------
            # STEP 3: GROQ AI REVIEW
            # ----------------------------------

            st.divider()

            with st.spinner(
                "Groq AI is analyzing your code..."
            ):

                ai_result = generate_review(
                    code,
                    analysis_results
                )

            st.success("AI code review completed!")

            # Display AI review
            st.subheader("2. AI Code Review")

            st.markdown(
                ai_result["review"]
            )

            # ----------------------------------
            # STEP 4: EXTRACT CORRECTED CODE
            # ----------------------------------

            corrected_code = extract_corrected_code(
                ai_result["review"]
            )

            st.divider()

            st.subheader("3. Corrected Python Code")

            if corrected_code:

                # Store corrected code for the apply button
                st.session_state["corrected_code"] = corrected_code

                st.success(
                    "AI-generated corrected code is ready!"
                )

                # Display corrected program
                st.code(
                    corrected_code,
                    language="python"
                )

                # Download corrected program
                st.download_button(
                    label="Download Corrected Code",
                    data=corrected_code,
                    file_name="corrected_code.py",
                    mime="text/x-python"
                )

                # Apply corrected program to editor
                st.button(
                    "Apply Corrected Code to Editor",
                    on_click=apply_corrected_code
                )

                st.caption(
                    "Applying the code replaces the editor contents. "
                    "You can then review or analyze it again."
                )

            else:

                st.warning(
                    "No corrected Python code was found "
                    "in the AI response. Try reviewing again."
                )

            # ----------------------------------
            # STEP 5: TOKEN USAGE
            # ----------------------------------

            st.divider()

            st.subheader("4. Token Usage")

            token_data = ai_result["tokens"]

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Input Tokens",
                token_data["prompt_tokens"]
            )

            col2.metric(
                "Output Tokens",
                token_data["completion_tokens"]
            )

            col3.metric(
                "Total Tokens",
                token_data["total_tokens"]
            )

            st.caption(
                f"AI Model: {ai_result['model']}"
            )

        except Exception as error:

            st.error(
                f"Code review failed: {error}"
            )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "AI Code Reviewer | Python Static Analysis "
    "+ Groq LLM | Version 1.0.0"
)
