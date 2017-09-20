def lang_genoeg(lengte):
    return 'Je bent lang genoeg voor de attractie' if lengte > 120 else 'Sorry, je bent te klein!'

print(lang_genoeg(110))

print(lang_genoeg(185))