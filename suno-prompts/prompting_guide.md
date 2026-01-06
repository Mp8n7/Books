# Suno AI Prompting Guide

This guide covers techniques, structure, and metatags to help you get the best results from Suno AI.

## The Anatomy of a Prompt

Suno generally accepts two main inputs:
1.  **Style Prompt**: Describes the musical genre, instruments, mood, and vocal style.
2.  **Lyrics**: Contains the actual words and **Metatags** (instructions for structure and performance).

### The Sweet Spot for Style Prompts
*   **Length**: 4-7 descriptors is usually optimal. Too few = generic; too many = confused.
*   **Formula**: `[Genre/Sub-genre]`, `[Vocal Style]`, `[Key Instruments]`, `[Mood/Tempo]`
*   **Example**: "80s synthwave, pulsating bass, neon atmosphere, male vocals, driving tempo"

---

## Metatags (The "Code" of Suno)

Metatags are instructions placed within the **Lyrics** field, usually inside square brackets `[]`. They tell the AI how to sing or structure the song.

### Structural Tags
These define the sections of your song.
*   `[Intro]` - Short instrumental start
*   `[Verse]` / `[Verse 1]` - Main storytelling section
*   `[Chorus]` - The main hook, usually higher energy
*   `[Pre-Chorus]` - Buildup to the chorus
*   `[Bridge]` - distinct change in melody/pace, usually towards the end
*   `[Outro]` / `[Fade Out]` - Ending
*   `[Instrumental Break]` / `[Solo]` - Section without vocals

### Vocal Tags
Place these before a section to influence how it is sung.
*   `[Male Vocals]` / `[Female Vocals]`
*   `[Duet]` - Two voices
*   `[Choir]` / `[Backing Vocals]`
*   `[Rap]` / `[Spoken Word]`
*   `[Whisper]` / `[Scream]` / `[Growl]`
*   `[Autotune]`

### Instrumental & Performance Tags
*   `[Guitar Solo]` / `[Synth Solo]`
*   `[Beat Drop]` / `[Bass Drop]`
*   `[Silence]` / `[Pause]` - Creates a stop
*   `[Acoustic]` / `[Unplugged]`
*   `[Heavy]` / `[Distorted]`

---

## Advanced Techniques

### The "Style" Field vs. "Lyrics" Field
*   **Global Style**: Put the main genre and mood in the "Style" field (e.g., "Heavy Metal").
*   **Local Instructions**: Put specific changes in the "Lyrics" field using metatags (e.g., `[Acoustic Intro]` inside a Metal song).

### "Anchoring" to Artists
Suno may block direct artist names, but you can describe their sound:
*   *Instead of "The Weeknd"*: "Dark R&B, falsetto vocals, cinematic synth production, nocturnal vibe"
*   *Instead of "Nirvana"*: "90s Grunge, loud-quiet dynamic, raspy male vocals, distorted guitars"

### Extending Songs
If a song cuts off:
1.  Click **Extend** on the clip you like.
2.  Clear the "Style" field (or keep it if you want the same vibe) and set the timestamp to where it ended.
3.  Add the next section of lyrics (e.g., `[Bridge]` -> `[Chorus]` -> `[Outro]`).

### Instrumental Hallucinations
Sometimes Suno ignores `[Instrumental]` or `[Solo]` tags.
*   *Fix*: Add descriptors like `virtuosic`, `complex`, or specific instrument names in the Style field to reinforce the intent.
*   *Fix*: Try `[Instrumental Interlude]` instead of just `[Instrumental]`.

---

## Example Structure

```text
[Style Prompt]:
Dark Synthwave, Cyberpunk, Aggressive Bass, Female Vocals

[Lyrics Field]:
[Intro]
(Synthesizer arpeggios build up)

[Verse 1]
Neon lights reflect in the rain
Walking down the memory lane

[Pre-Chorus]
Can you feel the static?
It's automatic...

[Chorus]
System overload!
(Explosive energy)
We are losing control!

[Guitar Solo]

[Bridge]
Everything is fading to black...

[Chorus]
System overload!

[Outro]
[Fade Out]
```
