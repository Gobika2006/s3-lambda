def calculate_score(text):

    skills = ["python", "aws", "docker", "sql", "java"]

    found = []
    missing = []

    for skill in skills:
        if skill in text:
            found.append(skill)
        else:
            missing.append(skill)

    score = int((len(found)/len(skills))*100)

    return {
        "score": score,
        "found": found,
        "missing": missing,
        "suggestions": "Add missing skills to improve ATS score"
    }
