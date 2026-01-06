import sys
import unicodedata

def count_characters(text):
    """
    Count characters in a way that aligns with typical LLM token/char limits,
    normalizing unicode.
    """
    normalized = unicodedata.normalize('NFC', text)
    return len(normalized)

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_prompt.py 'your prompt text'")
        sys.exit(1)

    prompt = sys.argv[1]
    count = count_characters(prompt)

    print(f"Character count: {count}")
    if count > 1000:
        print(f"WARNING: Over limit by {count - 1000} characters!")
    else:
        print(f"Space remaining: {1000 - count} characters")

if __name__ == "__main__":
    main()
