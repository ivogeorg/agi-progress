#!/usr/bin/env python3
"""Fix features.json: remove duplicates and update synthetic data status."""

import json
from pathlib import Path

# Read features.json
features_path = Path('.kiro/features.json')
with open(features_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Track seen feature IDs
seen = set()
cleaned_features = {}

# Remove duplicates (keep first occurrence)
for fid, feature in data['features'].items():
    if fid not in seen:
        seen.add(fid)
        cleaned_features[fid] = feature

# Update synthetic data generation status
if 'data-synthetic-generation-00001' in cleaned_features:
    cleaned_features['data-synthetic-generation-00001']['status'] = 'completed'
    cleaned_features['data-synthetic-generation-00001']['started_date'] = '2026-02-15T00:00:00Z'
    cleaned_features['data-synthetic-generation-00001']['completed_date'] = '2026-02-15T00:00:00Z'

# Write back
data['features'] = cleaned_features
with open(features_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"✓ Fixed features.json")
print(f"  - Removed {len(data['features']) - len(cleaned_features)} duplicate entries")
print(f"  - Updated data-synthetic-generation-00001 status to 'completed'")
