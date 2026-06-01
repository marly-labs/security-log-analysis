import pandas as pd

df = pd.read_csv("login_events.csv")

print("=== Login Events Analysis ===")

print("\nTotal events:")
print(len(df))

print("\nSuccessful logins:")
print(len(df[df["status"] == "success"]))

print("\nFailed logins:")
print(len(df[df["status"] == "failed"]))

print("\nTop IP addresses:")
print(df["ip"].value_counts())