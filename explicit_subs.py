from treat_comments import treat_comments
import json

explicit_subs = list()

def treat_explicit_sub(sub):
    if sub['subreddit_type'] == "public" and sub["over18"]:
        explicit_subs.append(sub["display_name"])


if __name__ == '__main__':
    treat_comments(treat_explicit_sub, "reddit_subreddits.ndjson.zst")

    with open("explicit_subs.json", "w") as f:
        json.dump(explicit_subs, f)