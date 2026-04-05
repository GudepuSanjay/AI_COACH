from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from groq_engine import generate_question
from topic_picker import pick_topic
from db import Session, User, Performance

import hashlib

# =========================
# GLOBAL MEMORY
# =========================
user_sessions = {}
user_history = {}
user_topic_history = {}

# =========================
# HASH FUNCTION
# =========================
def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# =========================
# INLINE BUTTONS
# =========================
def build_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("A", callback_data="A"),
         InlineKeyboardButton("B", callback_data="B")],
        [InlineKeyboardButton("C", callback_data="C"),
         InlineKeyboardButton("D", callback_data="D")]
    ])

# =========================
# START
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    db = Session()
    if not db.query(User).filter_by(user_id=user_id).first():
        db.add(User(user_id=user_id))
        db.commit()

    await update.message.reply_text(
        "🔥 IBPS AI Bot Ready\n\n"
        "/practice → Start practice\n"
        "/mock → Full mock test (60 Q)\n"
        "/stop → Show stats"
    )

# =========================
# SEND QUESTION
# =========================
async def send_question(context, user_id):

    # 🔁 Topic rotation
    if user_id not in user_topic_history:
        user_topic_history[user_id] = []

    subject = topic = micro = None

    for _ in range(5):
        subject, topic, micro = pick_topic()
        combo = f"{subject}-{topic}-{micro}"

        if combo not in user_topic_history[user_id]:
            user_topic_history[user_id].append(combo)
            break

    if len(user_topic_history[user_id]) > 10:
        user_topic_history[user_id].pop(0)

    # 🔁 Question uniqueness
    if user_id not in user_history:
        user_history[user_id] = set()

    q = None

    for _ in range(5):
        temp_q = generate_question(subject, topic, micro)

        if not temp_q or "question" not in temp_q:
            continue

        if "fallback" in temp_q["question"].lower():
            continue

        if not isinstance(temp_q.get("options"), dict):
            continue

        q_hash = get_hash(temp_q["question"])

        if q_hash in user_history[user_id]:
            continue

        user_history[user_id].add(q_hash)
        q = temp_q
        break

    if not q:
        await context.bot.send_message(
            chat_id=user_id,
            text="⚠️ Unable to generate question. Try again."
        )
        return

    if user_id not in user_sessions:
        user_sessions[user_id] = {
            "mode": "practice",
            "total": 0,
            "correct": 0,
            "wrong": 0
        }

    # ✅ UPDATED: store options
    user_sessions[user_id]["current"] = {
        "answer": q["answer"],
        "options": q["options"],   # ⭐ IMPORTANT
        "explanation": q["explanation"],
        "subject": subject,
        "topic": topic,
        "micro": micro
    }

    text = f"📘 {subject} → {topic}\n\n{q['question']}\n\n"

    for key in ["A", "B", "C", "D"]:
        text += f"{key}) {q['options'].get(key, 'N/A')}\n"

    await context.bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=build_keyboard()
    )

# =========================
# PRACTICE
# =========================
async def practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    user_sessions[user_id] = {
        "mode": "practice",
        "total": 0,
        "correct": 0,
        "wrong": 0
    }

    await send_question(context, user_id)

# =========================
# MOCK
# =========================
async def mock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    user_sessions[user_id] = {
        "mode": "mock",
        "total": 0,
        "correct": 0,
        "wrong": 0,
        "remaining": 60
    }

    await update.message.reply_text("📝 Mock Test Started (60 Questions)")
    await send_question(context, user_id)

# =========================
# STOP
# =========================
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if user_id not in user_sessions:
        await update.message.reply_text("No active session.")
        return

    s = user_sessions[user_id]
    accuracy = round((s["correct"] / max(1, s["total"])) * 100, 2)

    await update.message.reply_text(f"""📊 Session Summary

Total: {s['total']}
Correct: {s['correct']}
Wrong: {s['wrong']}
Accuracy: {accuracy}%
""")

    del user_sessions[user_id]

# =========================
# HANDLE ANSWER
# =========================
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    try:
        await query.answer()
    except:
        pass

    user_id = str(query.from_user.id)

    if user_id not in user_sessions or "current" not in user_sessions[user_id]:
        await query.message.reply_text("⚠️ Session expired. Use /practice again.")
        return

    session = user_sessions[user_id]
    selected = query.data
    correct = session["current"]["answer"]

    # ✅ NEW: get actual answer text
    options = session["current"]["options"]
    correct_text = options.get(correct, "N/A")

    session["total"] += 1

    explanation = session["current"]["explanation"]

    # ✅ FINAL FORMAT
    if selected == correct:
        session["correct"] += 1

        message = f"""✅ Correct  

Answer: {correct_text}  

📖 Explanation:  
{explanation}
"""

    else:
        session["wrong"] += 1

        message = f"""❌ Wrong  

✅ Correct Answer: {correct_text}  

📖 Explanation:  
{explanation}
"""

    try:
        await query.edit_message_text(message)
    except:
        await context.bot.send_message(
            chat_id=user_id,
            text=message
        )

    # SAVE TO DB
    db = Session()
    db.add(Performance(
        user_id=user_id,
        subject=session["current"]["subject"],
        topic=session["current"]["topic"],
        micro_topic=session["current"]["micro"],
        result="correct" if selected == correct else "wrong"
    ))
    db.commit()

    # MOCK END
    if session["mode"] == "mock":
        session["remaining"] -= 1

        if session["remaining"] == 0:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"""📊 Mock Test Finished

Total: {session['total']}
Correct: {session['correct']}
Wrong: {session['wrong']}
Score: {session['correct']}
"""
            )
            return

    await send_question(context, user_id)

# =========================
# RUN
# =========================
def run_bot(token):
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("practice", practice))
    app.add_handler(CommandHandler("mock", mock))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CallbackQueryHandler(handle_answer))

    return app