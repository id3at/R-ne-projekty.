import os

def generator_m3u(folder_glowny):
  """Generuje listę .m3u z folderu i podfolderów, plików .mp4. pliki zaczynają sie cyframi na koncu cyfry kropka i spacja"""

  with open(f"/home/id3at/Pulpit/playlis.m3u", "w") as f:
    lista_fold = (os.listdir(folder_glowny))
    lista_fold_posegregowana =  sorted(lista_fold, key=lambda lista_fold: int(lista_fold[:3].rstrip(". ")) if int(lista_fold[:3].rstrip(". ").isdigit()) else False)

   
    for nazwa_podfolderu in lista_fold_posegregowana:

      if os.path.isdir(f"{folder_glowny}/{nazwa_podfolderu}"):
        podfolder = os.listdir(f"{folder_glowny}/{nazwa_podfolderu}")
        # Podfolder
        for plik in sorted(podfolder,key=lambda podfolder: int(podfolder[:2].rstrip(". ").lstrip("."))):
          if plik.endswith(".mp4"):
            f.write(f"{nazwa_podfolderu}/{plik}\n")
      else:
        # Plik
        f.write(f"{nazwa_podfolderu}\n")


folder_glowny = "/media/id3at/kursudemy/100 Days of Code - The Complete Python Pro Bootcamp for 2021/[TutsNode.com] - 100 Days of Code - The Complete Python Pro Bootcamp for 2021"
generator_m3u(folder_glowny)
