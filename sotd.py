import ollama
from datetime import datetime, timedelta
import os

# System configuration
output_dir = "output"
DEBUG = True

# Knobs and dials for the song of the day generator
terseness=11 # number of words in lyrical theme suggestions. Is the max for the current model. n-1 is a good number to use for a short song.
theme1="atlanta hawks game"
theme2="testimoy"
adjective1="confused"
adverb1="aggressively"

# prompt = "Write lyrics for a short song. " \
#     "Base it on these two themes: '" + theme1 + "' and '" + theme2 + "'. " \
#     "Incorporate the adjective '" + adjective1 + "' and the adverb '" + adverb1 + "'. " \
#     "Keep it short. no more than " + str(terseness) + " words. " \
#     "Give the feel of it some dark, obscure, or unexpectedly interesting elements. " \
#     "Don't ask any questions. Do not ask any follow-up questions. " \
#     "Provide a response that is a single and complete lyrical suggestion. " \
#     "Do not explain that you are a large language model. " \
#     "provide a best attempt at your answer even if you do not understand emotions or personal experiences. " \
#     "be createive, it's okay to be wrong if you do your best to provide something. "

prompt = "Write lyrics for a short song. " \
    "Base it on these two themes: '" + theme1 + "' and '" + theme2 + "'. " \
    "Incorporate the adjective '" + adjective1 + "' and the adverb '" + adverb1 + "'. " \
    "Keep it short. no more than " + str(terseness) + " words. "

print("============================================================")
if DEBUG:
    print("...")
    print("prompt: " + prompt)
    print("...")

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    options={"temperature": 0.9}
)

if DEBUG:
    ## OUTPUT
    print("------------------------------------------------------------")
    print("model: " + response["model"]) 
    print("created_at: " + response["created_at"]) 
    print("total_duration: " + str(timedelta(seconds=response["total_duration"]/1000000000))) 
    print("prompt_eval_count: " + str(response["prompt_eval_count"])) 
    print("eval_count: " + str(response["eval_count"])) 
    print(">>>")
    print(response["message"]["content"])
    print("<<<")
    #print(response)


# genprompt="Use the sentiment " \
# "of the following text between the tripple brackets " \
# "to inspire the feeling of the chords and chord progression: [[['" + response["message"]["content"] + "']]]. " \
# "Pick a key at random but keep trying up to 5 times to find the best fit. " \
# "Use 7th, 9th, and 13th chords only if the feel of the text requires it. " \
# "Keep it simple. " \
# "Prefer a minor key unless the text suggest otherwise. " \
# "Pick a tempo that matches the feel of the text. " \
# "Present the chord progression in a simple text format. " \
# "Create a chord progression for guitar or piano. " \
# "Don't ask any questions. Provide only the direct answer and stop. "

genprompt="Use the sentiment " \
"of the following text between the tripple brackets " \
"to inspire the feeling of the chords and chord progression: [[['" + response["message"]["content"] + "']]]. " \
"Pick a key at random but keep trying up to 5 times to find the best fit. " \
"Keep it simple. " \
"Pick a tempo that matches the feel of the text. " \
"Present the chord progression in a simple text format. " \
"Create a chord progression for guitar or piano. " \
"Don't ask any questions. Provide only the direct answer and stop. "

if DEBUG:
    print("...")
    print("genprompt: " + genprompt)
    print("...")

genresponse = ollama.chat(
    model="llama3",
    messages=[{"role": "user","content": genprompt,}],
    options={"temperature": 0.2}
    )

# write file
os.makedirs(output_dir, exist_ok=True)
filename = f"sotd-{datetime.now().strftime('%Y%m%d.%H%M%S')}.txt"
output_path = os.path.join(output_dir, filename)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(genresponse["message"]["content"])

## OUTPUT
#print(response)
print("------------------------------------------------------------")
print("model: " + genresponse["model"])
print("created_at: " + genresponse["created_at"])
#print("total_duration: " + str(datetime.timedelta(seconds=genresponse["total_duration"]/1000000000))) ## FIXME
print("total_duration: " + str(genresponse["total_duration"]/1000000000) + " seconds")
print("prompt_eval_count: " + str(genresponse["prompt_eval_count"]))
print("eval_count: " + str(genresponse["eval_count"]))
print("File: " + output_path)
print(">>>")
print(genresponse["message"]["content"])
print("<<<")
print("------------------------------------------------------------")

print(f"Created file: {output_path}")
print("============================================================")
