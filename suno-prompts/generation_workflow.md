# Suno Generation Workflow

This skill outlines the iterative process for generating, evaluating, and refining Suno AI songs.

## The Loop

1.  **Generate Prompt**: Create a new Suno prompt based on the user's original idea.
    *   *Inputs*: Original user request + previous iteration feedback.
    *   *Skill*: Use `prompting_guide.md` (Realism Stacks, Personas, etc.).
    *   *Parameters*: Check `prompting_guide.md` for v5-specific ranges (Weirdness/Style) based on genre.
    *   *Output*: A prompt file (markdown).

2.  **Save Prompt**: Save the prompt to `prompts/<project_name>/<iteration>.md`.

3.  **Evaluate (Pre-Generation Simulation)**:
    *   Since I cannot *hear* the audio, I evaluate the **Prompt** and **Lyrics** potential using `evaluation_metrics.md`.
    *   Score the **Lyrics** for specificty, flow, and lack of clichés.
    *   Score the **Style Prompt** for correct formatting and depth.
    *   *Prediction*: Estimate the likely quality (1-10) based on prompt strength.

4.  **Refine (If Score < 7)**:
    *   If the lyrics are too generic ("AI Slop"), rewrite them with more specific imagery.
    *   If the style prompt is too vague, apply a "Realism Stack" or "Vocal Persona".
    *   Adjust **Parameters** if the intent isn't clear (e.g., increase weirdness for blends).
    *   Repeat evaluation.

5.  **Finalize & Save**:
    *   Once the prompt scores >= 7, save it as the final version for this iteration.
    *   Ensure the file includes the **Parameters** section.

6.  **Loop**:
    *   Generate a variant (change tempo, vocal gender, or instrument focus) and repeat.

---

## Special Generation (Every 5th Song)
Every 5th iteration, perform a **Blend Generation**:
*   Take the original idea and mash it with a completely different genre or artist style.
*   *Example*: If doing "Sad Folk", try "Sad Folk x 80s Synthpop".
*   *Goal*: Break the "Genre Gravity Well" and find unique sounds.
*   *Parameter Tip*: Increase **Weirdness** (>60%) and lower **Style Influence** (<40%) to allow the blend to work.

## File Structure
Save prompts as:
`prompts/{project_name}/{song_slug}_v{iteration}.md`

## Usage
To start the loop, provide an **Original Prompt Idea** (e.g., "A song about a space trucker missing his cat").
