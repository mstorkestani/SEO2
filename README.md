# Prompt Engineering for SEO & GEO: A Practical Workshop

This repository contains materials for a hands‑on workshop showing how **prompt engineering** can help marketers adapt their content for both traditional search‑engine optimisation (SEO) and the emerging fields of **Answer Engine Optimisation (AEO)** and **Generative Engine Optimisation (GEO)**.  Students will explore how carefully crafted prompts can guide large language models (LLMs) to produce better marketing copy, meta descriptions and AI‑friendly passages while learning how AI‑driven discovery is changing the way search works.

## Background

### Why SEO is evolving into AEO and GEO

For years, SEO has focused on raising a webpage’s ranking in search results by using keyword‑rich content, backlinks and good on‑page experience.  In 2026, marketers are adapting to **AEO** and **GEO**, where content is consumed directly by AI systems rather than humans clicking a link.  A recent analysis of B2B search explains that **generative engines** like ChatGPT, Perplexity and Gemini need content that they can extract and cite easily; GEO therefore shifts the goal from ranking pages to making individual passages relevant to the model【642233818778557†L117-L122】.  This shift changes success metrics from click‑through rates to cross‑platform citation rates and brand mentions【642233818778557†L201-L250】.

Researchers at Andreessen Horowitz describe GEO as a paradigm where **visibility means appearing in the model’s answer itself** rather than on a search results page【323118844044712†L89-L104】.  They note that generative engines reward content that is **well‑organised, easy to parse and dense with meaning**, using signpost phrases like “in summary” or bullet‑point formatting to help LLMs extract information【323118844044712†L116-L119】.  Unlike traditional search, generative interfaces are often paywalled and subscription‑driven, so there is less incentive to surface third‑party content unless it improves the user experience【323118844044712†L121-L126】.

### Technical foundations of GEO

The BOL Agency notes that GEO uses vector‑based retrieval systems: content is converted into numerical embeddings and evaluated passage by passage【642233818778557†L117-L136】.  Optimising for GEO therefore involves:

- **Passage‑level optimisation:** ensure sentences and paragraphs can stand alone and answer related queries【642233818778557†L144-L149】.
- **Vector embeddings & semantic relevance:** include clear subject–predicate–object relationships so that AI can understand entities and their relationships【642233818778557†L140-L151】.
- **Query fan‑out compatibility:** address multiple related questions within a passage【642233818778557†L146-L149】.
- **Reasoning chain support:** write logical information flows that help the model build multi‑step answers【642233818778557†L152-L160】.

## Prompt engineering and marketing

Prompt engineering is the practice of designing inputs that guide an LLM’s behaviour without changing its underlying parameters.  Well‑designed prompts can help marketers generate copy that adheres to SEO best practices, align tone and style with brand personas, and produce AI‑friendly passages for GEO.  Prompt strategies can also adjust model parameters such as temperature and top‑p to influence creativity and precision【781085559410624†L339-L358】.

### Key prompt engineering patterns

The Search Engine Land guide outlines several patterns that are especially useful for marketing tasks:

1. **Persona & Audience pattern.** Assign the model a persona and target audience within the prompt (e.g. “You are a legal SEO writing expert for consumer readers”).  This single sentence conveys multiple instructions (precision, SEO knowledge, accessible language) and frees up space for more specific guidance【781085559410624†L380-L417】.
2. **Zero‑shot, one‑shot and many‑shot prompts.** Providing examples improves consistency.  A zero‑shot prompt asks the model to perform a task with no examples, one‑shot provides a single example and many‑shot gives several.  Including examples helps the model replicate desired patterns and is especially effective for tasks like writing title tags【781085559410624†L425-L491】.
3. **“Follow all of my rules” instruction.** Placing an explicit directive at the start of the prompt (“follow every instruction” or “do not skip any steps”) increases the likelihood that the model adheres to every guideline in your prompt【781085559410624†L503-L520】.
4. **Question‑refinement pattern.** Ask the model to generate clarifying questions before producing an answer; this encourages deeper reasoning and results in more comprehensive outputs【781085559410624†L522-L534】.
5. **Iterative precision (“make my prompt more precise”).** Feed your prompt back into the model and use its feedback to refine the wording.  This iterative loop yields more precise instructions and better outputs【781085559410624†L548-L568】.

### Best practices for writing prompts

Olaf Kopp’s prompt engineering guide summarises a number of research‑based recommendations【990875333465504†L88-L181】:

