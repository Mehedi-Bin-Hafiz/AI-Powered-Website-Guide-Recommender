from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use the google/mt5-small model for both English and Bangla summarization
model_name = "google/mt5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

while True:
    # Example text (can be Bangla or English)
    text = input("give your text: ")
    # Print length of original text
    print(f"Original Text Length: {len(text.split())} words")

    # Tokenize input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=70, min_length=40, length_penalty=2.0, num_beams=4,
                                 early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Print summary
    print("Summary:", summary)
    print(f"Summary Length: {len(summary.split())} words")

    # Get user input to continue or stop
    con = input("Type 'x' to exit or press Enter to continue: ")

    if con == "x":
        break
