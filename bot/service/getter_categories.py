import inspect
from lexicon import lexicon

attrs_lexicon = inspect.getmembers(lexicon, lambda x : not inspect.isfunction(x))

callback_categories = {}
for attr, obj in attrs_lexicon:
    if attr.endswith("income") or attr.endswith("expence"):
        callback_categories[attr] = obj.text