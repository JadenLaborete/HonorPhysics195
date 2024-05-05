import math

def quadraticz_solver(x, y):
    discriminant = x**2 - 4 * -4.9 * y
    root1 = (-x + math.sqrt(discriminant)) / (2 * -4.9)
    root2 = (-x - math.sqrt(discriminant)) / (2 * -4.9)
    return root1, root2

def main():
    xi, yi, yf, vi, angle = 22, 15, 20, 70, 45

    theta_rad = math.radians(angle)
    vix = vi * math.cos(theta_rad)
    viy = vi * math.sin(theta_rad)

    quadatric_ans = quadraticz_solver(viy, yi - yf)
    time = max(quadatric_ans) if max(quadatric_ans) > 0 else min(quadatric_ans)

    xf = vix * time + xi
    vfy = viy - 9.8 * time

    print(f"Final x velocity: {vix:.2f} m/s, final y velocity: {vfy:.2f} m/s.")
    print(f"Projectile position at time {time:.2f} seconds: ({xf:.2f} meters, {yf} meters).")


if __name__ == "__main__":
    main()
