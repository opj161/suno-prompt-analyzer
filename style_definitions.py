# suno-prompt-analyzer/style_definitions.py

"""
This file contains the Style Personality Dictionary, a curated database that maps
Suno style keywords to their intrinsic semantic qualities. This data provides the
semantic layer for the advanced Prompt Starter Kit, allowing it to generate
rich, context-aware, and highly effective prompts.

Each entry can contain:
- "adjectives": A list of words describing the style's texture and feel.
- "energy": A short phrase describing the typical mood, tempo, or dynamic arc.
- "vocal_style": A description of the common vocal performance associated with the style.
"""

STYLE_PERSONALITY_DICT = {
    # --- Core & Broad Genres ---
    "acoustic": {
        "adjectives": ["intimate", "organic", "unplugged", "warm", "heartfelt"],
        "energy": "gentle and reflective",
        "vocal_style": "raw and emotional"
    },
    "rock": {
        "adjectives": ["driving", "gritty", "energetic", "rebellious"],
        "energy": "raw and powerful",
        "vocal_style": "powerful and anthemic"
    },
    "pop": {
        "adjectives": ["catchy", "polished", "upbeat", "melodic", "radio-ready"],
        "energy": "an uplifting build to a memorable chorus",
        "vocal_style": "clean, polished, and layered"
    },
    "metal": {
        "adjectives": ["aggressive", "heavy", "distorted", "powerful", "technical"],
        "energy": "driving and relentless high-intensity",
        "vocal_style": "ranging from aggressive growls to soaring clean vocals"
    },
    "electronic": {
        "adjectives": ["pulsating", "synthetic", "intricate", "futuristic"],
        "energy": "rhythmic and evolving",
        "vocal_style": "processed or sampled, often with effects"
    },
    "rap": {
        "adjectives": ["lyrical", "rhythmic", "confident", "urban", "boastful"],
        "energy": "a confident and steady flow",
        "vocal_style": "rhythmic and spoken, with a focus on lyrical delivery"
    },
    "hip hop": {
        "adjectives": ["groovy", "sample-based", "rhythmic", "laid-back"],
        "energy": "a head-nodding beat with a strong groove",
        "vocal_style": "a smooth, conversational flow"
    },
    "jazz": {
        "adjectives": ["smooth", "improvisational", "complex", "sophisticated", "soulful"],
        "energy": "a cool, sophisticated, and swinging rhythm",
        "vocal_style": "smooth and soulful, with opportunities for scat improvisation"
    },
    "funk": {
        "adjectives": ["groovy", "rhythmic", "tight", "syncopated", "energetic"],
        "energy": "an infectious and highly danceable groove",
        "vocal_style": "energetic and soulful, often with chanted phrases"
    },
    "country": {
        "adjectives": ["twangy", "heartfelt", "storytelling", "rustic"],
        "energy": "a narrative-driven and honest feel",
        "vocal_style": "clear and earnest, often with a distinct twang or drawl"
    },
    "r&b": {
        "adjectives": ["smooth", "soulful", "sensual", "rhythmic", "modern"],
        "energy": "a slick, polished groove with emotional weight",
        "vocal_style": "silky smooth, with impressive vocal runs and harmonies"
    },
    "soul": {
        "adjectives": ["warm", "emotive", "heartfelt", "passionate", "vintage"],
        "energy": "a deep, emotional groove powered by a tight rhythm section",
        "vocal_style": "powerful, passionate, and full of feeling"
    },
    "blues": {
        "adjectives": ["gritty", "mournful", "raw", "expressive", "twelve-bar"],
        "energy": "a cyclical, heartfelt, and storytelling rhythm",
        "vocal_style": "raw, soulful, and full of grit and emotion"
    },

    # --- Moods & Atmospheres ---
    "dramatic": {
        "adjectives": ["cinematic", "sweeping", "tense", "powerful", "climactic"],
        "energy": "a build from quiet tension to an epic peak",
        "vocal_style": "powerful and dynamic, ranging from a whisper to a belt"
    },
    "ethereal": {
        "adjectives": ["airy", "floating", "reverb-drenched", "dream-like", "shimmering"],
        "energy": "gentle and atmospheric",
        "vocal_style": "soft, breathy, and reverb-drenched"
    },
    "epic": {
        "adjectives": ["massive", "orchestral", "heroic", "sweeping", "grand"],
        "energy": "a constant build to a grand climax",
        "vocal_style": "soaring and operatic, often with a choir"
    },
    "cinematic": {
        "adjectives": ["orchestral", "atmospheric", "storytelling", "sweeping"],
        "energy": "a dynamic arc that tells a story",
        "vocal_style": "often instrumental, or featuring a powerful, emotive choir"
    },
    "ambient": {
        "adjectives": ["atmospheric", "textural", "drifting", "sparse", "calm"],
        "energy": "a slow-evolving soundscape without a strong beat",
    },
    "dark": {
        "adjectives": ["brooding", "ominous", "gothic", "somber", "heavy"],
        "energy": "a tense and melancholic atmosphere",
        "vocal_style": "deep, mournful, or menacing"
    },
    "lo-fi": {
        "adjectives": ["chill", "nostalgic", "warm", "hazy", "relaxed"],
        "energy": "a calm and steady, non-intrusive beat",
        "vocal_style": "often instrumental, or featuring soft, sampled vocal snippets"
    },
    "chill": {
        "adjectives": ["relaxed", "mellow", "laid-back", "smooth", "easygoing"],
        "energy": "a slow, steady, and relaxing groove",
        "vocal_style": "soft and gentle, often with a relaxed delivery"
    },

    # --- Stylistic Sub-genres & Fusions ---
    "synthwave": {
        "adjectives": ["retro", "neon-drenched", "nostalgic", "futuristic", "80s-inspired"],
        "energy": "a steady, cinematic night-driving pulse",
        "vocal_style": "often instrumental, but can include reverb-drenched, emotive vocals"
    },
    "hard rock": {
        "adjectives": ["anthemic", "powerful", "riff-based", "swaggering"],
        "energy": "a mid-tempo, powerful stomp",
        "vocal_style": "strong, raspy, and high-energy"
    },
    "heavy metal": {
        "adjectives": ["heavy", "fast", "aggressive", "powerful", "riff-driven"],
        "energy": "a fast-paced and relentless gallop",
        "vocal_style": "high-pitched and soaring, often operatic"
    },
    "punk": {
        "adjectives": ["raw", "fast", "rebellious", "stripped-down", "energetic"],
        "energy": "a chaotic and high-octane burst",
        "vocal_style": "sneering, shouted, and anti-melodic"
    },
    "folk": {
        "adjectives": ["storytelling", "traditional", "organic", "intimate"],
        "energy": "a focus on narrative and simple melodies",
        "vocal_style": "clear, earnest, and unpolished"
    },
    "gospel": {
        "adjectives": ["uplifting", "soulful", "harmonious", "praise-filled"],
        "energy": "a powerful build of collective joy and spirit",
        "vocal_style": "powerful, soulful lead vocals with a large, dynamic choir"
    },
    "orchestral": {
        "adjectives": ["grand", "sweeping", "symphonic", "lush", "majestic"],
        "energy": "a full dynamic range from pianissimo to fortissimo",
        "vocal_style": "operatic soprano or tenor, or a full classical choir"
    },
    "reggae": {
        "adjectives": ["syncopated", "laid-back", "off-beat", "bass-heavy"],
        "energy": "a relaxed, swaying one-drop rhythm",
        "vocal_style": "melodic and rhythmic chanting with a distinct patois"
    },

    # --- Instrumental Styles ---
    "piano": {
        "adjectives": ["emotive", "elegant", "melancholic", "delicate"],
        "energy": "ranging from sparse and sad to powerfully resonant"
    },
    "guitar": {
        "adjectives": ["riff-based", "melodic", "string-driven", "plucked"],
        "energy": "carrying the main melody or driving rhythm"
    }
}
