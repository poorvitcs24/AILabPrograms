
# Unification Algorithm in First Order Logic

# Variables used in the expressions
variables = {'x', 'y', 'z', 'u', 'v'}

# Apply substitution to an expression
def apply_subst(expr, subst):
    if isinstance(expr, str):
        while expr in subst:
            expr = subst[expr]
        return expr

    return tuple(apply_subst(x, subst) for x in expr)


# Check whether a variable occurs in an expression
def occurs(var, expr, subst):
    expr = apply_subst(expr, subst)

    if expr == var:
        return True

    if isinstance(expr, tuple):
        return any(occurs(var, x, subst) for x in expr)

    return False


# Unification function
def unify(x, y, subst=None):

    if subst is None:
        subst = {}

    x = apply_subst(x, subst)
    y = apply_subst(y, subst)

    # If both expressions are identical
    if x == y:
        return subst

    # If x is a variable
    if isinstance(x, str) and x in variables:
        if occurs(x, y, subst):
            return None

        subst[x] = y
        return subst

    # If y is a variable
    if isinstance(y, str) and y in variables:
        if occurs(y, x, subst):
            return None

        subst[y] = x
        return subst

    # If both are compound expressions
    if isinstance(x, tuple) and isinstance(y, tuple):

        if len(x) != len(y):
            return None

        for a, b in zip(x, y):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    # Otherwise, unification fails
    return None


# Example expressions:
# P(x, f(y)) and P(a, f(b))

expr1 = ('P', 'x', ('f', 'y'))
expr2 = ('P', 'Anu', ('f', 'Apple'))

result = unify(expr1, expr2)

if result is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Most General Unifier (MGU):")

    for var, value in result.items():
        print(var, "=", value)