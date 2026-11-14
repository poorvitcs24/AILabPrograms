
# Program 1: Prove Robert is Criminal
# Using Forward Chaining

facts = {
    ("American", "Robert"),
    ("Enemy", "A", "America"),
    ("Missile", "M1"),
    ("Sells", "Robert", "M1", "A")
}

def forward_chaining(facts):

    changed = True

    while changed:
        changed = False
        new_facts = set()

        # Rule 1: Enemy -> Hostile
        for f in facts:
            if f[0] == "Enemy":
                new_facts.add(("Hostile", f[1]))

        # Rule 2: Missile -> Weapon
        for f in facts:
            if f[0] == "Missile":
                new_facts.add(("Weapon", f[1]))

        # Rule 3: American + Weapon + Sells + Hostile
        for a in facts:
            for w in facts:
                for s in facts:
                    for h in facts:

                        if (a[0] == "American" and
                            w[0] == "Weapon" and
                            s[0] == "Sells" and
                            h[0] == "Hostile"):

                            if (a[1] == s[1] and
                                w[1] == s[2] and
                                s[3] == h[1]):

                                new_facts.add(
                                    ("Criminal", a[1])
                                )

        # Add only new facts
        for f in new_facts:
            if f not in facts:
                print("Derived:", f)
                facts.add(f)
                changed = True

    return facts


result = forward_chaining(facts)

query = ("Criminal", "Robert")

print("\nFinal Result:")

if query in result:
    print("Robert is a Criminal")
else:
    print("Robert is not proved Criminal")
