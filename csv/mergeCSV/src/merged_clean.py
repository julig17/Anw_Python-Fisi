import csv

VALID_ROLES = {"warrior", "mage", "healer", "archer", "tank", "assassin"}

DATA_NAME_SERVER_A = "./csv/mergeCSV/data/serverA.csv"
DATA_NAME_SERVER_B = "./csv/mergeCSV/data/serverB.csv"

DATA_NAME_SERVER_A_CLEAN = "./csv/mergeCSV/data/merged/serverA_clean.csv"
DATA_NAME_SERVER_B_CLEAN = "./csv/mergeCSV/data/merged/serverB_clean.csv"
DATA_NAME_MERGED = "./csv/mergeCSV/data/merged/merged_clean.csv"

def read_csv(path):
    roles = {}
    errors = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_no, row in enumerate(reader, start=2): # ACHTUNG: Header ist Zeile 1
            player = (row.get("playername") or "").strip().lower()
            role = (row.get("role") or "").strip().lower()
            if player == "":
                errors.append(f"{path}: Zeile {line_no}: Spielername fehlt")
                continue
            if role == "":
                errors.append(f"{path}: Zeile {line_no}: Rolle fehlt für {player}")
                continue
            if role not in VALID_ROLES:
                errors.append(f"{path}: Zeile {line_no}: Ungültige Rolle '{role}' für {player}")
                continue
            if player in roles and roles[player] != role:
                errors.append(
                    f"{path}: Zeile {line_no}: Konflikt für {player} "
                    f"(alt: {roles[player]}, neu: {role}), alte Rolle bleibt"
                )
                continue
            roles[player] = role
    return roles, errors

def merge(a, b):
    merged = dict(a)
    conflicts = []
    for player, role_b in b.items():
        if player in merged:
            if merged[player] != role_b:
                conflicts.append(
                    f"Konflikt: {player} -> serverA={merged[player]} vs serverB={role_b}"
                )
        else:
            merged[player] = role_b
    return merged, conflicts

def write_csv(path, roles):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["playername", "role"])
        for player in sorted(roles):
            writer.writerow([player, roles[player]])
    print("Geschrieben:", path)

def print_errors(errors_a, errors_b, roles_a, roles_b, merged, conflicts, show_max_errors=20):
    all_errors = errors_a + errors_b
    only_a = set(roles_a) - set(roles_b)
    only_b = set(roles_b) - set(roles_a)
    both = set(roles_a) & set(roles_b)
    union = set(roles_a) | set(roles_b)
    only_one_server = set(roles_a) ^ set(roles_b)
    gesamt = len(roles_a) + len(roles_b)

    print("=== Gesamtübersicht ===")
    print(f"Gesamteinträge (mit Duplikaten): {gesamt}")
    print(f"Gesamteinträge (ohne Duplikate): {len(union)}")
    print(f"Nur auf einem Server vorhanden: {len(only_one_server)}")

    print("\n=== Serververteilung ===")
    print(f"Server A Spieler: {len(roles_a)}")
    print(f"Server B Spieler: {len(roles_b)}")

    print("\n=== Nach Merge ===")
    print(f"Gesamt nach Merge: {len(merged)}")
    print(
        f"Spieler nur auf einem Server: {len(only_one_server)} | "
        f"Nur A: {len(only_a)} | "
        f"Nur B: {len(only_b)} | "
        f"Beide: {len(both)}"
    )

    for c in conflicts[:show_max_errors]:
        print(" ", c)
    print("\nKonflikte:", "Fehler gesamt:", len(all_errors), "Angezeigt:", show_max_errors)
    for e in all_errors[:show_max_errors]:
        print(" ", e)

def main():
    roles_a, errors_a = read_csv(DATA_NAME_SERVER_A)
    print(roles_a)
    print(errors_a)
    roles_b, errors_b = read_csv(DATA_NAME_SERVER_B)
    merged, conflicts = merge(roles_a, roles_b)
    print_errors(errors_a, errors_b, roles_a, roles_b, merged, conflicts, show_max_errors=10)
    write_csv(DATA_NAME_SERVER_A_CLEAN, roles_a)
    write_csv(DATA_NAME_SERVER_B_CLEAN, roles_b)
    write_csv(DATA_NAME_MERGED, merged)

if __name__ == "__main__":
    main()