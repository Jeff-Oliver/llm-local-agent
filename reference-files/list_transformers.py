import transformers

# Get all public members
items = [item for item in dir(transformers) if not item.startswith('_')]

print(f"Total items in transformers module: {len(items)}\n")
print("=" * 60)

# Categorize by common prefixes
categories = {}
for item in items:
    if item.startswith('Auto'):
        categories.setdefault('Auto Classes', []).append(item)
    elif item.endswith('Config'):
        categories.setdefault('Configuration Classes', []).append(item)
    elif item.endswith('Tokenizer') or item.endswith('TokenizerFast'):
        categories.setdefault('Tokenizers', []).append(item)
    elif item.endswith('Model') or 'Model' in item:
        categories.setdefault('Model Classes', []).append(item)
    elif item.endswith('Processor'):
        categories.setdefault('Processors', []).append(item)
    elif item.endswith('FeatureExtractor'):
        categories.setdefault('Feature Extractors', []).append(item)
    else:
        categories.setdefault('Other', []).append(item)

# Print categorized
for category in sorted(categories.keys()):
    print(f"\n{category} ({len(categories[category])}):")
    print("-" * 60)
    for item in sorted(categories[category])[:20]:  # Limit to first 20
        print(f"  - {item}")
    if len(categories[category]) > 20:
        print(f"  ... and {len(categories[category]) - 20} more")

print("\n" + "=" * 60)
print("\nAll items (alphabetically):")
print("-" * 60)
for item in sorted(items):
    print(f"  - {item}")
