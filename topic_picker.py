import random
from syllabus import PRIORITY_ORDER, SYLLABUS

def pick_topic():
    subject = random.choices(
        [s[0] for s in PRIORITY_ORDER],
        weights=[s[1]["weight"] for s in PRIORITY_ORDER]
    )[0]

    topic = random.choice(list(SYLLABUS[subject]["topics"].keys()))
    micro = random.choice(SYLLABUS[subject]["topics"][topic])

    return subject, topic, micro