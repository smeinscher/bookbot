def get_word_count(text: str):
    return len(text.split())

def get_character_count(text: str) -> dict[str, int]:
    text = text.lower()
    character_counts: dict[str, int] = {}
    for c in text:
        character_counts.update({c: character_counts.get(c, 0) + 1})
    return character_counts

def sort_on(items):
    return items["num"]

def get_sorted_character_list(character_counts: dict[str, int]):
    l = []
    for key, value in character_counts.items():
        l.append({"char": key, "num": value});
    l.sort(reverse=True, key=sort_on)
    return l
