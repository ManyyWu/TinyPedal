"""Config hover translations. Language data lives in one module per language."""

from . import zh_CN

# First version uses Simplified Chinese; no persisted setting or UI change.
LANGUAGES = {"zh_CN": zh_CN}
DEFAULT_LANGUAGE = "zh_CN"


def config_tooltip(section: str, key: str, language: str = DEFAULT_LANGUAGE) -> str:
    """Return a translated Config hint, preserving the original configuration key."""
    catalog = LANGUAGES.get(language)
    if catalog is None:
        return key
    text = catalog.SECTION_OPTIONS.get(section, {}).get(key)
    if text is None:
        text = catalog.OPTIONS.get(key)
    if text is None:
        # Shared display patterns, with explicitly translated subjects only.
        for prefix, template in catalog.PATTERNS:
            if key.startswith(prefix):
                subject = catalog.SUBJECTS.get(key[len(prefix):])
                if subject:
                    text = template.format(subject=subject)
                break
    return f"{text}\n配置键：{key}" if text else key


def config_label(section: str, key: str, fallback: str, language: str = DEFAULT_LANGUAGE) -> str:
    """Translate a Config label only; keep unknown labels in their original language."""
    catalog = LANGUAGES.get(language)
    if catalog is None:
        return fallback
    text = catalog.SECTION_LABELS.get(section, {}).get(key)
    if text is None:
        text = catalog.LABELS.get(key)
    if text is None:
        for prefix, template in catalog.LABEL_PATTERNS:
            if key.startswith(prefix):
                subject = catalog.SUBJECTS.get(key[len(prefix):])
                if subject:
                    text = template.format(subject=subject)
                break
    return text or _translate_key(catalog, key) or fallback


def _translate_key(catalog, key: str) -> str | None:
    """Translate known Config terminology; unknown words keep the English fallback."""
    if key in catalog.PHRASES:
        return catalog.PHRASES[key]
    for prefix, template in catalog.KEY_PATTERNS:
        if key.startswith(prefix):
            subject = _translate_key(catalog, key[len(prefix):])
            return template.format(subject=subject) if subject else None
    tokens = key.split('_')
    result = []
    index = 0
    while index < len(tokens):
        for end in range(len(tokens), index, -1):
            phrase = '_'.join(tokens[index:end])
            if phrase in catalog.PHRASES:
                result.append(catalog.PHRASES[phrase])
                index = end
                break
        else:
            token = tokens[index]
            text = token if token.isdigit() else catalog.WORDS.get(token)
            if text is None:
                return None
            result.append(text)
            index += 1
    return ''.join(result)


def config_ui(text: str) -> str:
    """Translate Config-only fixed interface text."""
    return LANGUAGES[DEFAULT_LANGUAGE].UI.get(text, text)


def list_name(key: str, fallback: str, language: str = DEFAULT_LANGUAGE) -> str:
    """Translate Widget / Module list names without changing shared formatters."""
    catalog = LANGUAGES.get(language)
    return catalog.LIST_NAMES.get(key, fallback) if catalog else fallback
