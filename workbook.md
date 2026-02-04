# Prompt Engineering Workbook

This workbook guides you through a series of marketing‑oriented prompt engineering exercises.  Each section introduces a technique, provides an example prompt, and offers a space for you to paste your answers.  Fork this repository, open this file in your editor, and use it as a template to record your experiments.  You can run the prompts in any LLM of your choice (ChatGPT, Claude, Gemini, etc.) and copy the generated responses back into the designated sections.

## How to use the workbook

1. **Read the description** to understand the technique and why it matters for marketers.
2. **Copy the provided prompt** into your chosen language model and generate a response.
3. **Paste the model’s answer** into the `Your answer` box under each exercise.
4. **Reflect on the output**: Does the technique improve clarity, precision or creativity?  Note any observations or ideas for improvement.

Feel free to adapt the prompts to your own products or scenarios, but always keep the underlying technique in mind.

---

## Chapter 4 – Zero‑Shot Prompting

**Overview:** In zero‑shot prompting, you ask the model to perform a task without providing any examples.  This method is useful for straightforward tasks where the model can rely on its pre‑existing training.  For marketing, zero‑shot prompts are great for brainstorming slogans, creating taglines or generating simple copy quickly.

### Exercise 1 – Generate slogans for “Morning Gold” coffee

**Prompt:**

> You are a creative advertising copywriter.  Generate five catchy slogans for a new brand of premium, organic coffee called “Morning Gold.”  The target audience is health‑conscious young professionals.

**Your answer:**


**Reflection:** Did the model capture the organic, premium and health‑conscious aspects of the brand?  Which slogans resonate most with the target audience?

---

## Chapter 5 – Few‑Shot Prompting

**Overview:** Few‑shot prompting involves providing a handful of examples to guide the model toward a specific format or style.  This is useful when you need consistent outputs or adherence to brand guidelines, such as sentiment classification, content categorisation or structured product descriptions.

### Exercise 2 – Sentiment analysis of customer comments

**Prompt (few‑shot):**

> Classify the sentiment of the following customer comments.
>
> Comment: “I absolutely love the new user interface!  It’s so much easier to navigate.”  Sentiment: Positive
>
> Comment: “The app keeps crashing after the latest update.  I’m so frustrated.”  Sentiment: Negative
>
> Comment: “The delivery arrived on time as expected.”  Sentiment: Neutral
>
> Comment: “Your customer service is a joke.  I’ve been on hold for an hour.”  Sentiment:

**Your answer (add the sentiment for the last comment):**


**Reflection:** How did the model classify the final comment?  Does the tone match the examples?  Try replacing the examples with your own to see how the classification changes.

---

## Chapter 6 – Chain‑of‑Thought Prompting

**Overview:** Chain‑of‑Thought (CoT) prompting encourages the model to reason through intermediate steps before delivering an answer.  Including phrases like “Let’s think step by step” prompts the model to break down complex problems logically.  This is especially helpful for tasks like budget calculations, ROI analysis and strategic planning.

### Exercise 3 – Calculate campaign ROI

**Prompt:**

> I need to calculate the ROI for our latest campaign.  We spent $5,000 on ads, which generated 200 new customers.  The average lifetime value of a customer is $150.  Our profit margin is 40%.  Calculate the total revenue, total profit and final ROI.  Let’s think step by step.

**Your answer:**


**Reflection:** Did the model break down the steps clearly?  Are the calculations correct?  Try removing “Let’s think step by step” and compare the responses.

---

## Chapter 7 – Prompt Chaining

**Overview:** Complex tasks often benefit from being split into smaller, interconnected prompts.  In prompt chaining, the output of one prompt becomes the input of the next.  This technique allows for greater control over each step and can yield more polished results.

### Exercise 4 – Design a content marketing campaign

Use the following chain of prompts to develop a campaign around email marketing for small businesses.

1. **Ideation:**

   Prompt: “Generate 10 blog post ideas about the benefits of email marketing for small businesses.”

   **Your answer (list the ideas):**

   
2. **Outline:**

   Choose one idea from above (write it here):

   
   Prompt: “Create a detailed outline for a blog post titled ‘Why Email Marketing is the Best Investment for Small Businesses.’”

   **Your answer (outline):**

   
3. **Drafting:**

   Prompt: “Write a 1,500‑word blog post based on the provided outline.”

   **Your answer (first paragraph or a summary of the post):**

   
4. **Social media:**

   Prompt: “Create five engaging social media posts to promote this blog post on LinkedIn and Twitter.”

   **Your answer (list the posts):**


**Reflection:** Did breaking the task into stages produce a more coherent campaign?  Which step added the most value?  How could you improve the chain?

---

## Chapter 8 – Retrieval‑Augmented Generation (RAG)

**Overview:** RAG enables models to consult external knowledge sources during generation.  Instead of relying solely on their training data, models can retrieve relevant documents (e.g. from a website or database) and use them as context.  This technique is powerful for tasks requiring up‑to‑date or proprietary information.

### Exercise 5 – Competitive feature comparison

If you have access to a retrieval‑augmented system (or you can manually gather the information), compare your company’s premium plan against a competitor.

**Instructions:**

