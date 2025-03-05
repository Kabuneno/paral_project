import json
import pathlib
import functions
with open('C:\\Pythonprojects_2.0\\paralelipipedes\\parallelepipeds.json', 'r') as f:
  parallelepipeds = json.load(f)
  print(parallelepipeds)

def getdata_(parallelepipedes)->dict:
  wholeresult = {}
  for i,g in parallelepipedes.items():
    res = {}
    a = float(g['a'])
    b = float(g['b'])
    c = float(g['c']) #чтение
    diagonal = functions.get_d(a,b,c)
    Vp = functions.get_par(a,b,c)
    S_surf = functions.get_surf(a,b,c)
    alpha = functions.get_alpha(a,b,c)
    Beta = functions.get_Beta(a,b,c)
    Gamma = functions.get_Gamma(a,b,c)
    Rsphere = functions.get_Rsphere(a,b,c)
    Vsphere = functions.get_Vsphere(a,b,c)
    res = ({"diag":diagonal,
          "volume": Vp ,
          "surface_area":S_surf,
          "alpha": alpha,
          "beta": Beta,
          "gamma":Gamma,
          "radius_described_sphere": Rsphere,
          "volume_described_sphere":Vsphere})
    wholeresult[i] = res
  return wholeresult


result = json.dumps(getdata_(parallelepipeds),indent=4)
pathlib.Path("response.json").write_text(result, encoding="utf-8")