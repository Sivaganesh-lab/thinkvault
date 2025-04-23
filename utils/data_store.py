import pandas as pd
import os

CSV_PATH = "idea_data.csv"

def save_idea(idea: str, idea_hash: str, timestamp: str):
    if not os.path.exists(CSV_PATH):
        df = pd.DataFrame(columns=["idea", "idea_hash", "timestamp"])
    else:
        df = pd.read_csv(CSV_PATH)
    
    new_entry = {"idea": idea, "idea_hash": idea_hash, "timestamp": timestamp}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(CSV_PATH, index=False)

def verify_hash(hash_to_check: str):
    if not os.path.exists(CSV_PATH):
        return False, "No data yet."

    df = pd.read_csv(CSV_PATH)
    row = df[df["idea_hash"] == hash_to_check]
    
    if not row.empty:
        return True, row.iloc[0].to_dict()
    return False, "Hash not found."
