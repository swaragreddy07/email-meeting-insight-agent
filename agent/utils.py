import os

def load_text_files(folder_path: str) -> list[str]:
    emails = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                emails.append(f.read())
    return emails
