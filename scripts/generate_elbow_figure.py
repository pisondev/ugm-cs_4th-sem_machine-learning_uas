from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "elbow_method_optimal_k.svg"

# Approximate values digitized from the provided figure.
POINTS = [
    (2, 3000),
    (3, 1700),
    (4, 1460),
    (5, 1220),
    (6, 1040),
    (7, 920),
    (8, 820),
    (9, 720),
]

WIDTH = 760
HEIGHT = 560
LEFT = 110
RIGHT = 48
TOP = 72
BOTTOM = 92
PLOT_W = WIDTH - LEFT - RIGHT
PLOT_H = HEIGHT - TOP - BOTTOM
X_MIN, X_MAX = 2, 9
Y_MIN, Y_MAX = 650, 3050


def sx(x):
    return LEFT + (x - X_MIN) / (X_MAX - X_MIN) * PLOT_W


def sy(y):
    return TOP + (Y_MAX - y) / (Y_MAX - Y_MIN) * PLOT_H


def text(x, y, value, size=24, weight=400, anchor="middle", rotate=None):
    transform = f' transform="rotate({rotate} {x} {y})"' if rotate else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" '
        f'text-anchor="{anchor}" font-family="Arial, Helvetica, sans-serif"{transform}>'
        f"{value}</text>"
    )


def line(x1, y1, x2, y2, stroke="#d3d3d3", width=1.2):
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{stroke}" stroke-width="{width}" />'
    )


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)

    x_ticks = [2, 4, 6, 8]
    y_ticks = [1000, 1500, 2000, 2500, 3000]
    path = " ".join(
        ("M" if idx == 0 else "L") + f" {sx(x):.1f} {sy(y):.1f}"
        for idx, (x, y) in enumerate(POINTS)
    )

    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<rect width="100%" height="100%" fill="#ffffff" />',
        text(WIDTH / 2, 42, "Elbow Method For Optimal k", size=28, weight=700),
    ]

    for y in y_ticks:
        elements.append(line(LEFT, sy(y), WIDTH - RIGHT, sy(y)))
        elements.append(text(LEFT - 18, sy(y) + 8, str(y), size=20, weight=700, anchor="end"))

    for x in x_ticks:
        elements.append(line(sx(x), TOP, sx(x), HEIGHT - BOTTOM))
        elements.append(text(sx(x), HEIGHT - BOTTOM + 34, str(x), size=20, weight=700))

    elements.extend(
        [
            line(LEFT, TOP, LEFT, HEIGHT - BOTTOM, stroke="#303030", width=2),
            line(LEFT, HEIGHT - BOTTOM, WIDTH - RIGHT, HEIGHT - BOTTOM, stroke="#303030", width=2),
            f'<path d="{path}" fill="none" stroke="#555555" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />',
        ]
    )

    for x, y in POINTS:
        elements.append(f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="7" fill="#222222" />')

    elements.extend(
        [
            text(WIDTH / 2, HEIGHT - 24, "Number of Clusters (k)", size=24, weight=700),
            text(28, HEIGHT / 2, "Sum_of_squared_distances", size=24, weight=700, rotate=-90),
            "</svg>",
        ]
    )

    OUT.write_text("\n".join(elements), encoding="utf-8")


if __name__ == "__main__":
    main()
