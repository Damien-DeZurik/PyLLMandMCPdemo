import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "write a song",
        }
    ],
    options={"temperature": 1.0} # low temp seems to bring on more creativity, but also more randomness. 0.0 is more deterministic and less random.
)

print(response["message"]["content"])