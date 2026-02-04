# Practical Exercises

The following tasks are designed to help you explore how different prompt engineering techniques influence the outputs of large language models.  Work through them in order or choose those most relevant to your work.  You can execute the prompts using the `run_prompts.py` script or within the provided Jupyter notebook.  Record your observations after each task.

## 1 Adjusting temperature and top‑p

Large language models offer two key parameters that govern randomness: **temperature** and **top‑p**.  Lower values make the model more conservative and repetitive, while higher values encourage creative outputs【781085559410624†L339-L358】.

1. **Write a meta description.** Use the following prompt with two different temperature settings (e.g. 0.2 and 0.8):

   > *Prompt:* “Write a 160‑character meta description for a new line of eco‑friendly running shoes.  Include a call to action.”

   Run the prompt using the `run_prompts.py` script:

   ```bash
   python scripts/run_prompts.py --prompt "Write a 160‑character meta description ..." --temperature 0.2 --top-p 0.95
   python scripts/run_prompts.py --prompt "Write a 160‑character meta description ..." --temperature 0.8 --top-p 0.95
   ```

   Compare the two outputs.  How does the tone, vocabulary and creativity change?  Which one feels more appropriate for your brand?

## 2 Persona & audience pattern

Assigning a persona and audience at the start of your prompt packs multiple instructions into a single sentence【781085559410624†L380-L417】.

2. **Create two introductions.** Use the persona pattern to generate a blog introduction about “the benefits of standing desks for remote workers.”  Compare these variations:

   - *Prompt A:* “You are an experienced SEO copywriter for a general audience.  Write an engaging introduction on the benefits of standing desks for remote workers.”
   - *Prompt B:* “You are a tech‑savvy storyteller targeting health‑conscious entrepreneurs.  Write an engaging introduction on the benefits of standing desks for remote workers.”

   Observe differences in tone, vocabulary and level of detail.  How does the change in persona and audience influence the output?

## 3 Zero‑shot vs one‑shot vs many‑shot

Providing examples (few‑shot prompting) guides the model toward the desired format and improves consistency【781085559410624†L425-L491】.

3. **Generate SEO title tags.** Write SEO‑optimised title tags for a page about “Best vegan restaurants in London.”  Perform the task three times:

   - **Zero‑shot:** Provide no examples.  Prompt: “Create an SEO‑optimised title tag for a webpage about the best vegan restaurants in London.”
   - **One‑shot:** Provide one example.  Prompt: “Example: ‘Top 10 Sushi Restaurants in Tokyo – A Foodie’s Guide.’  Now create an SEO‑optimised title tag for a webpage about the best vegan restaurants in London.”
   - **Many‑shot:** Provide three examples.  Prompt: “Examples: ‘Discover the Best Chefs in Los Angeles – Your Guide to Fine Dining’; ‘Atlanta’s Top Chefs: Who’s Who in the Culinary Scene’; ‘Explore Elite Chefs in Chicago – A Culinary Journey.’  Now create an SEO‑optimised title tag for a webpage about the best vegan restaurants in London.”

   Compare the generated titles.  Does providing examples help the model produce more structured and keyword‑rich tags?

## 4 Follow‑all‑rules instruction

An explicit directive at the start of a prompt can make the model adhere closely to your guidelines【781085559410624†L503-L520】.

4. **Craft a precise meta description.** Use the base prompt:

   > “Write a meta description (max 160 characters) for an app that helps freelancers track invoices.  Include the brand name ‘FastBill’ and a call to action.”

   Then add a first line saying “Follow every instruction exactly.”  Compare the resulting descriptions.  Which version stays closer to the length limit and includes all required elements?

## 5 Question‑refinement pattern

Encouraging the model to ask clarifying questions leads to more comprehensive answers【781085559410624†L522-L534】.

5. **Generate an FAQ.** Draft a prompt to produce an FAQ section for an AI marketing agency.  Use this two‑step approach:

   1. First prompt: “List three clarifying questions you would ask before drafting an FAQ page for an AI marketing agency.”
   2. Based on the questions returned, feed your answers (as the client) back into a second prompt: “Using the information provided, write an FAQ section for our AI marketing agency.”

   How do the clarifying questions improve the relevance and specificity of the FAQ content?

## 6 Iterative precision

Iteratively refining prompts can lead to more precise instructions and better outputs【781085559410624†L548-L568】.

6. **Summarise a case study.** Start with a prompt: “Summarise the key points of our case study showing how Company X increased ecommerce sales by 40 % using email automation.”  Run the prompt and evaluate the output.  Then refine your prompt to specify sections, tone and details, e.g.:

   > “Summarise the case study outlining how Company X increased ecommerce sales by 40 % using email automation.  Organise your summary into three sections—Background, Strategy and Results—and include specific metrics and quotes.”

   Compare the two summaries.  How does the additional structure affect clarity and completeness?

## 7 GEO‑friendly content: explicit relationships and semantic completeness

GEO content is evaluated passage by passage; clear subject–predicate–object relationships, bullet lists and signposting phrases help AI extract information【642233818778557†L117-L160】【323118844044712†L116-L119】.

7. **Rewrite a product description.** Choose a paragraph describing one of your own products or services.  Rewrite it in two ways:

   - **Original:** Copy the paragraph as is.
   - **GEO‑friendly:** Break the information into standalone sentences or bullet points, include signposts like “In summary,” and explicitly state relationships (e.g. “Product X uses sustainable materials to reduce environmental impact”).

   Submit both versions to the model and ask: “Why is this product special?”  Observe which version yields more detailed and accurate citations or summaries.  What changes made the content easier for the model to extract?

## 8 Passage‑level optimisation

Instead of optimising an entire page, GEO focuses on passage‑level relevance【642233818778557†L117-L149】.

8. **Segment long content.** Take a long article or blog post (at least 500 words).  Divide it into smaller passages that each answer a specific question (e.g. “What problem does the product solve?”, “What features does it offer?”, “How is it different from competitors?”).  Run each passage through the model and ask for a summary.  Compare the clarity of summaries from individual passages versus the full article.  Which approach yields more concise and relevant responses?

## 9 Query fan‑out

Generative engines fan out a user’s query into multiple related questions【642233818778557†L146-L149】.

9. **Create a multi‑question passage.** Write a short passage (2–3 paragraphs) that answers several related queries about Generative Engine Optimisation, such as:

   - “What is GEO?”
   - “How does GEO differ from SEO?”
   - “Why does GEO matter for marketers?”

   Use clear subheadings or bullet points.  Ask the model: “Summarise the main points of the following passage.”  Does the passage answer all three questions clearly?  How might you structure it differently to improve coverage?

## 10 Domain‑specific prompts and emotional cues

Role‑based personas and emotional cues can tailor tone and style to the intended audience【990875333465504†L130-L140】【990875333465504†L174-L181】.

10. **Write a press release.** Use this prompt:

   > “You are a PR specialist with a warm and inspiring tone.  Draft a 300‑word press release announcing the launch of our new AI‑powered project management tool.  Highlight its key features, emphasise how it simplifies teamwork and include a motivating call to action.”

   Then try an alternative persona and tone (e.g. “analytical B2B marketer, formal tone”).  Compare how the language and emotional appeal differ between outputs.

Use these exercises to develop an intuition for how prompt design and model settings influence outputs.  Feel free to create your own variations as you become more comfortable with the techniques.
