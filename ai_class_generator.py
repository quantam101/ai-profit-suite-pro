def generate_class(topic):
    class_outline = {
        "title": f"Mastering {topic}",
        "lessons": ["Intro", "Why It Matters", "Tools You Need", "Case Studies"],
        "cta": "Join now at alreadyherepro.com/classes"
    }
    with open(f"classes/{topic.replace(' ', '_')}.txt", "w") as f:
        for k, v in class_outline.items():
            f.write(f"{k}: {v}\n")
    print(f"Class on {topic} created.")
