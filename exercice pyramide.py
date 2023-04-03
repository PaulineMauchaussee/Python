
""""
    *
   * *
  * * *
 * * * *
* * * * *

"""


nombre = int(input("Entrez un nombre positif: "))
for i in range (nombre):
    espace = " "*(nombre-i)
    print(espace + "* "*i)

