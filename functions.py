import math as mt
def get_d(a:float,b:float,c:float)->float:
  return mt.sqrt(a**2 + b**2 + c**2)
def get_par(a:float,b:float,c:float)->float:
  return a*b*c
def get_surf(a:float,b:float,c:float)->float:
  return 2* (a*b + a*c + b*c)

def get_alpha(a:float,b:float,c:float)->float:
  return  mt.degrees(mt.acos(a/mt.sqrt(a**2 + b**2 + c**2)))

def get_Beta(a:float,b:float,c:float)->float:
  return  mt.degrees(mt.acos(b/mt.sqrt(a**2 + b**2 + c**2)))

def get_Gamma(a:float,b:float,c:float)->float:
  return mt.degrees(mt.acos(c/mt.sqrt(a**2 + b**2 + c**2)))

def get_Rsphere(a:float,b:float,c:float)->float:
  return mt.sqrt(a**2 + b**2 + c**2) / 2

def get_Vsphere(a:float,b:float,c:float)->float:
  return 4/3*mt.pi * (mt.sqrt(a**2 + b**2 + c**2) / 2)**3