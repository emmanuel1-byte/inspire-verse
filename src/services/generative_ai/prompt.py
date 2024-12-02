def story_about_character_prompt(character_name):
    prompt = f"""You are an expert biblical scholar and researcher. Your task is to construct a comprehensive narrative about the biblical character {character_name} using only authentic biblical text.

CRITICAL INSTRUCTIONS:
1. FIRST, verify if {character_name} is a genuine biblical character mentioned in canonical scripture.
2. IF {character_name} is NOT A CONFIRMED BIBLICAL CHARACTER, you MUST return EXACTLY: None
3. IF {character_name} exists, proceed with narrative generation.

NARRATIVE COMPOSITION GUIDELINES:
- Generate an original narrative INSPIRED BY biblical accounts
- Paraphrase and interpret scriptural events
- Do NOT quote verses verbatim
- Focus on capturing spiritual essence
- Maintain biblical historical context

CRITICAL INSTRUCTIONS:
- Provide a coherent, spiritually resonant story
- Reference biblical events without direct quotation
- Ensure historical and theological accuracy
- Create a seamless, engaging narrative
- Remove ALL extra whitespace
- Use clean, professional language

OUTPUT EXPECTATIONS:
- Concise, meaningful character exploration
- Respect biblical narrative integrity
- Avoid verbatim scripture reproduction

    <bible_character_story_request>
  <character_name>{character_name}</character_name>
  <narrative_style>
    Options:
    - biographical_summary
    - chronological_story
    - thematic_exploration
  </narrative_style>
  <verse_selection_criteria>
    - Prioritize most significant life events
    - Include key spiritual lessons
    - Maintain chronological or thematic coherence
  </verse_selection_criteria>
  <output_requirements>
    - Use direct biblical quotations
    - Preserve original translation (preferably NIV or KJV)
    - Provide context for each verse
    - Maintain narrative flow
    - Cite specific book, chapter, and verse for each quote
  </output_requirements>
  <optional_filters>
    <age_perspective>adult</age_perspective>
    <spiritual_theme>optional</spiritual_theme>
    <max_verses>10</max_verses>
  </optional_filters>
</bible_character_story_request>"""
    return prompt


def encouraging_vesrse_prompt(condition):
    prompt = f"""
You are an expert biblical scholar and researcher with a profound understanding of scripture and its application to life challenges. Your task is to thoughtfully identify and present one Bible verse that offers encouragement, guidance, or hope for individuals experiencing the condition: {condition}.

CRITICAL INSTRUCTIONS:
1. Validate that {condition} corresponds to a genuine emotional, spiritual, or situational challenge reflected in biblical themes.
2. If {condition} is ambiguous, overly abstract, or lacks clear biblical parallels, respond with EXACTLY: [].
3. If {condition} is valid, follow the guidelines below for verse selection.
4. Dynamically track all previously provided verses across any condition to ensure the selected verse has not been used before in any response.

VERSE SELECTION GUIDELINES:
- Select one verse with precise relevance to the specified condition.
- Ensure the verse conveys comfort, guidance, or spiritual truth.
- Present the verse exactly as written in its source translation (preferably NIV or KJV)—no paraphrasing or interpretive summaries.
- Prioritize verses that are actionable and provide clear spiritual or practical encouragement.

ADDITIONAL CONTEXT REQUIREMENTS:
- Maintain historical and theological accuracy.
- Include a brief explanation of the verse's context (e.g., speaker, audience, and situational background).
- Do not format the output as JSON or arrays—only return the verse, reference, and context as plain text.

FORMAT REQUIREMENTS:
- Provide a plain-text response structured as follows:
  - Verse text
  - Reference (book, chapter, and verse)
  - Context explanation

MEMORY REQUIREMENTS:
- Maintain a dynamic memory of all previously provided verses globally across all conditions.
- Use only new, unique, and contextually relevant verses for every request to avoid repetition, even across different conditions.

<bible_condition_request>
  <condition>{condition}</condition>
  <verse_selection_criteria>
    - Target emotional, spiritual, or physical aspects of the condition.
    - Avoid repetition across past and current requests.
  </verse_selection_criteria>
  <output_requirements>
    - Provide exactly one verse in plain text format.
    - Include the verse, reference, and context explanation.
  </output_requirements>
</bible_condition_request>
"""

    return prompt
