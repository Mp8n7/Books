# Suno AI Prompting Guide

This guide covers techniques, structure, and metatags to help you get the best results from Suno AI. It is based on advanced strategies from the [Suno Song Creator Plugin](https://github.com/nwp/suno-song-creator-plugin).

## The Anatomy of a Prompt

Suno generally accepts two main inputs:
1.  **Style Prompt**: Describes the musical genre, instruments, mood, and vocal style.
2.  **Lyrics**: Contains the actual words and **Metatags** (instructions for structure and performance).

### The 1000 Character Limit
Suno has a strict 1000-character limit for the Style Prompt. To maximize quality:
*   **NO BLANK LINES**: Blank lines waste characters. separate sections with newlines but don't leave gaps.
*   **Colon-and-Quotes**: Use `key: "value"` format for clarity (though Suno parses natural text, this structure helps you organize).

**Recommended Structure (concatenated):**
```text
genre: "genre tags here"
vocal: "vocal persona here"
instrumentation: "instruments here"
production: "production values here"
mood: "mood descriptors"
```

---

## Generation Parameters (Weirdness vs. Style)

Beyond the text prompt, setting the right parameters is crucial for steering the model. These ranges are based on research into Suno v5 behaviors (e.g., Jack Righteous Guide).

### Weirdness (Safe → Chaos)
*   **Safe (0-20%)**: Predictable, highly commercial.
*   **Normal (35-55%)**: The baseline for most genres.
*   **High (60-100%)**: Experimental, chaotic. Use for blends or avant-garde.

**Specific V5 Ranges:**
*   **Radio Pop**: 35–50%
*   **Hip-Hop / Trap**: 40–55%
*   **Worship / Gospel**: 25–40%
*   **Orchestral**: 55–70%
*   **Ambient / Experimental**: 70–85%

### Style Influence (Loose → Strong)
*   **Loose (0-30%)**: Open interpretation. Good for incompatible genre blends.
*   **Medium (40-60%)**: Balanced adherence.
*   **Strong (65-100%)**: Strict adherence to prompt tags.

**Specific V5 Ranges:**
*   **Radio Pop**: 65–80% (Strict)
*   **Hip-Hop / Trap**: 55–70%
*   **Worship / Gospel**: 70–85%
*   **Orchestral**: 45–60%
*   **Ambient / Experimental**: 35–55%

---

## Advanced Strategies

### 1. Escaping Genre Gravity Wells
Suno's model has "gravity wells"—strong genres like Pop or Rock that pull everything towards them.
*   **Strategy**: If you want "Old School Hip Hop" but keep getting "Trap", explicitly exclude it in the prompt or use negative prompting if available (or just strong descriptors).
*   **Weird Combinations**: Combine tags that don't normally go together to force the model into creative corners (e.g., "Math Rock Gospel").

### 2. Building Vocal Personas (4 Layers)
Don't just say "Female Vocals". Build a persona:
1.  **Demographics/Timbre**: "Female contralto, husky, nasal"
2.  **Technical Delivery**: "Breathless, staccato phrasing, vocal fry"
3.  **Emotional Context**: "Detached, melancholic, urgent"
4.  **Sonic Anchor**: "Reminiscent of [Artist Style], 90s grunge aesthetic"

### 3. Realism Stacks (For Acoustic/Folk)
To make acoustic instruments sound real, use "recording engineer" language.
*   **Room**: `small room acoustics`, `room tone`, `background noise floor`
*   **Mic**: `close mic presence`, `proximity effect`, `off-axis placement`
*   **Performance**: `fret squeak`, `pick noise`, `breath detail`, `natural timing drift`
*   **Analog**: `tape saturation`, `tube warmth`, `slight wow and flutter`

**Example Realism Stack:**
> "small room acoustics, close mic presence, proximity effect, fret squeak, pick noise, tape saturation, natural dynamics"

### 4. Electronic/Synth Strategies
Realism descriptors hurt electronic music. Instead use:
*   `FM synthesis bass`, `wavetable movement`
*   `sidechain compression`, `low-pass filter sweeps`
*   `clean punch`, `phase-coherent low end`

---

## Metatags (The "Code" of Suno)

Metatags are instructions placed within the **Lyrics** field, usually inside square brackets `[]`.

### Structural Tags
*   `[Intro]`, `[Verse]`, `[Chorus]`, `[Bridge]`, `[Outro]`
*   `[Pre-Chorus]`, `[Hook]`, `[Break]`, `[Interlude]`

### Performance & Stacking
You can "stack" commands with pipes `|`:
*   `[Chorus | Anthemic | Stacked Harmonies]`
*   `[Verse | Whispered | Minimal]`

### Instrumental Tags
*   `[Guitar Solo]`, `[Synth Solo]`, `[Bass Drop]`
*   `[Instrumental Break]`, `[Silence]`

---

## Example: The "Perfect" Acoustic Prompt

**Parameters:**
*   **Weirdness:** 40%
*   **Style Influence:** 60%

**Style Field:**
```text
genre: "indie folk, singer-songwriter, 2020s bedroom pop aesthetic"
vocal: "soft female alto, intimate whisper-to-belt, breathy delivery, slight vocal fry"
instrumentation: "fingerpicked acoustic guitar, warm upright bass, sparse piano"
production: "small room acoustics, close mic presence, proximity effect, fret squeak, tape saturation"
mood: "melancholic, nostalgic, intimate"
```

**Lyrics Field:**
```text
[Intro | acoustic guitar | tape hiss]

[Verse 1]
(Lyrics...)

[Chorus | Double-tracked vocals]
(Lyrics...)
```
