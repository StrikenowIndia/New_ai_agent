from random import choice

def fetch_news():
    # Future: connect to a news API
    headlines = {
        "Indian Politics": "भारत में अगले चुनावों को लेकर हलचल तेज़",
        "Global Politics": "अमेरिका और चीन के बीच नई व्यापार वार्ता",
        "India-related Global News": "G7 समिट में भारत की भूमिका पर चर्चा",
        "Local Indian News": "दिल्ली में भारी बारिश, ट्रैफिक प्रभावित"
    }
    topic = choice(list(headlines.keys()))
    return topic, headlines[topic]
