# script_writer.py

import logging
logging.basicConfig(filename='log.txt', level=logging.INFO)

def generate_script(news_items):
    try:
        script = "📰 नमस्कार दोस्तों, स्वागत है आपके अपने चैनल पर। आइए जानते हैं आज की 5 बड़ी खबरें:\n\n"
        
        for i, news in enumerate(news_items, 1):
            headline = news['headline'].strip()
            summary = news['summary'].strip()
            script += f"🗞️ खबर {i}: {headline}\n👉 {summary}\n\n"

        script += "📌 धन्यवाद! ऐसे ही लेटेस्ट और ज़रूरी खबरों के लिए चैनल को लाइक, शेयर और सब्सक्राइब ज़रूर करें। 🙏"
        logging.info("✅ Script generated successfully.")
        return script
    except Exception as e:
        logging.error(f"❌ Error in generate_script: {str(e)}")
        return "⚠️ स्क्रिप्ट जनरेट करने में त्रुटि हुई।"

# Test example
if __name__ == "__main__":
    sample_news = [
        {"headline": "भारत ने चांद पर नया मिशन भेजा", "summary": "ISRO ने एक और चंद्रयान सफलतापूर्वक लॉन्च किया।"},
        {"headline": "वैश्विक तापमान रिकॉर्ड स्तर पर", "summary": "संयुक्त राष्ट्र ने चेतावनी दी है कि पृथ्वी तेजी से गर्म हो रही है।"}
    ]
    print(generate_script(sample_news))
