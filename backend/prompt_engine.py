def build_prompt(role, context, task, rules, output_format):

    prompt = f"""
Analyze the situation and give me a useful output with all the details.

[P1: ROLE]

{role}

--------------------------------------------------

[P2: CONTEXT]

{context}

--------------------------------------------------

[P3: TASK INSTRUCTIONS]

{task}

--------------------------------------------------

[P4: RULES]

{rules}

--------------------------------------------------

[P5: OUTPUT FORMAT]

{output_format}
"""

    return prompt