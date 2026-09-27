import ollama


theme1="Hot desert air and sun in the distance"
theme2="Trying to find love with a language barrier"
adjective1="hungry to prove yourself"
adverb1="abruptly"


prompt = "Create a short poem. " \
    "Base it on these two themes: '" + theme1 + "' and '" + theme2 + "'. " \
    "Incorporate the adjective '" + adjective1 + "' and the adverb '" + adverb1 + "'. " \
    "Make it dark. " \
    "Keep it short. no more than 26 words. " \
    "Use the sentiment of the poem to create a corresponding song. " \
    "The song is a chord progression which supports the feel of the poem. " \
    "Suggest a key for the song at random. " \
    "Randomly pick between: Major or Minor key. " \
    "Use 7th, 9th, and 13th chords only if the feel of the song requires it. " \
    "Suggest a tempo that fits the sentiment of the poem. " \
    "Show the chord progression in a simple text format. "


response = ollama.chat(
    # model="llama3",
    model="SeekerThe3rd/chatmusician",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    options={"temperature": 0.4},
#    format="json",
)
print(response["message"]["content"])