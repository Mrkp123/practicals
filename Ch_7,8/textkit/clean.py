
# Convert text into title case after removing extra spaces
def tidy(text):
    return text.strip().title()


# Convert text into lowercase slug
def slug(text):
    return "-".join(text.lower().split())
