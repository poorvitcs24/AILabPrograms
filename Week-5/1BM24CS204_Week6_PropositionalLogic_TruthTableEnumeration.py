
from itertools import product

# Knowledge Base
def KB(P, Q):
    e1 = (not P) or Q       # P -> Q
    e2 = P                  # P
    e3 = Q or P             # Q OR P
    return e1 and e2 and e3

# Queries
def query1(P, Q):
    return Q

def query2(P, Q):
    return P

def query3(P, Q):
    return P and Q

# Truth Table Enumeration
def entails(query):
    for P, Q in product([True, False], repeat=2):
        if KB(P, Q) and not query(P, Q):
            return False
    return True

# Display Complete Truth Table
print("\n========== TRUTH TABLE ==========")

print(f"{'P':<6}{'Q':<6}{'P->Q':<8}"
      f"{'P':<6}{'Q|P':<8}{'KB':<8}"
      f"{'Q1':<6}{'Q2':<6}{'Q3':<6}")

for P, Q in product([True, False], repeat=2):

    e1 = (not P) or Q
    e2 = P
    e3 = Q or P
    kb = KB(P, Q)

    q1 = query1(P, Q)
    q2 = query2(P, Q)
    q3 = query3(P, Q)

    # Print T/F values
    values = [P, Q, e1, e2, e3, kb, q1, q2, q3]

    print("".join(f"{'T' if v else 'F':<6}"
                  for v in values))

# Display Entailment Results
print("\n======= QUERY RESULTS =======")

queries = {
    "Query 1 (Q)": query1,
    "Query 2 (P)": query2,
    "Query 3 (P AND Q)": query3
}

for name, query in queries.items():
    if entails(query):
        print(name, ": Entailed")
    else:
        print(name, ": Not Entailed")