#!/usr/bin/env python3
"""Analyze feature graph: summary for @prime, full detail + recommendation for @next."""

import json
import sys
from collections import defaultdict


def load_features():
    try:
        with open('.kiro/features.json', 'r') as f:
            return json.load(f)['features']
    except FileNotFoundError:
        print("❌ .kiro/features.json not found. Run @design-digest first.")
        sys.exit(1)


def calculate_horizon(features):
    horizon, blocked = [], []
    for fid, f in features.items():
        status = f.get('status', 'not_started')
        if status in ('completed', 'in_progress', 'planned', 'next_selected', 'deprecated'):
            continue
        deps = f.get('dependencies', [])
        incomplete = [d for d in deps if features.get(d, {}).get('status') != 'completed']
        if not incomplete:
            horizon.append(fid)
        else:
            blocked.append((fid, incomplete))
    return horizon, blocked


def count_dependents(features):
    dependents = defaultdict(int)
    for f in features.values():
        for dep in f.get('dependencies', []):
            dependents[dep] += 1
    return dependents


def get_stats(features):
    stats = {'completed': 0, 'in_progress': 0, 'not_started': 0, 'next_selected': 0, 'planned': 0, 'deprecated': 0}
    for f in features.values():
        s = f.get('status', 'not_started')
        if s in stats:
            stats[s] += 1
        else:
            stats['not_started'] += 1
    return stats


def score_features(horizon, features):
    dependents = count_dependents(features)
    scored = []
    for fid in horizon:
        f = features[fid]
        score, reasons = 0, []
        moscow = f.get('moscow', 'Should-have')
        if moscow == 'Must-have':
            score += 10; reasons.append("Must-have priority")
        elif moscow == 'Should-have':
            score += 5
        uc = dependents.get(fid, 0)
        if uc > 0:
            score += uc * 3; reasons.append(f"Unblocks {uc} feature{'s' if uc != 1 else ''}")
        tasks = len(f.get('tasks', []))
        complexity = 'Low' if tasks <= 3 else ('Medium' if tasks <= 6 else 'High')
        score += (4 - (1 if tasks <= 3 else (2 if tasks <= 6 else 3)))
        if complexity == 'Low':
            reasons.append("Low complexity")
        scored.append((fid, score, reasons, complexity))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


def print_summary(features, horizon, blocked, stats):
    """Compact summary for @prime."""
    total = len(features) - stats['deprecated']
    print(f"📊 FEATURE STATUS: {stats['completed']}/{total} completed | {len(horizon)} ready | {len(blocked)} blocked")
    if stats['next_selected']:
        ns = [fid for fid, f in features.items() if f.get('status') == 'next_selected']
        print(f"⏭️  Next selected: {', '.join(ns)}")
    if stats['planned']:
        pl = [fid for fid, f in features.items() if f.get('status') == 'planned']
        print(f"📝 Planned: {', '.join(pl)}")
    if stats['in_progress']:
        ip = [fid for fid, f in features.items() if f.get('status') == 'in_progress']
        print(f"🔄 In progress: {', '.join(ip)}")
    if horizon:
        print(f"\n🎯 HORIZON ({len(horizon)} ready):")
        for fid in horizon:
            f = features[fid]
            print(f"  • {fid} [{f.get('moscow','?')}] - {f['name']}")
    if blocked:
        print(f"\n🚫 BLOCKED ({len(blocked)}):")
        for fid, deps in blocked[:5]:
            print(f"  • {fid} → {', '.join(deps)}")
        if len(blocked) > 5:
            print(f"  ... and {len(blocked) - 5} more")


def print_detail(features, horizon, blocked, stats):
    """Full detail with recommendation for @next."""
    total = len(features) - stats['deprecated']
    scored = score_features(horizon, features)
    dependents = count_dependents(features)

    print("🎯 DEVELOPMENT HORIZON\n")
    print(f"Progress: {stats['completed']}/{total} completed, {len(horizon)} ready, {len(blocked)} blocked\n")
    print("━" * 70)

    if not scored:
        print("\n⚠️  No features ready to implement.\n")
        if blocked:
            for fid, deps in blocked[:5]:
                print(f"  • {fid} → waiting on: {', '.join(deps)}")
        return

    # Recommended
    rec_id, _, rec_reasons, rec_complexity = scored[0]
    rec = features[rec_id]
    print(f"\n⭐ RECOMMENDED: {rec_id}\n")
    print(f"   📋 {rec['name']}")
    print(f"   🎯 {rec.get('moscow','?')} | 📊 {rec_complexity}")
    uc = dependents.get(rec_id, 0)
    if uc:
        print(f"   🔓 Unblocks {uc} feature{'s' if uc != 1 else ''}")
    for r in rec_reasons:
        print(f"   • {r}")

    # Others
    others = scored[1:]
    if others:
        print(f"\n{'━' * 70}")
        print(f"\nOTHER READY ({len(others)}):\n")
        for i, (fid, _, _, comp) in enumerate(others, 1):
            f = features[fid]
            deps = f.get('dependencies', [])
            dep_str = f"deps: {', '.join(deps)} ✓" if deps else "no deps"
            print(f"  {i}. {fid} [{f.get('moscow','?')}] {comp} | {dep_str}")

    if blocked:
        print(f"\n{'━' * 70}")
        print(f"\nBLOCKED ({len(blocked)}):\n")
        for fid, deps in blocked[:5]:
            print(f"  • {fid} → {', '.join(deps)}")

    print(f"\n{'━' * 70}")
    # Machine-readable output for @next prompt
    print(f"\n__RECOMMENDED__:{rec_id}")
    print(f"__HORIZON__:{','.join([s[0] for s in scored])}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else '--detail'
    features = load_features()
    horizon, blocked = calculate_horizon(features)
    stats = get_stats(features)

    if mode == '--summary':
        print_summary(features, horizon, blocked, stats)
    else:
        print_detail(features, horizon, blocked, stats)


if __name__ == '__main__':
    main()
