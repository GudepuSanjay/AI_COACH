def format_stats(session):
    return f"""
📊 Stats:
Total: {session['total']}
Correct: {session['correct']}
Wrong: {session['wrong']}
"""