# script_writer.py

def generate_script(news_items):
    script = "नमस्कार दोस्तों, आइए जानते हैं आज की बड़ी खबरें:\n\n"
    for i, news in enumerate(news_items, 1):
        script += f"{i}. {news['headline']}\n{news['summary']}\n\n"
    script += "धन्यवाद, और ऐसे ही अपडेट्स के लिए चैनल को सब्सक्राइब करें।"
    return script
