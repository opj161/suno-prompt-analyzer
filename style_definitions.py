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
    "pop": {
        "adjectives": ["catchy", "polished", "upbeat", "melodic", "radio-ready"],
        "energy": "an uplifting build to a memorable chorus",
        "vocal_style": "clean, polished, and layered"
    },
    "rock": {
        "adjectives": ["driving", "gritty", "energetic", "rebellious"],
        "energy": "raw and powerful",
        "vocal_style": "powerful and anthemic"
    },
    "rap": {
        "adjectives": ["lyrical", "rhythmic", "confident", "urban", "boastful"],
        "energy": "a confident and steady flow",
        "vocal_style": "rhythmic and spoken, with a focus on lyrical delivery"
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
    "hip hop": {
        "adjectives": ["groovy", "sample-based", "rhythmic", "laid-back"],
        "energy": "a head-nodding beat with a strong groove",
        "vocal_style": "a smooth, conversational flow"
    },
    "acoustic": {
        "adjectives": ["intimate", "organic", "unplugged", "warm", "heartfelt"],
        "energy": "gentle and reflective",
        "vocal_style": "raw and emotional"
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
    "trap": {
        "adjectives": ["rhythmic", "bass-heavy", "syncopated", "modern", "dark"],
        "energy": "driven by deep 808 kick drums and complex, skittering hi-hat patterns",
        "vocal_style": "often auto-tuned, rhythmic, with a mumble or melodic flow"
    },
    "ballad": {
        "adjectives": ["slow", "narrative", "emotional", "sentimental", "sweeping"],
        "energy": "a slow tempo building to a powerful, emotional chorus",
        "vocal_style": "clear, emotional storytelling, often with a wide dynamic range"
    },
    "indie": {
        "adjectives": ["independent", "raw", "DIY", "alternative", "authentic"],
        "energy": "a less polished, more authentic sound than mainstream music",
        "vocal_style": "varied, but often more personal and less produced; can be understated or quirky"
    },

    # --- Moods & Atmospheres ---
    "upbeat": {
        "adjectives": ["cheerful", "lively", "optimistic", "bouncy", "bright"],
        "energy": "a bright and positive feel-good tempo"
    },
    "melodic": {
        "adjectives": ["tuneful", "lyrical", "song-like", "harmonious"],
        "energy": "a focus on a strong, memorable melody line"
    },
    "dark": {
        "adjectives": ["brooding", "ominous", "gothic", "somber", "heavy"],
        "energy": "a tense and melancholic atmosphere",
        "vocal_style": "deep, mournful, or menacing"
    },
    "epic": {
        "adjectives": ["massive", "orchestral", "heroic", "sweeping", "grand"],
        "energy": "a constant build to a grand climax",
        "vocal_style": "soaring and operatic, often with a choir"
    },
    "emotional": {
        "adjectives": ["expressive", "moving", "passionate", "heart-on-sleeve", "poignant"],
        "energy": "a dynamic arc that builds to a powerful emotional peak",
        "vocal_style": "full of feeling, from a gentle whisper to a powerful belt"
    },
    "aggressive": {
        "adjectives": ["harsh", "abrasive", "confrontational", "intense", "furious"],
        "energy": "a relentless and high-energy sonic assault",
        "vocal_style": "shouted, growled, snarled, or rapped with force"
    },
    "atmospheric": {
        "adjectives": ["textural", "drifting", "spacious", "immersive"],
        "energy": "a soundscape that prioritizes mood over a strong beat"
    },
    "catchy": {
        "adjectives": ["memorable", "hook-filled", "repetitive", "singable", "infectious"],
        "energy": "focused on a melodic or rhythmic hook that sticks in your head"
    },
    "sad": {
        "adjectives": ["mournful", "somber", "tearful", "melancholy", "heartbreaking"],
        "energy": "a slow and sorrowful pace",
        "vocal_style": "sorrowful and full of pathos"
    },
    "dreamy": {
        "adjectives": ["hazy", "surreal", "drifting", "nostalgic", "shimmering"],
        "energy": "a gentle, floating atmosphere",
        "vocal_style": "soft, washed-out, and ethereal"
    },
    "powerful": {
        "adjectives": ["strong", "commanding", "impactful", "forceful", "dynamic"],
        "energy": "a driving and assertive presence with a wide dynamic range",
        "vocal_style": "strong, confident, and resonant"
    },
    "uplifting": {
        "adjectives": ["inspiring", "hopeful", "positive", "soaring", "joyful"],
        "energy": "a build towards a euphoric and optimistic climax",
        "vocal_style": "soaring and inspirational, often with layered harmonies"
    },
    "chill": {
        "adjectives": ["relaxed", "mellow", "laid-back", "smooth", "easygoing"],
        "energy": "a slow, steady, and relaxing groove",
        "vocal_style": "soft and gentle, often with a relaxed delivery"
    },
    "romantic": {
        "adjectives": ["passionate", "intimate", "sentimental", "loving", "sensual"],
        "energy": "a warm and gentle mood, often building to a passionate peak",
        "vocal_style": "soft, intimate, and full of heartfelt emotion"
    },
    "energetic": {
        "adjectives": ["high-energy", "fast-paced", "vibrant", "dynamic", "propulsive"],
        "energy": "a driving, propulsive rhythm that invites movement"
    },
    "melancholic": {
        "adjectives": ["wistful", "somber", "reflective", "downcast", "plaintive"],
        "energy": "a gentle and sorrowful atmosphere",
        "vocal_style": "subdued, mournful, and full of longing"
    },
    "intense": {
        "adjectives": ["unrelenting", "dramatic", "urgent", "fervent", "pounding"],
        "energy": "a constant state of high tension and power"
    },
    "smooth": {
        "adjectives": ["silky", "polished", "relaxed", "sensual", "fluid"],
        "energy": "a laid-back and sophisticated groove",
        "vocal_style": "soft, breathy, and effortless"
    },
    "psychedelic": {
        "adjectives": ["trippy", "mind-bending", "surreal", "experimental", "hazy"],
        "energy": "a swirling, otherworldly soundscape with unexpected shifts",
        "vocal_style": "often washed in effects like reverb and delay, creating a sense of distance"
    },
    "mellow": {
        "adjectives": ["gentle", "calm", "subdued", "relaxed", "soft"],
        "energy": "a slow and easygoing pace with soft dynamics"
    },
    "groovy": {
        "adjectives": ["rhythmic", "funky", "danceable", "infectious", "syncopated"],
        "energy": "driven by a strong, repetitive bass and drum groove that makes you want to move"
    },
    "anthemic": {
        "adjectives": ["big", "singalong", "unifying", "uplifting", "epic"],
        "energy": "a build-up to a massive, crowd-pleasing chorus",
        "vocal_style": "powerful, designed for a stadium to sing along"
    },
    "cinematic": {
        "adjectives": ["soundtrack-like", "sweeping", "atmospheric", "orchestral", "grand"],
        "energy": "a track that tells a story and evokes strong visual imagery"
    },
    "heartfelt": {
        "adjectives": ["sincere", "emotional", "earnest", "genuine", "authentic"],
        "energy": "an honest and deeply emotional delivery",
        "vocal_style": "sincere and full of raw feeling, without pretense"
    },
    "ethereal": {
        "adjectives": ["airy", "floating", "reverb-drenched", "dream-like", "shimmering"],
        "energy": "gentle and atmospheric",
        "vocal_style": "soft, breathy, and reverb-drenched"
    },
    "dramatic": {
        "adjectives": ["cinematic", "sweeping", "tense", "powerful", "climactic"],
        "energy": "a build from quiet tension to an epic peak",
        "vocal_style": "powerful and dynamic, ranging from a whisper to a belt"
    },
    "deep": {
        "adjectives": ["resonant", "low-frequency", "thoughtful", "immersive", "profound"],
        "energy": "a focus on sub-bass frequencies and a contemplative, serious mood"
    },
    "futuristic": {
        "adjectives": ["sci-fi", "synthetic", "innovative", "experimental", "cybernetic"],
        "energy": "a sound palette that feels ahead of its time, often with electronic textures"
    },

    # --- Vocal Styles ---
    "male voice": {
        "adjectives": ["masculine", "resonant", "baritone", "tenor"],
        "energy": "a male-fronted vocal performance",
        "vocal_style": "can range from soft and gentle to powerful and aggressive"
    },
    "female voice": {
        "adjectives": ["feminine", "soprano", "alto", "ethereal"],
        "energy": "a female-fronted vocal performance",
        "vocal_style": "can range from breathy and delicate to a powerful belt"
    },
    "male vocals": {
        "adjectives": ["masculine", "harmonized", "layered", "baritone"],
        "energy": "a focus on male vocal parts, including leads and harmonies",
        "vocal_style": "often implies multiple male singers or layered vocal tracks"
    },
    "female vocals": {
        "adjectives": ["feminine", "harmonized", "layered", "soprano"],
        "energy": "a focus on female vocal parts, including leads and harmonies",
        "vocal_style": "often implies multiple female singers or layered vocal tracks"
    },
    "female singer": {
        "adjectives": ["solo", "frontwoman", "diva", "songstress"],
        "energy": "a track led by a single female performer",
        "vocal_style": "the singular focus of the song's emotional delivery"
    },
    "vocaloid": {
        "adjectives": ["synthetic", "digital", "anime-style", "futuristic", "high-pitched"],
        "energy": "vocals provided by singing synthesizer software",
        "vocal_style": "perfectly pitched, often fast-paced and distinctly non-human"
    },
    "opera": {
        "adjectives": ["classical", "dramatic", "virtuosic", "theatrical", "powerful"],
        "energy": "a grand, theatrical performance",
        "vocal_style": "highly trained, powerful, and unamplified classical singing"
    },

    # --- Tempo & Pacing ---
    "slow": {
        "adjectives": ["leisurely", "unhurried", "gentle", "adagio", "largo"],
        "energy": "a relaxed tempo, often creating a calm or sad mood"
    },
    "fast": {
        "adjectives": ["high-tempo", "rapid", "allegro", "frantic", "driving"],
        "energy": "a quick pace that creates excitement and energy"
    },

    # --- Eras & Time Periods ---
    "80s": {
        "adjectives": ["bright", "synthetic", "gated-reverb", "nostalgic", "anthemic"],
        "energy": "a vibrant and often dramatic feel with prominent synths and drums",
        "vocal_style": "big, reverb-heavy, and often featuring powerful harmonies"
    },
    "90s": {
        "adjectives": ["alternative", "gritty", "cynical", "melodic", "raw"],
        "energy": "a raw and less-polished feel, spanning from grunge to pop-punk",
        "vocal_style": "either angsty and raw or poppy and melodic, defining the decade's contrast"
    },

    # --- Stylistic Sub-genres & Fusions ---
    "hard rock": {
        "adjectives": ["anthemic", "powerful", "riff-based", "swaggering", "gritty"],
        "energy": "a mid-tempo, powerful stomp driven by electric guitar riffs",
        "vocal_style": "strong, raspy, and high-energy"
    },
    "synthwave": {
        "adjectives": ["retro", "neon-drenched", "nostalgic", "futuristic", "80s-inspired"],
        "energy": "a steady, cinematic night-driving pulse",
        "vocal_style": "often instrumental, but can include reverb-drenched, emotive vocals"
    },
    "dance": {
        "adjectives": ["rhythmic", "four-on-the-floor", "club-ready", "energetic"],
        "energy": "a strong, consistent beat designed for dancing"
    },
    "heavy metal": {
        "adjectives": ["heavy", "fast", "aggressive", "powerful", "riff-driven"],
        "energy": "a fast-paced and relentless gallop",
        "vocal_style": "high-pitched and soaring, often operatic"
    },
    "lo-fi": {
        "adjectives": ["chill", "nostalgic", "warm", "hazy", "relaxed"],
        "energy": "a calm and steady, non-intrusive beat, often with vinyl crackle",
        "vocal_style": "often instrumental, or featuring soft, sampled vocal snippets"
    },
    "techno": {
        "adjectives": ["driving", "minimal", "hypnotic", "industrial", "repetitive"],
        "energy": "a relentless and repetitive pulse",
        "vocal_style": "often instrumental, or featuring sparse, processed vocal chops"
    },
    "punk": {
        "adjectives": ["raw", "fast", "rebellious", "stripped-down", "energetic"],
        "energy": "a chaotic and high-octane burst",
        "vocal_style": "shouted, sneering, and anti-authoritarian"
    },
    "reggae": {
        "adjectives": ["syncopated", "laid-back", "off-beat", "bass-heavy", "skanking"],
        "energy": "a relaxed, swaying one-drop rhythm",
        "vocal_style": "melodic and rhythmic chanting with a distinct patois"
    },
    "alternative rock": {
        "adjectives": ["angsty", "melodic", "dynamic", "introspective", "distorted"],
        "energy": "a loud-quiet-loud dynamic shift",
        "vocal_style": "introspective and often cynical"
    },
    "emo": {
        "adjectives": ["emotional", "confessional", "melodramatic", "heartfelt", "dynamic"],
        "energy": "a dynamic build from quiet verses to a cathartic, loud chorus",
        "vocal_style": "earnest, heartfelt, and often strained with emotion"
    },
    "grunge": {
        "adjectives": ["gritty", "sludgy", "apathetic", "distorted", "raw"],
        "energy": "a raw and heavy dirge with a sense of disillusionment",
        "vocal_style": "angsty, raw, and often gravelly or strained"
    },
    "house": {
        "adjectives": ["four-on-the-floor", "deep", "soulful", "hypnotic", "danceable"],
        "energy": "a hypnotic and danceable groove",
        "vocal_style": "soulful, often diva-like vocal samples or hooks"
    },
    "k-pop": {
        "adjectives": ["hyper-polished", "high-energy", "choreography-driven", "multi-faceted", "slick"],
        "energy": "a blend of pop, rap, and electronic sections with dynamic structure shifts",
        "vocal_style": "a mix of clean, precise singing and sharp, rhythmic rap verses"
    },
    "dubstep": {
        "adjectives": ["bass-heavy", "syncopated", "wobbly", "dark", "robotic"],
        "energy": "a half-time rhythm with a heavy focus on bass drops and complex sound design"
    },
    "disco": {
        "adjectives": ["groovy", "four-on-the-floor", "orchestral", "danceable", "lush"],
        "energy": "an infectious, upbeat dance rhythm with lush string and horn sections",
        "vocal_style": "soaring, soulful, and often featuring falsetto"
    },
    "experimental": {
        "adjectives": ["unconventional", "avant-garde", "abstract", "boundary-pushing", "atonal"],
        "energy": "a rejection of traditional song structures and tonality"
    },
    "progressive": {
        "adjectives": ["technical", "complex", "epic", "multi-part", "virtuosic"],
        "energy": "long compositions with complex time signatures and shifting movements"
    },
    "nu metal": {
        "adjectives": ["aggressive", "down-tuned", "syncopated", "angsty", "hybrid"],
        "energy": "a fusion of heavy metal riffs with hip-hop rhythms and electronic textures",
        "vocal_style": "a dynamic mix of rapping, screaming, and melodic singing"
    },
    "pop rock": {
        "adjectives": ["catchy", "guitar-driven", "anthemic", "polished", "energetic"],
        "energy": "combining the memorable hooks of pop with the driving energy of rock",
        "vocal_style": "clean, powerful, and ready for radio"
    },
    "swing": {
        "adjectives": ["jazzy", "bouncy", "syncopated", "big-band", "vintage"],
        "energy": "a distinctive 'swing' rhythm that makes you want to dance",
        "vocal_style": "charismatic and rhythmic, in the style of a classic crooner"
    },
    "electro": {
        "adjectives": ["robotic", "synthetic", "808-driven", "funky", "digital"],
        "energy": "a rhythmic funk sound created with purely electronic instruments"
    },
    "drum and bass": {
        "adjectives": ["fast", "breakbeat-driven", "energetic", "bass-heavy", "complex"],
        "energy": "a high-speed, complex drum pattern (breakbeat) over a deep sub-bass line"
    },
    "trance": {
        "adjectives": ["hypnotic", "euphoric", "melodic", "progressive", "arpeggiated"],
        "energy": "a building, evolving track with a melodic breakdown and uplifting climax",
        "vocal_style": "often features ethereal, reverb-drenched female vocal snippets"
    },
    "indie pop": {
        "adjectives": ["quirky", "lo-fi", "melodic", "charming", "jangly"],
        "energy": "a blend of catchy pop sensibilities with an independent, less-polished feel",
        "vocal_style": "often understated, breathy, or slightly off-kilter"
    },
    "gospel": {
        "adjectives": ["uplifting", "soulful", "harmonious", "praise-filled", "choral"],
        "energy": "a powerful build of collective joy and spirit",
        "vocal_style": "powerful, soulful lead vocals with a large, dynamic choir"
    },
    "industrial": {
        "adjectives": ["abrasive", "mechanical", "dystopian", "noisy", "cold"],
        "energy": "a harsh blend of rock and electronic music with heavy, machine-like sounds"
    },
    "electropop": {
        "adjectives": ["synth-heavy", "catchy", "danceable", "modern", "slick"],
        "energy": "pop music where the primary instrumentation is synthesizers",
        "vocal_style": "polished and melodic, often with some light processing"
    },
    "phonk": {
        "adjectives": ["lo-fi", "distorted", "bass-heavy", "cowbell-driven", "dark"],
        "energy": "a dark, underground style inspired by 90s Memphis rap, with heavy 808s",
        "vocal_style": "chopped, slowed, and heavily processed vocal samples from old rap tapes"
    },
    "math rock": {
        "adjectives": ["technical", "complex", "asymmetrical", "intricate", "clean-toned"],
        "energy": "rock with a focus on complex rhythms, odd time signatures, and angular melodies"
    },
    "mutation funk": {
        "adjectives": ["experimental", "complex", "glitchy", "hyper-funky", "erratic"],
        "energy": "an extremely technical and unpredictable style of funk"
    },
    "bounce drop": {
        "adjectives": ["high-energy", "bouncy", "rhythmic", "plucky", "driving"],
        "energy": "a sub-genre of electronic music defined by a specific rhythmic drop"
    },

    # --- Regional & Cultural Genres ---
    "j-pop": {
        "adjectives": ["hyper-melodic", "upbeat", "polished", "eclectic", "energetic"],
        "energy": "a fast-paced and highly produced blend of pop, rock, and electronic styles",
        "vocal_style": "clean, high-pitched, and energetic, sung in Japanese"
    },
    "japanese": {
        "adjectives": ["traditional", "melodic", "cultural", "eclectic"],
        "energy": "can range from traditional folk music to modern genre fusions with a Japanese identity"
    },
    "anime": {
        "adjectives": ["energetic", "melodic", "dramatic", "J-rock-inspired", "cinematic"],
        "energy": "a high-energy track perfect for an opening or closing sequence",
        "vocal_style": "powerful and emotive, often in Japanese"
    },
    "cantonese": {
        "adjectives": ["Cantopop", "melodic", "ballad-heavy", "dramatic"],
        "energy": "pop music from Hong Kong, often characterized by strong melodies and emotional ballads",
        "vocal_style": "clear, emotive singing in the Cantonese language"
    },

    # --- Instrumental Styles ---
    "piano": {
        "adjectives": ["emotive", "elegant", "melancholic", "delicate", "percussive"],
        "energy": "ranging from sparse and sad to powerfully resonant"
    },
    "guitar": {
        "adjectives": ["riff-based", "melodic", "string-driven", "plucked", "strummed"],
        "energy": "carrying the main melody, a driving rhythm, or a complex solo"
    },
    "bass": {
        "adjectives": ["deep", "rhythmic", "foundational", "groovy", "low-end"],
        "energy": "providing the low-end groove and harmonic anchor of a song"
    },
    "drum": {
        "adjectives": ["rhythmic", "driving", "percussive", "tight", "keeping-time"],
        "energy": "setting the core tempo, feel, and rhythmic foundation"
    },
    "synth": {
        "adjectives": ["synthetic", "versatile", "textural", "atmospheric", "arpeggiated"],
        "energy": "providing pads, leads, bass, or complex rhythmic patterns"
    },
    "orchestral": {
        "adjectives": ["grand", "sweeping", "symphonic", "lush", "majestic"],
        "energy": "a full dynamic range from pianissimo to fortissimo",
        "vocal_style": "operatic soprano or tenor, or a full classical choir"
    },
    "violin": {
        "adjectives": ["string-driven", "classical", "soaring", "emotive", "lyrical"],
        "energy": "carrying a beautiful, high-pitched melody or adding lush texture"
    },
    "electric guitar": {
        "adjectives": ["distorted", "riff-driven", "searing", "overdriven", "clean-toned"],
        "energy": "carrying powerful rock riffs or soaring, melodic lead solos"
    },
    "acoustic guitar": {
        "adjectives": ["fingerpicked", "strummed", "organic", "intimate", "unplugged"],
        "energy": "providing a warm rhythmic or melodic foundation for a song"
    },
    "classical": {
        "adjectives": ["symphonic", "ornate", "complex", "timeless", "contrapuntal"],
        "energy": "a complex and dynamic arrangement for an orchestra, chamber ensemble, or solo instrument",
        "vocal_style": "operatic, choral, and highly trained"
    },
    "flute": {
        "adjectives": ["airy", "melodic", "wind-driven", "delicate", "breathy"],
        "energy": "providing a high-pitched, often beautiful and soaring melody"
    },
    "beat": {
        "adjectives": ["rhythmic", "percussive", "foundational", "driving"],
        "energy": "the underlying rhythmic pulse of a track, especially in electronic or hip hop music"
    },
    "edm": {
        "adjectives": ["electronic", "dance", "club-ready", "high-energy", "synthetic"],
        "energy": "a broad term for electronic music designed for festivals and clubs, often featuring a 'drop'",
    },

}
