import ollama
import datetime

terseness=31 # number of words in lyrical theme suggestions. Is the max for the current model. n-1 is a good number to use for a short song.
theme1="alone"
theme2="trembling"
adjective1="cold"
adverb1="coldly"

prompt = "Suggest lyrical themes for a short song. " \
    "Base it on these two themes: '" + theme1 + "' and '" + theme2 + "'. " \
    "Incorporate the adjective '" + adjective1 + "' and the adverb '" + adverb1 + "'. " \
    "Make it dark. " \
    "Keep it short. no more than " + str(terseness) + " words. " \
    "Don't ask me any more questions, do your best without further input."

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "tool",
            "content": prompt,
        }
    ],
    options={"temperature": 0.0} # low temp seems to bring on more creativity, but also more randomness. 0.0 is more deterministic and less random.
)

## OUTPUT
#print(response)
print("------------------------------------------------------------")
print("model: " + response["model"]) 
print("created_at: " + response["created_at"]) 
print("total_duration: " + str(datetime.timedelta(seconds=response["total_duration"]/1000000000))) 
print("prompt_eval_count: " + str(response["prompt_eval_count"])) 
print("eval_count: " + str(response["eval_count"])) 
print(">>>")
print(response["message"]["content"])
print("<<<")
print("------------------------------------------------------------")


genprompt="Use the ideas, feel, and sentiment " \
"of the following part between the tripple brackets " \
"to inspire the feel of the riff: [[['" + response["message"]["content"] + "']]]. " \
"Pick a key at random but keep trying up to 5 times to find the best fit for the sentiment and feel of the riff. " \
"Use 7th, 9th, and 13th chords only if the feel of the song requires it. " \
"Keep it simple. " \
"Prefer a minor key unless the ideas suggest otherwise. " \
"Pick a tempo that matches the feel of the ideas and riff. " \
"Present the chord progression in a simple text format. " \
"Create a chord progression for guitar or piano. " \
"Don't ask me any more questions, do your best without further input."

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user","content": genprompt,}],
    options={"temperature": 0.0}
    )

## OUTPUT
#print(response)
print("------------------------------------------------------------")
print("model: " + response["model"]) 
print("created_at: " + response["created_at"]) 
print("total_duration: " + str(datetime.timedelta(seconds=response["total_duration"]/1000000000))) 
print("prompt_eval_count: " + str(response["prompt_eval_count"])) 
print("eval_count: " + str(response["eval_count"])) 
print(">>>")
print(response["message"]["content"])
print("<<<")
print("------------------------------------------------------------")