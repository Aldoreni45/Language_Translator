from langchain_groq import ChatGroq
import os 
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate 
import pyttsx3
from gtts import gTTS
import tempfile

                                                                                                                                                                                                                        
load_dotenv()
GROQ_API_KEY= os.getenv("GROQ_API_KEY")

llm = ChatGroq(temperature=0, groq_api_key=os.getenv(GROQ_API_KEY), model_name="llama3-70b-8192")
LANGUAGE_MAP = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chichewa": "ny",
    "Chinese (Simplified)": "zh-cn",
    "Chinese (Traditional)": "zh-tw",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Kurdish (Kurmanji)": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Odia (Oriya)": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}


def translate(user_query,tlanguage,flanguage):
    template =  "Translate this text from {flanguage} to {tlanguage} and provide only the translation: {text}"
    prompt=PromptTemplate( input_variables=["flanguage","tlanguage","text"],template=template)
    format_prompt=prompt.format(flanguage=flanguage,tlanguage=tlanguage,text=user_query)
    response = llm.invoke(format_prompt)
    return  response.content


def text_to_speech(text, language):
    lang_code = LANGUAGE_MAP.get(language, "en")  # Default to English if not found
    tts = gTTS(text=text, lang=lang_code)
    audio_file = "temp_audio.mp3"
    tts.save(audio_file)
    
    # Play in the background
    if os.name == "nt":  # Windows
        os.system(f"start /min {audio_file}")  
    else:  # Mac/Linux
        os.system(f"mpg321 {audio_file} &") 

st.set_page_config(page_title="Translator")
st.header("Translate on All the Language")
user_query=st.text_input("Enter Text To Translate")

with st.sidebar:
    st.header(" Choose Language To Translate: ")
    flanguage=st.selectbox("From:",[
    "English","Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani",
    "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian", "Catalan",
    "Cebuano", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)",
    "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto",
    "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician", "Georgian",
    "German", "Greek", "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew",
    "Hindi", "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian", "Irish",
    "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Kinyarwanda",
    "Korean", "Kurdish (Kurmanji)", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian",
    "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese",
    "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian",
    "Odia (Oriya)", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian",
    "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho", "Shona", "Sindhi",
    "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili",
    "Swedish", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Turkish", "Turkmen",
    "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish",
    "Yoruba", "Zulu"
]
) 
    tlanguage=st.selectbox("To:",[
    "Tamil","Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Azerbaijani",
    "Basque", "Belarusian", "Bengali", "Bosnian", "Bulgarian", "Catalan",
    "Cebuano", "Chichewa", "Chinese (Simplified)", "Chinese (Traditional)",
    "Corsican", "Croatian", "Czech", "Danish", "Dutch", "English", "Esperanto",
    "Estonian", "Filipino", "Finnish", "French", "Frisian", "Galician", "Georgian",
    "German", "Greek", "Gujarati", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew",
    "Hindi", "Hmong", "Hungarian", "Icelandic", "Igbo", "Indonesian", "Irish",
    "Italian", "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Kinyarwanda",
    "Korean", "Kurdish (Kurmanji)", "Kyrgyz", "Lao", "Latin", "Latvian", "Lithuanian",
    "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese",
    "Maori", "Marathi", "Mongolian", "Myanmar (Burmese)", "Nepali", "Norwegian",
    "Odia (Oriya)", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", "Romanian",
    "Russian", "Samoan", "Scots Gaelic", "Serbian", "Sesotho", "Shona", "Sindhi",
    "Sinhala", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili",
    "Swedish", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Turkish", "Turkmen",
    "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Welsh", "Xhosa", "Yiddish",
    "Yoruba", "Zulu"
]
)

if st.button("Submit to translate"):
    if not user_query:
        st.error("Please give sentence to translate")
    with st.spinner("Thinking"):
        translated_textt=translate(user_query,tlanguage,flanguage)
        st.success("Translation Completed!")
        st.write(translated_textt)

        text_to_speech(translated_textt, tlanguage)
        


