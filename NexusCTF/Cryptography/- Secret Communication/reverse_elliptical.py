from sage.all import *

def pohlig_hellman_attack(G, Q, order, factorization):
    """
    Solve discrete log Q = secret * G using Pohlig-Hellman algorithm
    when the order factors into small primes.
    """
    print(f"\n[*] Starting Pohlig-Hellman attack")
    print(f"[*] Order: {order}")
    print(f"[*] Factorization: {factorization}\n")
    
    moduli = []
    remainders = []
    
    for prime, exponent in factorization:
        print(f"[+] Working on prime factor {prime}^{exponent}")
        
        # For each prime power factor
        prime_power = prime^exponent
        
        # Reduce to subgroup of order prime_power
        cofactor = order // prime_power
        G_sub = cofactor * G
        Q_sub = cofactor * Q
        
        # Solve discrete log in this subgroup
        if prime_power < 10^8:
            print(f"    Using discrete_log for order {prime_power}")
            secret_mod = discrete_log(Q_sub, G_sub, ord=prime_power, operation='+')
        else:
            print(f"    Prime power too large: {prime_power}")
            print(f"    Trying discrete_log anyway...")
            secret_mod = discrete_log(Q_sub, G_sub, ord=prime_power, operation='+')
        
        print(f"    Found: secret ≡ {secret_mod} (mod {prime_power})")
        
        moduli.append(prime_power)
        remainders.append(secret_mod)
    
    # Use Chinese Remainder Theorem to combine results
    print(f"\n[*] Applying Chinese Remainder Theorem")
    secret = CRT(remainders, moduli)
    
    return secret

def recover_y_coordinate(E, x_coord):
    """Recover the y coordinate from x coordinate on elliptic curve"""
    # For curve y^2 = x^3 + x, compute y^2 and take square root
    p = E.base_ring().order()
    y_squared = (x_coord^3 + x_coord) % p
    
    # Try to find square root
    K = GF(p)
    y_squared_element = K(y_squared)
    
    if not y_squared_element.is_square():
        raise ValueError("x coordinate not on curve")
    
    y = y_squared_element.sqrt()
    
    # Return both possible y values
    return (int(y), int(-y))

def break_with_known_info():
    """Break the ECDLP with known Q.x(), P.x(), and partial secret leak"""
    
    print("="*70)
    print("Elliptic Curve Discrete Log Attack - With Known Information")
    print("="*70)
    
    # The curve parameters
    p = 3391454550160661115094033672759471
    E = EllipticCurve(GF(p), [1, 0])
    
    print(f"\n[*] Curve: y^2 = x^3 + x over GF({p})")
    
    # Known information
    Q_x = 627816505764523651613513947713902
    P_x = 2908007773384647231320272840899154
    secret_prefix = "144"
    
    print(f"[*] Known Q.x() = {Q_x}")
    print(f"[*] Known P.x() = {P_x}")
    print(f"[*] Known secret prefix = {secret_prefix}...")
    
    # Recover full points
    print(f"\n[*] Recovering y-coordinates...")
    Q_y_options = recover_y_coordinate(E, Q_x)
    P_y_options = recover_y_coordinate(E, P_x)
    
    print(f"[*] Q possible y values: {Q_y_options[0]}, {Q_y_options[1]}")
    print(f"[*] P possible y values: {P_y_options[0]}, {P_y_options[1]}")
    
    # Get the generator
    G = E.gens()[0]
    print(f"[*] Generator G: {G}")
    
    # Get the order of the curve and its factorization
    order = E.order()
    print(f"[*] Curve order: {order}")
    
    factorization = list(factor(order))
    print(f"[*] Order factorization: {factorization}")
    
    max_prime = max([pr for pr, e in factorization])
    print(f"[*] Largest prime factor: {max_prime}")
    
    if max_prime > 10^10:
        print(f"\n[!] Warning: Largest prime factor is {max_prime}")
        print(f"[!] Attack may take some time...")
    else:
        print(f"\n[+] Order is smooth! Attack is feasible.\n")
    
    # Try all combinations of y-coordinates
    print("\n" + "="*70)
    print("[*] Trying all possible point combinations...")
    print("="*70)
    
    success = False
    for i, Q_y in enumerate(Q_y_options):
        for j, P_y in enumerate(P_y_options):
            print(f"\n[*] Attempt {i*2 + j + 1}/4: Q_y option {i+1}, P_y option {j+1}")
            
            try:
                Q = E(Q_x, Q_y)
                P = E(P_x, P_y)
                
                print(f"    Q = {Q}")
                print(f"    P = {P}")
                
                # Check if points are on curve and valid
                if Q not in E or P not in E:
                    print("    [!] Points not on curve, skipping...")
                    continue
                
                # Perform Pohlig-Hellman attack
                secret_recovered = pohlig_hellman_attack(G, Q, order, factorization)
                
                # Verify the result
                Q_check = secret_recovered * G
                if Q_check == Q:
                    print(f"\n    [✓] Verification passed: secret * G == Q")
                    
                    # Check if it matches the known prefix
                    secret_str = str(secret_recovered)
                    if secret_str.startswith(secret_prefix):
                        print(f"\n{'='*70}")
                        print(f"[✓] SUCCESS! Found matching secret!")
                        print(f"[✓] SECRET: {secret_recovered}")
                        print(f"{'='*70}")
                        
                        # Also compute shared secret for verification
                        shared_secret = secret_recovered * P
                        print(f"\n[*] Shared secret point: {shared_secret}")
                        print(f"[*] Shared secret x-coordinate: {shared_secret.xy()[0]}")
                        
                        success = True
                        return secret_recovered
                    else:
                        print(f"    [!] Secret found but doesn't match prefix")
                        print(f"    [!] Found: {secret_str[:10]}...")
                        print(f"    [!] Expected prefix: {secret_prefix}")
                else:
                    print(f"    [✗] Verification failed")
                    
            except Exception as e:
                print(f"    [!] Error: {e}")
                continue
    
    if not success:
        print("\n[!] Could not recover secret with given information")
        print("[!] The partial secret leak might help narrow down the search...")
        
        # Try to use the prefix constraint
        print("\n[*] Attempting recovery with prefix constraint...")
        Q = E(Q_x, Q_y_options[0])  # Try first option
        secret_base = pohlig_hellman_attack(G, Q, order, factorization)
        
        print(f"\n[*] Base secret found: {secret_base}")
        print(f"[*] Checking if it matches prefix {secret_prefix}...")
        
        if str(secret_base).startswith(secret_prefix):
            print(f"[✓] Match found!")
            return secret_base
    
    return None

if __name__ == "__main__":
    print("\n" + "🔓"*35)
    secret = break_with_known_info()
    print("\n" + "🔓"*35)
    
    if secret:
        print(f"\n[✓] FINAL ANSWER: {secret}")
    else:
        print(f"\n[✗] Attack unsuccessful")