def count_words(string):
    return f"Found {len(string.split())} total words"

def count_characters(string):
    result = {}
    for c in string:
        key = c.lower()
        if key not in result:
            result[key] = 0
        result[key] += 1
    return result

def sort_on(items):
    return items["count"]

def sort_stats(characters_stats):
    stats = []
    for key in characters_stats:
        stats.append({
            "char": key,
            "count": characters_stats[key]
        })
    stats.sort(reverse=True, key=sort_on)
    return stats