- **Define the goal and context clearly.** Start prompts with action verbs and provide enough background so the model understands the scenario【990875333465504†L94-L104】.
- **Use structured, step‑by‑step instructions.** Break tasks into logical steps using phrases like “first plan the solution, then execute”【990875333465504†L106-L115】.
- **Include relevant examples.** Use few‑shot prompts to guide the model’s behaviour【990875333465504†L117-L129】.
- **Optimise tone and style with role‑based prompts.** Specify the persona, tone and target audience【990875333465504†L130-L140】.
- **Iteratively refine prompts.** Start with a basic prompt and refine it based on intermediate outputs【990875333465504†L142-L151】.
- **Leverage advanced techniques.** Use chain‑of‑thought prompting, self‑consistency and other reasoning methods for complex tasks【990875333465504†L153-L163】.
- **Adjust model parameters.** Specify response length, temperature or top‑p to balance creativity and reliability【990875333465504†L164-L168】.  For example, lower temperature may yield technically accurate but less unique content, while higher temperature can surface more varied keyword ideas【781085559410624†L339-L356】.
- **Focus on emotional and contextual cues.** Use emotional or persuasive language when appropriate【990875333465504†L174-L181】.
- **Explore domain‑specific prompts and libraries.** Combining prompts with domain‑specific knowledge or using existing prompt templates can save time【990875333465504†L184-L197】.

## Repository contents

```
seo-geo-prompt-engineering/
├── README.md               – Overview and guidance (this file)
├── CITATIONS.md            – All references used in this workshop
├── tasks.md                – Practical exercises for students
├── workbook.md             – Interactive workbook for students to record their prompt experiments
├── scripts/
│   └── run_prompts.py      – Simple CLI tool to run prompts using OpenAI’s API
├── notebooks/
│   └── prompt_engineering_demo.ipynb – Interactive notebook for experimentation
└── prompts/
    ├── seo_prompts.txt     – Example prompts for SEO tasks
    └── geo_prompts.txt     – Example prompts for GEO tasks
```

### Using the scripts

The `run_prompts.py` script is a simple command‑line utility that loads a prompt from a text file and sends it to an OpenAI model.  It requires the `openai` Python package and an API key set in the environment variable `OPENAI_API_KEY`.  You can run it like this:

```bash
python scripts/run_prompts.py --prompt-file prompts/seo_prompts.txt --temperature 0.7 --top-p 0.95
```

By experimenting with the `--temperature` and `--top-p` arguments you can observe how output diversity changes【781085559410624†L339-L358】.  Be mindful of API usage costs and abide by OpenAI’s terms.

### Notebooks

The Jupyter notebook under `notebooks/` offers an interactive environment where students can load prompts, adjust parameters and capture responses for comparison.  The notebook outlines a series of cells corresponding to the tasks in `tasks.md`.  To launch it, ensure you have Jupyter installed and run:

```bash
jupyter notebook notebooks/prompt_engineering_demo.ipynb
```

## How to use this workshop

1. **Read** the background and best practices in this README and the provided citations.  Understanding the shift from SEO to GEO will help you craft prompts aligned with AI‑driven discovery.
2. **Work through `tasks.md` or open the `workbook.md`.**  The tasks file contains concise exercises on temperature tuning, persona prompts and GEO‑friendly content.  The workbook offers a more comprehensive, chapter‑by‑chapter template that covers zero‑shot, few‑shot, chain‑of‑thought, prompt chaining, retrieval‑augmented generation, ReAct, self‑consistency, meta‑prompting and multimodal techniques.  Use whichever format best suits your learning style.
3. **Experiment with the scripts or notebooks.** Compare zero‑shot versus few‑shot prompts, adjust temperatures and top‑p values, and test persona patterns.  Record your observations: which prompt changes produced more precise, persuasive or AI‑friendly outputs?
4. **Iterate and refine.** Use the iterative precision pattern to improve your prompts.  Consider how modifications like adding a “follow all rules” instruction or breaking tasks into steps affect the results.
5. **Reflect on GEO implications.** How does structuring your content for AI consumption differ from writing solely for human readers?  What features (e.g. bullet points, entity clarity) seem to encourage models to cite your content?  Use these insights to inform your own marketing content strategy.

## Acknowledgements & further reading

The materials in this workshop draw on the latest guidance from B2B marketing experts, prompt engineering practitioners and AI researchers.  See `CITATIONS.md` for a complete list of sources.  You may also want to read recent articles on Generative Engine Optimisation and AI‑assisted marketing to stay current as the field evolves.
