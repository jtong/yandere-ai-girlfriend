import openai


def step(prompt, **kwargs):
    print("/====prompt===\\")
    print(prompt)
    print("\====prompt===/")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.75,
        **kwargs
    )
    print("/====completion===\\")
    print(completion.choices)
    print("\====completion===/")
    return completion.choices[0].message.content
