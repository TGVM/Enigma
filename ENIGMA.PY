def Left( S ) :
  return S[1:] + S[0:1]

# Procura ch no disco D1 e vai na posicao correspondente em D2
"""
ch = F
D1 = ABCDEFGHIJ
          ^
D2 = ACGT%MUFOL
          ^
"""

def map( ch, D1, D2 ) :
  for p in range(len( D1 )) :
    if D1[p] == ch : break
  return D2[p]

def PlugIn( ch ):
  if ch == "A" : return "B"
  if ch == "S" : return "Z"
  if ch == "U" : return "Y"
  if ch == "G" : return "H"
  if ch == "L" : return "Q"
  if ch == "E" : return "N"
  return ch
  

def PlugOut( ch ) :
  if ch == "B" : return "A"
  if ch == "Z" : return "S" 
  if ch == "Y" : return "U" 
  if ch == "H" : return "G" 
  if ch == "Q" : return "L" 
  if ch == "N" : return "E" 
  return ch

def code( ch ) :
  global A1, S1
  global A2, S2
  global A3, S3

  """
  II I III
  Alfa

  A2
  S2

  A1
  S1

  A3
  S3

  R
  """
  
  A2 = Left( A2 )
  S2 = Left( S2 )
  
  ch = PlugIn( ch )
  ch = map( ch, Alfa, A2 )
  ch = map( ch, S2, A1 )
  ch = map( ch, S1, A3 )
  ch = map( ch, S3, R )
  ch = map( ch, Alfa, S3 )
  ch = map( ch, A3, S1 )
  ch = map( ch, A1, S2 )
  ch = map( ch, A2, Alfa )
  return PlugOut(ch)


def reset() :
# Linha 1 do scrambler começa com o alfabeto
# Linha 2 do scrambler começa com o scrambler original
  global A1, S1
  global A2, S2
  global A3, S3
  A1 = Alfa
  A2 = Alfa
  A3 = Alfa
  S1 = "UWYGADFPVZBECKMTHXSLRINQOJ"
  S2 = "AJPCZWRLFBDKOTYUQGENHXMIVS"
  S3 = "TAGBPCSDQEUFVNZHYIXJWLRKOM"
 
  #AEB
  for i in range(4) :
    A1 = Left( A1 )
    S1 = Left( S1 )
    
  A3 = Left( A3 )
  S3 = Left( S3 )
  
  
# Um alfabeto pra usar
Alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Refletor
R =    "YRUHQSLDPXNGOKMIEBFZCWVJAT"
A1 = S1 = ""
A2 = S2 = ""
A3 = S3 = ""

reset()


while ( True ) :
  print("Digite a sequência de caracteres a serem criptografadas: (segure ctrl+c para fechar o programa)")
  Lin = input()
  if Lin == "*" : reset()
  else :
    for i in range( len( Lin ) ):
      print( code( Lin[i] ), end='')
    print()

exit()

for j in range( 26 ) :
  Lin = "GYHRVFLRXY"
  for i in range( len( Lin ) ):
    print( code( Lin[i] ), end='')
  print()
  reset()
  for i in range( j ):
    A1 = Left( A1 )
    S1 = Left( S1 )

exit()