
def calculate_token_usage(token_details):
    """
    Calculate and organize token consumption.
    """

    prompt_tokens = token_details.get("prompt_tokens", 0)
    completion_tokens = token_details.get("completion_tokens", 0)
    total_tokens = token_details.get("total_tokens", 0)

    return {
        "Input Tokens": prompt_tokens,
        "Output Tokens": completion_tokens,
        "Total Tokens": total_tokens
    }


def display_token_summary(token_details):
    """
    Generate a readable token usage summary.
    """

    usage = calculate_token_usage(token_details)

    summary = f"""
    Token Usage Summary

    Input Tokens: {usage['Input Tokens']}
    Output Tokens: {usage['Output Tokens']}
    Total Tokens: {usage['Total Tokens']}
    """

    return summary
