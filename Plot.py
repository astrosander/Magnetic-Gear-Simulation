import numpy as np
import matplotlib.pyplot as plt
from magpylib.source.magnet import Cylinder
import magpylib as magpy
import math
import os

pi = math.pi

def DrawImage(res, num1, val, r, x0, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for i in range(0, num1):
      phi = pi / (128) * i

      s1 = Cylinder(mag=[0, 0, val], dim=[2.5, 2])
      s3 = Cylinder(mag=[0, 0, val], dim=[2.5, 2])
      s2 = Cylinder(mag=[0, 0, val], dim=[2.5, 2])
      s4 = Cylinder(mag=[0, 0, val], dim=[2.5, 2])

      s1.move((r * math.cos(pi / 2 + phi), 0, r * math.sin(pi / 2 + phi)))
      s2.move((r * math.cos(2 * pi / 2 + phi), 0, r * math.sin(2 * pi / 2 + phi)))
      s3.move((r * math.cos(3 * pi / 2 + phi), 0, r * math.sin(3 * pi / 2 + phi)))
      s4.move((r * math.cos(phi), 0, r * math.sin(phi)))

      s1.rotate(2 * 90 - phi / pi * 180, [0, 1, 0])
      s2.rotate(1 * 90 - phi / pi * 180, [0, 1, 0])
      s3.rotate(0 * 90 - phi / pi * 180, [0, 1, 0])
      s4.rotate(3 * 90 - phi / pi * 180, [0, 1, 0])


      phi1 = -pi / (128) * i

      s5 = Cylinder(mag=[0, 0, -val], dim=[2.5, 2])
      s6 = Cylinder(mag=[0, 0, -val], dim=[2.5, 2])
      s7 = Cylinder(mag=[0, 0, -val], dim=[2.5, 2])
      s8 = Cylinder(mag=[0, 0, -val], dim=[2.5, 2])

      s5.move((r * math.cos(pi / 2 + phi1) + x0, 0, r * math.sin(pi / 2 + phi1)))
      s6.move((r * math.cos(2 * pi / 2 + phi1) + x0, 0, r * math.sin(2 * pi / 2 + phi1)))
      s7.move((r * math.cos(3 * pi / 2 + phi1) + x0, 0, r * math.sin(3 * pi / 2 + phi1)))
      s8.move((r * math.cos(phi1) + x0, 0, r * math.sin(phi1)))

      s5.rotate(2 * 90 - phi1 / pi * 180, [0, 1, 0])
      s6.rotate(1 * 90 - phi1 / pi * 180, [0, 1, 0])
      s7.rotate(0 * 90 - phi1 / pi * 180, [0, 1, 0])
      s8.rotate(3 * 90 - phi1 / pi * 180, [0, 1, 0])

      c = magpy.Collection(s1, s2, s3, s4, s5, s6, s7, s8)

      zs = np.linspace(-12, 12, res)
      xs = np.linspace(-10, 30, res)

      fig = plt.figure(figsize=(10, 6))

      ax2 = fig.add_subplot(111)
      B = []
      B1 = []
      num = 0

      for z in zs:
          num = num + 1
          print(f"{i}.png   {round(100*num/res, 1)}%")

          for x in xs:
              magnetic_field1 = c.getB([x, 0, z])

              aa = magnetic_field1[0]
              bb = magnetic_field1[1]
              cc = magnetic_field1[2]

              B1.append([aa, bb, cc])

              aa = abs(aa)
              bb = abs(bb)
              cc = abs(cc)

              aa = math.sqrt(aa)  #make colors more contrast
              bb = math.sqrt(bb)
              cc = math.sqrt(cc)

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