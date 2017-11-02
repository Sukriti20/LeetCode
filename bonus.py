# Python3 code. Run the code with python 3 or greater version. With python2 precision of geo location is small hence will not produce spirograph curve
import math
f = open('BonusQ.kml','w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n<Document>\n')
f.write('<Placemark><name>SGM Building</name>\n')
f.write('<styleUrl>#z1</styleUrl><Point><coordinates>-118.289164,34.021204</coordinates></Point>\n')
f.write('</Placemark>\n')
f.write('<Placemark>\n')
f.write('<Polygon> <outerBoundaryIs>  <LinearRing>\n')
f.write('<coordinates>\n')


R=5
r=1
a=4
cos=math.cos
sin=math.sin
pi=math.pi
nRev=10
t=0.0
#sgm coordinates -118.289164,34.021204
while t<(pi*nRev):
    x=((R+r)*cos((r/R)*t)-a*cos((1+r/R)*t))
    y=((R+r)*sin((r/R)*t)-a*sin((1+r/R)*t))
    #print(str(-118.289164+x/10000)+','+str(34.021204+y/10000)+',0.')
    f.write(str(str(-118.289164+x/10000)+','+str(34.021204+y/10000)+',0.'+'\n'))
    t=t+0.01

f.write('</coordinates>\n</LinearRing> </outerBoundaryIs> </Polygon>')
f.write('<Style>\n')
f.write('<PolyStyle>\n')
f.write('<color>#a00000ff</color>\n')
f.write('<outline>0</outline>\n')
f.write('</PolyStyle>\n</Style>\n</Placemark>')
f.write('</Document>\n</kml>')
f.close()
