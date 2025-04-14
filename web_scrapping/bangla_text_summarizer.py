from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "csebuetnlp/banglat5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

while True:
    text = "৫ আগস্টের পর দেশের অনেক কিছুতেই বদল এসেছে। বদল এসেছে বাংলাদেশ ফুটবল ফেডারেশনেও (বাফুফে)।" \
           " সেটি অবশ্য নিয়ম মেনে নির্বাচনের মাধ্যমেই। তাবিথ আউয়ালের সভাপতিত্বে বাফুফের নতুন নির্বাহী কমিটি দায়িত্ব " \
           "নেওয়ার পর চ্যালেঞ্জ কাপ দিয়ে এরই মধ্যে ঘরোয়া ফুটবল মৌসুম শুরু হয়ে গেছে। মোহামেডানকে হারিয়ে মৌসুমের " \
           "প্রথম শিরোপা জিতেছে বসুন্ধরা কিংস। আজ বেশ কিছু ‘নতুনত্ব’ নিয়ে মাঠে গড়াচ্ছে ঘরোয়া ফুটবলের সবচেয়ে বড় আসর " \
           " প্রিমিয়ার লিগও। দেশের সার্বিক পরিবর্তনের আঁচ প্রিমিয়ার লিগেও কিছু লেগেছে। ‘নতুনত্ব’ বলা আসলে সে কারণেই।" \
           " রাজনৈতিক পটপরিবর্তনের পর ঘরোয়া ফুটবলের সর্বোচ্চ স্তর থেকে নাম প্রত্যাহার করে নিয়েছে আগের মৌসুমগুলোতে " \
           "বড় বাজেটের দল গড়া শেখ রাসেল ক্রীড়া চক্র ও শেখ জামাল ধানমন্ডি ক্লাব।"
    print(len(text.split()))
    # Tokenize input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=70, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Print summary
    print("Bangla Summary:", summary)
    print(len(summary.split()))

    # Get user input to continue or stop
    con = input("Type 'x' to exit or press Enter to continue: ")

    if con == "x":
        break
