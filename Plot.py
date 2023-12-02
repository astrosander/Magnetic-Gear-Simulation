import numpy as np
import matplotlib.pyplot as plt
from magpylib.source.magnet import Cylinder
import magpylib as magpy
import math

pi = math.pi

def ConstrastVal(a):
  return math.sqrt(abs(a))

def DrawImage(c, res, i, folder_name):
    zs = np.linspace(-13, 13, res)
    xs = np.linspace(-11.5, 31.5, res)

    fig = plt.figure(figsize=(10, 6))

    ax2 = fig.add_subplot(111)
    B, B1 = [],[]
    num = 0

    for z in zs:
        num += 1
        print(f"{i}.png   {round(100*num/res, 1)}%")

        for x in xs:
            magnetic_field1 = c.getB([x, 0, z])

            aa = magnetic_field1[0]
            bb = magnetic_field1[1]
            cc = magnetic_field1[2]

            B1.append([aa, bb, cc])

            aa = ConstrastVal(aa)
            bb = ConstrastVal(bb)
            cc = ConstrastVal(cc)

            # magnetic_field = math.sqrt(aa * aa + bb*bb + cc*cc)

            B.append([aa, bb, cc])

    print("\nCompiling...\n")

    Bs = np.array(B).reshape([res, res, 3])  # reshape

    Bamp = np.linalg.norm(Bs, axis=2)

    # magpy.displaySystem(c,subplotAx=ax1,suppress=True)
    # ax1.view_init(elev=75)

    X, Z = np.meshgrid(xs, zs)
    ax2.pcolor(xs, zs, Bamp, cmap="turbo", vmax=50)

    Bs = np.array(B1).reshape([res, res, 3])  # reshape

    X, Z = np.meshgrid(xs, zs)
    U, V = Bs[:, :, 0], Bs[:, :, 2]
    ax2.streamplot(X, Z, U, V, color="k", density=5, linewidth=0.6, arrowsize=0.6)
    # plt.show()
    plt.savefig(f"{folder_name}\\{i}.png", dpi=300)

def SystemCalc()

def DrawImageNxM(res, j, val, r, x0, folder_name, m1, m2):
    phi = pi / (129) * j * m2 / m1

    for i in range(0, m1):
        s1.append(Cylinder(mag=[0, 0, val], dim=[2.5, 2]))
    for i in range(0, m1):
        s1[i].move(
            (
                r * math.cos(pi / 2 + phi + 2 * pi * i / m1),
                0,
                r * math.sin(pi / 2 + phi + 2 * pi * i / m1),
            )
        )

    for i in range(0, m1):
        s1[i].rotate(-i * 360 / m1 - phi / pi * 180, [0, 1, 0])


    phi1 = -pi / (129) * j * m1 / m2

    s2 = []
    for i in range(0, m2):
        s2.append(Cylinder(mag=[0, 0, -val], dim=[2.5, 2]))

    for i in range(0, m2):
        s2[i].move(
            (
                r * math.cos(pi / 2 + phi1 + 2 * pi * i / m2) + x0,
                0,
                r * math.sin(pi / 2 + phi1 + 2 * pi * i / m2),
            )
        )

    for i in range(0, m2):
        s2[i].rotate(-i * 360 / m2 - phi1 / pi * 180, [0, 1, 0])

    c = magpy.Collection(s1, s2)

    DrawImage(c, res, j, folder_name)