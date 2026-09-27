import ollama

theme1="alone"
theme2="trembling"
adjective1="cold"
adverb1="coldly"

prompt = "Create a short poem. " \
    "Base it on these two themes: '" + theme1 + "' and '" + theme2 + "'. " \
    "Incorporate the adjective '" + adjective1 + "' and the adverb '" + adverb1 + "'. " \
    "Make it dark. " \
    "Keep it short. no more than 26 words. "

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    options={"temperature": 0.0} # low temp seems to bring on more creativity, but also more randomness. 0.0 is more deterministic and less random.
)

print(response["message"]["content"])