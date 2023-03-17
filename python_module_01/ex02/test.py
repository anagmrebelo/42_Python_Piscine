from vector import Vector


print("# TESTS CORRECTOS")
vec = Vector([[0.0], [1.0], [2.0], [3.0]])
vec2 = Vector([[0.0], [1.0], [2.0], [3.0]])
vec3 = Vector([[0.0, 1.0, 2.0, 3.0]])
vec4 = Vector([[0.0, 1.0, 2.0, 3.0]])
vec5 = Vector((10, 16))
vec6 = Vector((1, 4))
vec7 = Vector(4)
vec8 = Vector(5)
print("------------------repr------------------")
vec
vec2
vec3
vec4
vec5
vec6
vec7
vec8
# vec4 = Vector(3)
print("----------------------------------------")
print("------------------str------------------")
print(f'vec 1. {vec}')
print(f'vec 2. {vec2}')
print(f'vec 3. {vec3}')
print(f'vec 4. {vec4}')
print(f'vec 5. {vec5}')
print(f'vec 6. {vec6}')
print("----------------------------------------")
print("----------------product-----------------")
print(f"Product 1 * 2: {vec.dot(vec2)}")
print(f"Product 2 * 1: {vec2.dot(vec)}")
print("----------------------------------------")
vec3.T()
print("---------------transform----------------")
print(f"transfor 3: {vec3}")
vec3.T()
print(f"transfor 3: {vec3}")
print("----------------------------------------")
print("------------------add-------------------")
print(f" {vec3.values}   +   {vec4.values}   =   {vec3 + vec4}")
print(f" {vec4.values}   +   {vec3.values}   =   {vec4 + vec3}")
print(f" {vec.values}   +   {vec2.values}   =   {vec + vec2}")
print(f" {vec2.values}   +   {vec.values}   =   {vec2 + vec}")
print("----------------------------------------")
print("------------------sub-------------------")
print(f" {vec.values}   -   {vec2.values}   =   {vec - vec2}")
print(f" {vec2.values}   -   {vec.values}   =   {vec2 - vec}")
print("----------------------------------------")
print("----------------truediv-----------------")
print(f" {vec.values}   /   {2}\t =\t{vec / 2}")
print(f" {vec.values}   /   {0.75} =\t{vec / 0.75}")
print("----------------------------------------")
# print("----------------rtruediv----------------")
# print(f" {2} / {vec.values}\t =\t{2 / vec}")
# print(f" {0.75} / {vec.values} =\t{0.75 / vec}")
# print("----------------------------------------")
print("------------------mul-------------------")
print(f" {vec.values}   *   {2}\t =\t{vec * 2}")
print(f" {vec.values}   *   {0.75} =\t{vec * 0.75}")
print("----------------------------------------")
print("------------------rmul------------------")
print(f" {2} * {vec.values}\t=\t{2 * vec}")
print(f" {0.75} * {vec.values}\t=\t{0.75 * vec}")
print("----------------------------------------")


print("# TESTS DE ERRORES")

print("----------------------------------------")
try:
	vec = Vector([[0.0], [1.0], ['hola'], [3.0]])
except ValueError:
	print("Erro parseado correctamente")
try:
	vec = Vector([[0.0, 1.0, 'que onda', 3.0]])
except ValueError:
	print("Erro parseado correctamente")
try:
	vec = Vector([0.0, 1.0, 2.0, 3.0])
except ValueError:
	print("Erro parseado correctamente")
try:
	vec4 = Vector(3.7)
except ValueError:
	print("Erro parseado correctamente")
try:
	vec = Vector((1.2, 4))
except ValueError:
	print("Erro parseado correctamente")
try:
	vec = Vector((1, 4, 3))
except ValueError:
	print("Erro parseado correctamente")
try:
	vec = Vector([[1], [2]])
	print('Got it')
except ValueError:
	print("Erro parseado correctamente")
print("----------------------------------------")