1. Find a live page describing your competitor’s product (or imagine one if none are available).
2. Extract the key features of their “Pro” plan and those of your own “Premium” plan (e.g. unlimited storage, 24/7 support, advanced analytics, API access).
3. Use a prompt like:

   > Using the information from the website [URL], create a table comparing the features of their “Pro” plan against our “Premium” plan.  The columns should include the feature and whether it is present in each plan.

**Your answer (paste the comparison table or summary here):**


**Reflection:** How reliable is the information retrieved?  Could the model synthesise the comparison accurately?  If you didn’t have a retrieval system, could you provide the context manually in the prompt?

---

## Chapter 9 – ReAct Prompting

**Overview:** ReAct (“Reasoning and Acting”) is a framework that allows an LLM to both think and interact with external tools.  It combines reasoning (e.g. chain‑of‑thought) with actions like web searches, API calls or sending notifications.  This enables the model to gather information, take action and then continue reasoning.

### Exercise 6 – Dynamic pricing scenario

Although you may not have the actual tools to execute actions, you can simulate the reasoning steps and actions in your response.

**Prompt:**

> Your goal is to ensure our “Wireless Pro” headphones are priced competitively.  Check the price of the “NoiseFree 5000” on competitor‑store.com.  If their price is lower than ours (currently $250), adjust our price to be $5 lower than theirs, but not below our minimum of $220.  Then notify the #pricing channel on Slack of the change.

1. **Thought:** Describe what information you need to gather first.
2. **Action:** Write a pseudo‑code or descriptive step for fetching the competitor’s price.
3. **Thought:** Explain how you will adjust the price based on the result.
4. **Action:** Write a pseudo‑code or descriptive step to set the new price.
5. **Thought:** Summarise what happened and prepare to notify the team.
6. **Action:** Write a pseudo‑code or descriptive step to send a Slack message.

**Your answer (fill in each step):**


**Reflection:** How did structuring the reasoning into thoughts and actions help clarify the workflow?  What external tools would you need to fully automate this scenario?

---

## Chapter 10 – Self‑Consistency and Verification

**Overview:** Large language models can sometimes provide inconsistent answers.  Self‑consistency involves running the same prompt multiple times (with higher randomness) and using a majority vote to decide on the final answer.  Reviewing divergent responses can also reveal hidden assumptions or risks.

### Exercise 7 – Market opportunity analysis

Run the following prompt five times using a high temperature setting (e.g. 0.9) and record each conclusion.

**Prompt:**

> Analyze the potential of the “urban gardening” market for our brand of sustainable home goods.  Consider the market size, growth trends, competitive landscape and our brand alignment.  Conclude with a recommendation: “High Potential,” “Medium Potential,” or “Low Potential.”

**Your answers:**

1. Run 1 conclusion:

2. Run 2 conclusion:

3. Run 3 conclusion:

4. Run 4 conclusion:

5. Run 5 conclusion:


**Majority verdict:**


**Reflection:** Did the responses agree?  What reasoning differences did you notice?  How might you improve the prompt to obtain more consistent answers?

---

## Chapter 11 – Meta‑Prompting and Optimization

**Overview:** Meta‑prompting treats your prompts as artifacts that can be improved over time.  By analysing outputs and iteratively refining your prompt (adding personas, tone directives, structure, etc.), you can optimise performance and better align the output with your goals.

### Exercise 8 – Optimise a blog post prompt

Start with an initial prompt and refine it in two iterations.  After each run, analyse the output and adjust the prompt accordingly.

1. **Version 1:**

   Prompt: “Write a blog post about the benefits of our new software update.”

   **Your answer (summary of the output):**

   **Observation:**

2. **Version 2:** (add persona and audience)

   Prompt: “You are a tech blogger writing for a non‑technical audience.  Write a blog post about the benefits of our new software update, focusing on how it makes life easier for the user.”

   **Your answer (summary of the output):**

   **Observation:**

3. **Version 3:** (add brand voice and format)

   Prompt: “You are a tech blogger for the ‘SimplyTech’ blog, known for its friendly and approachable tone.  Write a 1,000‑word blog post about the benefits of our new software update, focusing on how it makes life easier for the user.  Use headings, bullet points and a conversational style.”

   **Your answer (summary of the output):**

   **Observation:**

**Reflection:** How did each iteration improve the output?  Which version best aligns with your marketing objectives?

---

## Chapter 12 – Multimodal and Advanced Applications

**Overview:** Multimodal models can handle text, images and other media.  Prompting these models involves describing both the visual concept and desired style.  This opens new possibilities for creating integrated marketing experiences.

### Exercise 9 – Visual content generation

Use an image generation model (e.g. DALL‑E 3 or Midjourney) to create a visual asset for a new shoe launch.

**Prompt:**

> Create a photorealistic image of a sleek, minimalist sneaker with glowing neon‑blue soles.  The sneaker should be displayed on a pedestal in a dark, futuristic cityscape setting.  The style should be cinematic and high‑tech.

**Your answer:** (If you generate the image, include a link or embed it; otherwise, describe the image you would expect.)


**Reflection:** How well did the model interpret the description?  Did it match the desired style and mood?  What additional details would you include to refine the output?

---

## Appendix: Your own experiments

Use this section for any additional prompts or techniques you’d like to try.  Feel free to adapt prompts to your industry or campaign needs.  Record your prompts, outputs and reflections below.

