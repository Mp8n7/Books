# Suno Evaluation Metrics

This guide outlines the metrics and scoring system for evaluating Suno AI songs, ranging from prompt quality to lyric authenticity.

## The 1-10 Scoring Scale

*   **1 - Terrible Noise**: Unusable. Hallucinations, extreme robotic artifacts, incoherence, or fails to follow prompt entirely.
*   **3 - Bad**: Technically valid audio but boring, cliché-ridden, or structurally broken. "AI Slop".
*   **5 - Average Pop**: Competent but generic. Sounds like stock music or radio filler. "Suno Default".
*   **7 - Good Music**: Engaging, catchy, or emotionally resonant. Worth a second listen. Good adherence to genre.
*   **8 - Playlist Worthy**: Distinctive character, catchy hook, or genuine emotional weight. You would save this to a playlist.
*   **9 - Nearly Perfect**: Professional quality. Exceptional lyrics, unique production, "human" feel.
*   **10 - Masterpiece**: Defies the "AI" label. Innovative, deeply moving, or a perfect earworm.

---

## Evaluation Categories

### 1. Structural Integrity & Suno Mechanics
*   **Did it follow the prompt?** (Genre, Mood, Vocals)
*   **Did it follow metatags?** (Did the guitar solo happen? Did the beat drop?)
*   **Hallucinations:** Are there random voices or glitches?
*   **Ending:** Did it end cleanly or cut off/fade randomly?

### 2. Lyrical Quality (The "Cringe" Test)
*   **Specificity vs. AI Slop:** Does it use "neon lights", "echoes", "city nights", "digital void"? (Bad) Or specific, grounded details? (Good)
*   **Show vs. Tell:**
    *   *Pop*: 70% Show / 30% Tell.
    *   *Indie/Folk*: 50% Show / 50% Tell.
*   **Rhyme Scheme:** Is it forced (Dr. Seuss style) or natural (slant rhymes)?
*   **Flow/Wordiness:** Are lines too long to sing breathlessly? (Pop: 6-8 words/line).

### 3. Musicality & Vibe
*   **Catchiness:** Is the melody memorable?
*   **Production Quality:** Does it sound "muddy" or "crisp"?
*   **Genre Authenticity:** Does the "Country" song actually sound like Country, or just Pop with a banjo?
*   **Vocal Persona:** Does the voice match the lyrics (e.g., gritty voice for sad lyrics)?

---

## Metric Checklist

**Prompt Evaluation (Pre-Generation):**
- [ ] **Character Count:** Under 1000 chars?
- [ ] **Formatting:** No blank lines in Style Prompt?
- [ ] **Tags:** Are metatags correct (e.g., `[Chorus]` not `(Chorus)`)?
- [ ] **Persona:** Is the vocal description 4-layered (Timbre, Tech, Emotion, Anchor)?

**Song Evaluation (Post-Generation):**
- [ ] **Cringe Factor (1-10):** (10 = No Cringe, 1 = Painful).
- [ ] **Catchiness (1-10):** (10 = Earworm).
- [ ] **Coherence (1-10):** (10 = Perfect structure).
- [ ] **Overall Score (1-10)**

---

## Common "AI Slop" to Avoid (Automatic Deduction)
*   **Tech words**: *neon, circuit, wire, static, glitch, binary, code*.
*   **Vague angst**: *shadows, void, abyss, echoes, silence, darkness*.
*   **Cliché phrases**: *"tears like rain"*, *"dancing in the moonlight"*, *"broken wings"*.

**Penalty:** -1 point for every 3 cliché words found in lyrics.
