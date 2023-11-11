# snaptutor
A simple app for providing feedback on textbook reflections. This demonstrates basic assessment qualities using GPT 3.5.

## How to use
The app is configured to run with Flask. If you have Python and Flask, you can clone this repository and run it using `flask run`.

The app takes user input and runs the result using OpenAI's Chat SDK. The system is configured using the following query:

`Students will provide you with short reflections on emerging trends in the business world. Evaluate the reflections in terms of spelling and grammar, and in terms of evidence of critical thought. Provide a grade between 0 and 10, where 0 represents a very poor response and 10 represents a fantastic response.`

The site then writes ChatGPT's response in the space below the button.

## Sample reflections
Need some sample reflections? Consider copying and pasting the following to see ChatGPT's assessement.

### Stronger
> Thomson Reuters has a wide range of digital transformation products and is well-positioned to lead in this space. The  company has some of the leading real-time news sources, which has allowed them to develop advanced natural language processing tools, which they have tailored to professional services automation. They are likely to leverage this advantage, as there are few companies that have both the resources and capabilities to develop novel generative AI, due to the complexity of procuring and retaining vast quantities of novel data.

> I appreciated Walmart's implementation of sustainable practices. Their implementation of LED lighting and sustainable energy will likely have a measurable impact. I am not sure whether this is an example of greenwashing, though, because they provided their statistics in cumulative terms, rather than their annual emissions reductions.

### Weaker
> I think Thomson Reuters provides news. I don't really see how this makes them a technology leader.

> Walmart suuuuucks and its shares are gonna tank. Nobdy buys stuff from them.

## Problems
- OpenAI is a bit slow as of 2023-11-11. I am confident they will fix this over time.
- The prompt is still pretty general. It could use a fine-tuning feature to help it provide more consistent responses.

A huge shout out to the OpenAI Quickstart repository at https://github.com/openai/openai-quickstart-python
